from parser import PrintNode, LetNode, IfNode, ConditionNode

class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.generated_code = []
        self.variables = set()
        self.current_indent = 0  # Добавляем инициализацию отступа

    def generate(self):
        """Генерирует Python-код из AST"""
        self.generated_code.append("# Generated Python code from BASIC")
        self.generated_code.append("")

        for node in self.ast:
            self.generate_node(node)

        return "\n".join(self.generated_code)

    def generate_node(self, node):
        """Генерирует код для конкретного узла AST"""
        if isinstance(node, PrintNode):
            self.generate_print(node)
        elif isinstance(node, LetNode):
            self.generate_let(node)
        elif isinstance(node, IfNode):
            self.generate_if(node)
        else:
            raise ValueError(f"Unknown node type: {type(node)}")

    def generate_print(self, node):
        """Генерирует код для PRINT"""
        value = node.value
        # Если это строка в кавычках, убираем внешние кавычки BASIC
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        indent = "    " * self.current_indent
        self.generated_code.append(f"{indent}print({repr(value)})")

    def generate_let(self, node):
        """Генерирует код для LET"""
        var_name = node.var_name
        value = node.value

        # Добавляем переменную в набор известных переменных
        self.variables.add(var_name)

        # Обрабатываем значение
        if value.isdigit():
            # Целое число
            processed_value = value
        elif value.replace('.', '', 1).isdigit():
            # Дробное число
            processed_value = value
        elif value.startswith('"') and value.endswith('"'):
            # Строка
            processed_value = repr(value[1:-1])
        elif value in self.variables:
            # Переменная
            processed_value = value
        else:
            raise ValueError(f"Invalid value for LET: {value}")

        indent = "    " * self.current_indent
        self.generated_code.append(f"{indent}{var_name} = {processed_value}")

    def generate_if(self, node):
        """Генерирует код для IF-THEN"""
        condition = node.condition
        then_branch = node.then_branch

        # Генерируем условие
        condition_code = f"{condition.left} {self.translate_operator(condition.operator)} {condition.right}"
        indent = "    " * self.current_indent
        self.generated_code.append(f"{indent}if {condition_code}:")

        self.current_indent += 1

        # Генерируем все команды в THEN-ветке
        for stmt in then_branch:
            if isinstance(stmt, PrintNode):
                self.generate_print(stmt)
            else:
                raise ValueError(f"Unsupported statement in THEN branch: {type(stmt)}")

        # Возвращаем отступ
        self.current_indent -= 1

    def translate_operator(self, op):
        """Переводит операторы BASIC в операторы Python"""
        translations = {
            "=": "==",
            ">": ">",
            "<": "<"
        }
        return translations.get(op, op)


def generate_python_code(ast):
    """Основная функция для генерации кода"""
    generator = CodeGenerator(ast)
    return generator.generate()


# Тестирование
if __name__ == "__main__":
    from parser import Parser
    import lexer

    test_code = '''
    PRINT "Hello, BASIC!"
    LET X = 10
    IF X > 5 THEN PRINT "X is greater than 7"
    END
    '''

    tokens = lexer.lexer(test_code)
    parser = Parser(tokens)
    ast = parser.parse()

    python_code = generate_python_code(ast)
    print(python_code)