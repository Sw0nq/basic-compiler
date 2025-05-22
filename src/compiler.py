import os
import sys
from antlr4 import InputStream, CommonTokenStream
from generated.BasicLexer import BasicLexer
from generated.BasicParser import BasicParser
from ast_builder import AstBuilder
from ast_nodes import LabelNode, GotoNode, ProgramNode, GosubNode
from semantic_analyzer import SemanticAnalyzer
from code_generator import CodeGenerator
from optimizers import create_default_pipeline


def resolve_labels(program_node):
    labels = {}
    for stmt in program_node.statements:
        if isinstance(stmt, LabelNode):
            labels[stmt.name] = stmt
        if hasattr(stmt, 'line_number') and stmt.line_number is not None:
            labels[stmt.line_number] = stmt

    for stmt in program_node.statements:
        if isinstance(stmt, GotoNode) or isinstance(stmt, GosubNode):
            if stmt.target_label_ref.name_or_number in labels:
                stmt.target_label_ref.target = labels[stmt.target_label_ref.name_or_number]
                stmt.target_label_ref.resolved = True


def compile_and_print_ast(basic_code_string, test_name="Test", enable_optimizations=False):
    print(f"--- {test_name} ---")
    print("Исходный BASIC код:")
    print(basic_code_string.strip())
    print("-" * 20)

    input_stream = InputStream(basic_code_string)
    lexer = BasicLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = BasicParser(token_stream)
    parse_tree = parser.program()

    ast_builder = AstBuilder()
    ast_root = ast_builder.visit(parse_tree)

    if isinstance(ast_root, ProgramNode):
        resolve_labels(ast_root)

    print("Абстрактное Синтаксическое Дерево (AST):")
    if ast_root:
        if hasattr(ast_root, 'display') and callable(ast_root.display):
            ast_root.display()
        elif hasattr(ast_root, 'statements'):
            for i, statement_node in enumerate(ast_root.statements):
                print(f"  Statement {i + 1}: {statement_node!r}")
        else:
            print(f"  Root: {ast_root!r}")
    else:
        print("AST не было построено или оно пустое.")
    return ast_root


def compile_basic_to_python(basic_code_string, output_file=None, enable_optimizations=True, debug=False):
    input_stream = InputStream(basic_code_string)
    lexer = BasicLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = BasicParser(token_stream)
    parse_tree = parser.program()
    ast_builder = AstBuilder()
    ast_root = ast_builder.visit(parse_tree)

    if not isinstance(ast_root, ProgramNode):
        return None, ["Ошибка: не удалось построить AST"]

    resolve_labels(ast_root)

    analyzer = SemanticAnalyzer()
    semantic_errors = analyzer.analyze(ast_root)

    if semantic_errors and debug:
        print("Семантические ошибки:")
        for error in semantic_errors:
            print(f"  - {error}")

    if enable_optimizations:
        optimizer = create_default_pipeline()
        ast_root = optimizer.optimize(ast_root)

        if debug:
            print("Оптимизированное AST:")
            ast_root.display()

    code_generator = CodeGenerator()
    python_code = code_generator.generate(ast_root)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(python_code)

        if debug:
            print(f"Python код сохранен в {output_file}")

    return python_code, semantic_errors


def compile_and_run(basic_code_string, output_file=None, run=False, enable_optimizations=True, debug=False):
    python_code, semantic_errors = compile_basic_to_python(
        basic_code_string, output_file, enable_optimizations, debug
    )

    if run and not semantic_errors and python_code:
        if output_file:
            dirname = os.path.dirname(output_file)
            filename = os.path.basename(output_file)

            if dirname:
                cwd = os.getcwd()
                os.chdir(dirname)

            try:
                import subprocess
                subprocess.call([sys.executable, filename])
            finally:
                if dirname:
                    os.chdir(cwd)
        else:
            try:
                exec(python_code)
            except Exception as e:
                print(f"Ошибка выполнения: {e}")

    return python_code, semantic_errors

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.rsplit('.', 1)[0] + '.py'

        with open(input_file, 'r') as f:
            basic_code = f.read()

        print(f"Компиляция {input_file} в {output_file}")
        python_code, errors = compile_and_run(basic_code, output_file, '--run' in sys.argv, '--debug' in sys.argv)

        if errors:
            print("Ошибки:")
            for error in errors:
                print(f"  - {error}")
    else:
        test_expressions = """
        PRINT 1 + 2 * 3
        LET A = (10 - 2) / 4
        LET B% = -A + 5
        PRINT B% > 0
        PRINT "A="; A, "B%="; B%
        
        END
        """
        compile_and_print_ast(test_expressions, "Expressions Test")

        test_if_only = """
        LET X = 10
        IF  X = 10 THEN PRINT "X is 10"
        END
        """
        compile_and_print_ast(test_if_only, "IF Only Test")

        test_if_goto_labels = """
        START:
        LET X = 10
        IF X = 10 THEN GOTO SUCCESS
        PRINT "This should be skipped"
        GOTO FAIL

        SUCCESS:
        PRINT "Success! X is 10."
        GOTO END_PROGRAM
        
        FAIL:
        PRINT "Failure or X is not 10."
        
        END_PROGRAM:
        END
        """
        compile_and_print_ast(test_if_goto_labels, "IF, GOTO, Labels Test")

        test_loops_gosub = """
        PRINT "FOR Loop:"
        FOR I = 1 TO 5 STEP 2
            PRINT "I ="; I
        NEXT I

        PRINT "WHILE Loop:"
        LET J = 0
        WHILE J < 3
            PRINT "J ="; J
            LET J = J + 1
        WEND

        PRINT "Testing GOSUB"
        GOSUB MYSUB
        PRINT "Returned from GOSUB"
        END

        MYSUB:
        PRINT "Inside MYSUB"
        RETURN
        """
        compile_and_print_ast(test_loops_gosub, "Loops and GOSUB Test")

        test_input_vars = """
        INPUT "Enter name: ", N$
        INPUT V1, V2%
        PRINT "Hello, "; N$
        PRINT "V1:"; V1, "V2%:"; V2%
        END
        """
        compile_and_print_ast(test_input_vars, "INPUT and Variables Test")

        test_optimizations = """
        LET X = 2 + 3 * 4  ' Должно быть оптимизировано в X = 14
        PRINT X
        GOTO EXIT          ' Код после GOTO должен быть удален как недостижимый
        PRINT "This should be removed"
        
        EXIT:
        PRINT "End of program"
        END
        """
        ast = compile_and_print_ast(test_optimizations, "Before Optimizations")

        optimizer = create_default_pipeline()
        optimized_ast = optimizer.optimize(ast)

        print("\nПосле оптимизаций:")
        optimized_ast.display()

        code_generator = CodeGenerator()
        python_code = code_generator.generate(optimized_ast)

        print("\nСгенерированный Python код:")
        print(python_code)
