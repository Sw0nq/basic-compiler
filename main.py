from lexer import lexer
from parser import Parser
from codegen import generate_python_code

def main():
    # Читаем код из файла
    with open("examples/input.txt", "r", encoding="utf-8") as f:
        code = f.read()

    # Лексический анализ
    tokens = lexer(code)
    print("\n🔹 Токены:", tokens)

    # Синтаксический анализ
    parser = Parser(tokens)
    ast = parser.parse()
    print("\n🔹 AST:", ast)

    # Генерация кода
    generated_code = generate_python_code(ast)
    print("\n🔹 Сгенерированный код:\n", generated_code)

    # Сохраняем сгенерированный код в файл
    with open("examples/output.py", "w", encoding="utf-8") as f:
        f.write(generated_code)

    # Запускаем сгенерированный код
    print("\n🔹 Результат выполнения:")
    exec(generated_code)

if __name__ == "__main__":
    main()
