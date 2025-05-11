# Файл: BasicCompiler/src/compiler.py

import os
import sys
from antlr4 import InputStream, CommonTokenStream
# Используем относительные импорты
from generated.BasicLexer import BasicLexer
from generated.BasicParser import BasicParser
from ast_builder import AstBuilder
from ast_nodes import LabelNode, GotoNode, ProgramNode, GosubNode
from semantic_analyzer import SemanticAnalyzer
from code_generator import CodeGenerator
from optimizers import create_default_pipeline


def resolve_labels(program_node):
    labels = {}
    # Первый проход: сбор всех меток
    for stmt in program_node.statements:
        if isinstance(stmt, LabelNode):
            labels[stmt.name] = stmt
        # Добавляем поддержку числовых меток, если они есть
        if hasattr(stmt, 'line_number') and stmt.line_number is not None:
            labels[stmt.line_number] = stmt

    # Второй проход: разрешение ссылок
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

    # Можно добавить свой ErrorListener для более красивого вывода ошибок ANTLR
    # parser.removeErrorListeners() # Удалить стандартный listener
    # parser.addErrorListener(MyCustomErrorListener()) # Добавить свой

    parse_tree = parser.program() # Запускаем парсинг с правила 'program'

    ast_builder = AstBuilder()
    ast_root = ast_builder.visit(parse_tree)

    if isinstance(ast_root, ProgramNode):
        resolve_labels(ast_root)

    print("Абстрактное Синтаксическое Дерево (AST):")
    if ast_root:
        if hasattr(ast_root, 'display') and callable(ast_root.display):
            ast_root.display() # Используем новый метод display
        elif hasattr(ast_root, 'statements'): # Старый способ, если display нет
            for i, statement_node in enumerate(ast_root.statements):
                print(f"  Statement {i+1}: {statement_node!r}")
        else:
            print(f"  Root: {ast_root!r}")
    else:
        print("AST не было построено или оно пустое.")
    
    # Возвращаем AST для возможной дальнейшей обработки
    return ast_root


def compile_basic_to_python(basic_code_string, output_file=None, enable_optimizations=True, debug=False):
    """
    Компилирует BASIC код в Python и опционально записывает в файл.
    
    Args:
        basic_code_string: Исходный код на BASIC
        output_file: Имя выходного файла для Python кода
        enable_optimizations: Включить оптимизации
        debug: Режим отладки (печатать промежуточные результаты)
    
    Returns:
        Кортеж (python_code, semantic_errors) с результатами компиляции
    """
    # Парсинг и построение AST
    input_stream = InputStream(basic_code_string)
    lexer = BasicLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = BasicParser(token_stream)
    parse_tree = parser.program()
    
    # Построение AST
    ast_builder = AstBuilder()
    ast_root = ast_builder.visit(parse_tree)
    
    if not isinstance(ast_root, ProgramNode):
        return None, ["Ошибка: не удалось построить AST"]
    
    # Разрешение ссылок на метки
    resolve_labels(ast_root)
    
    # Семантический анализ
    analyzer = SemanticAnalyzer()
    semantic_errors = analyzer.analyze(ast_root)
    
    if semantic_errors and debug:
        print("Семантические ошибки:")
        for error in semantic_errors:
            print(f"  - {error}")
    
    # Оптимизация
    if enable_optimizations:
        optimizer = create_default_pipeline()
        ast_root = optimizer.optimize(ast_root)
        
        if debug:
            print("Оптимизированное AST:")
            ast_root.display()
    
    # Генерация кода
    code_generator = CodeGenerator()
    python_code = code_generator.generate(ast_root)
    
    # Запись в файл, если указан
    if output_file:
        with open(output_file, 'w') as f:
            f.write(python_code)
        
        if debug:
            print(f"Python код сохранен в {output_file}")
    
    return python_code, semantic_errors


def compile_and_run(basic_code_string, output_file=None, run=False, enable_optimizations=True, debug=False):
    """
    Компилирует BASIC код в Python, опционально записывает в файл и запускает.
    
    Args:
        basic_code_string: Исходный код на BASIC
        output_file: Имя выходного файла для Python кода
        run: Запустить сгенерированный код
        enable_optimizations: Включить оптимизации
        debug: Режим отладки (печатать промежуточные результаты)
    
    Returns:
        Кортеж (python_code, semantic_errors) с результатами компиляции
    """
    python_code, semantic_errors = compile_basic_to_python(
        basic_code_string, output_file, enable_optimizations, debug
    )
    
    # Запускаем код, если нужно и нет семантических ошибок
    if run and not semantic_errors and python_code:
        if output_file:
            # Запускаем сгенерированный файл
            dirname = os.path.dirname(output_file)
            filename = os.path.basename(output_file)
            
            if dirname:
                cwd = os.getcwd()
                os.chdir(dirname)
            
            try:
                # Здесь мы запускаем Python скрипт как отдельный процесс
                import subprocess
                subprocess.call([sys.executable, filename])
            finally:
                if dirname:
                    os.chdir(cwd)
        else:
            # Выполняем код прямо здесь
            try:
                exec(python_code)
            except Exception as e:
                print(f"Ошибка выполнения: {e}")
    
    return python_code, semantic_errors


# --- Тестовый запуск ---
if __name__ == "__main__":
    # Проверка аргументов командной строки
    if len(sys.argv) > 1:
        # Компиляция файла
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
        # Запуск тестовых примеров
        test_expressions = """
        PRINT 1 + 2 * 3
        LET A = (10 - 2) / 4
        LET B% = -A + 5
        PRINT B% > 0
        PRINT "A="; A, "B%="; B%
        
        END
        """
        compile_and_print_ast(test_expressions, "Expressions Test")

        # Тестирование только инструкции IF с явной табуляцией между IF и переменной
        test_if_only = """
        LET X = 10
        IF\tX = 10 THEN PRINT "X is 10"
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
        # INPUT потребует реального ввода, для автоматического теста это сложно.
        # Пока просто проверим парсинг.
        compile_and_print_ast(test_input_vars, "INPUT and Variables Test")
        
        # Пример с оптимизациями
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
        
        # Применяем оптимизации
        optimizer = create_default_pipeline()
        optimized_ast = optimizer.optimize(ast)
        
        print("\nПосле оптимизаций:")
        optimized_ast.display()
        
        # Генерация Python кода
        code_generator = CodeGenerator()
        python_code = code_generator.generate(optimized_ast)
        
        print("\nСгенерированный Python код:")
        print(python_code)