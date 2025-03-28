import re

# 🔹 Определяем типы токенов
TOKEN_SPECIFICATION = [
    ("NUMBER", r"\d+(\.\d*)?"),  # Числа (целые и дробные)
    ("STRING", r'"[^"]*"'),      # Строки в кавычках
    ("PRINT", r"PRINT"),         # Команда PRINT
    ("LET", r"LET"),             # Присваивание LET X = 10
    ("IF", r"IF"),               # Условие
    ("THEN", r"THEN"),           # THEN
    ("GOTO", r"GOTO"),           # Переход по метке
    ("END", r"END"),             # Конец программы
    ("ID", r"[A-Za-z_][A-Za-z0-9_]*"),  # Переменные (X, Y, count)
    ("OP", r"[+\-*/=<>]"),         # Операторы (+ - * / =)
    ("NEWLINE", r"\n"),          # Конец строки
    ("SKIP", r"[ \t]+"),         # Пробелы (пропускаем)
    ("MISMATCH", r".")           # Ошибка
]

TOKEN_RE = re.compile("|".join(f"(?P<{name}>{regex})" for name, regex in TOKEN_SPECIFICATION))


# 🔹 Функция лексического анализа
def lexer(code):
    tokens = []
    for match in TOKEN_RE.finditer(code):
        kind = match.lastgroup
        value = match.group()
        if kind == "SKIP":
            continue
        elif kind == "MISMATCH":
            raise SyntaxError(f"Unexpected character: {value}")
        tokens.append((kind, value))
    return tokens


# 🔹 Тестовый запуск
if __name__ == "__main__":
    code = '''
    PRINT "Hello, BASIC!"
    LET X = 10
    IF X > 5 THEN PRINT "X is greater than 5"
    END
    '''
    print(lexer(code))
