import lexer  # Импортируем наш лексер


class Node:
    """ Базовый класс узла AST """
    pass


class PrintNode(Node):
    def __init__(self, value):
        self.value = value


class LetNode(Node):
    def __init__(self, var_name, value):
        self.var_name = var_name
        self.value = value


class IfNode(Node):
    def __init__(self, condition, then_branch):
        self.condition = condition
        self.then_branch = then_branch


class ConditionNode(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"ConditionNode(left={self.left}, operator={self.operator}, right={self.right})"


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consume(self):
        """Получает текущий токен и переходит к следующему"""
        if self.pos >= len(self.tokens):
            raise SyntaxError("Ошибка: неожиданный конец входных данных (нехватает токенов)")
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def parse(self):
        """ Основная функция парсинга, обрабатывает весь код """
        statements = []

        while self.pos < len(self.tokens):
            token_type, token_value = self.tokens[self.pos]

            if token_type == "NEWLINE":
                self.consume()
                continue  # Пропускаем пустые строки

            elif token_type == "PRINT":
                self.consume()  # Пропускаем PRINT
                expr = self.consume()
                if expr[0] not in ("STRING", "ID"):
                    raise SyntaxError(f"Ожидалась строка или переменная в PRINT, но получено: {expr}")
                statements.append(PrintNode(expr[1]))

            elif token_type == "LET":
                self.consume()  # Пропускаем LET
                var_name = self.consume()
                if var_name[0] != "ID":
                    raise SyntaxError(f"Ожидалось имя переменной, но получено: {var_name}")

                eq = self.consume()
                if eq[0] != "OP" or eq[1] != "=":
                    raise SyntaxError(f"Ожидался знак '=', но получено: {eq}")

                value = self.consume()
                if value[0] not in ("NUMBER", "STRING", "ID"):
                    raise SyntaxError(f"Ожидалось значение, но получено: {value}")

                statements.append(LetNode(var_name[1], value[1]))

            elif token_type == "IF":
                self.consume()  # Пропускаем IF
                left = self.consume()
                if left[0] != "ID":
                    raise SyntaxError(f"Ожидалась переменная в условии IF, но получено: {left}")

                operator = self.consume()
                if operator[0] != "OP" or operator[1] not in ("=", ">", "<"):
                    raise SyntaxError(f"Ожидался оператор сравнения в IF, но получено: {operator}")

                right = self.consume()
                if right[0] not in ("NUMBER", "ID"):
                    raise SyntaxError(f"Ожидалось число или переменная в правой части IF, но получено: {right}")

                then = self.consume()
                if then[0] != "THEN":
                    raise SyntaxError(f"Ожидалось THEN, но получено: {then}")

                # Парсим вложенные выражения внутри THEN (например, PRINT)
                then_statements = []
                while self.pos < len(self.tokens) and self.tokens[self.pos][0] not in ("NEWLINE", "END"):
                    then_statements.append(self.consume())

                statements.append(IfNode(ConditionNode(left[1], operator[1], right[1]), then_statements))

            elif token_type == "END":
                self.consume()  # Пропускаем END
                break

            else:
                raise SyntaxError(f"Unexpected token: {token_value}")

        return statements



# Тест парсера
if __name__ == "__main__":
    code = '''
    PRINT "Hello, BASIC!"
    LET X = 10
    IF X > 5 THEN PRINT "X is greater than 5"
    END
    '''
    tokens = lexer.lexer(code)
    parser = Parser(tokens)
    ast = parser.parse()

    for node in ast:
        print(vars(node))
