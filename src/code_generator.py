# Файл: BasicCompiler/src/code_generator.py

from ast_nodes import (
    ProgramNode, PrintNode, LetNode, EndNode, IfNode, GotoNode, LabelReferenceNode,
    ForNode, NextNode, GosubNode, ReturnNode, WhileNode, InputNode,
    NumberNode, StringNode, VariableNode, BinaryOpNode, UnaryOpNode, LabelNode
)

class CodeGenerator:
    """Класс для генерации Python кода из AST дерева"""
    
    def __init__(self):
        self.labels = {}  # name -> метка для инструкции перехода
        self.indent_level = 0
        self.current_line = 0
        self.code_lines = []
        self.forward_jumps = {}  # Для разрешения переходов на метки, которые еще не встречались
        self.for_loops = {}  # Для хранения информации о циклах FOR
        self.while_stack = []  # Для хранения информации о циклах WHILE
        self.gosub_calls = []  # Для хранения информации о вызовах GOSUB
    
    def generate(self, ast_root):
        """Основной метод для генерации Python кода"""
        if not isinstance(ast_root, ProgramNode):
            raise ValueError("Ожидается корень AST дерева типа ProgramNode")
        
        # Добавляем необходимые импорты для runtime
        self._add_line("# Генерированный код из BASIC")
        self._add_line("import sys")
        self._add_line("import math")
        
        # Добавляем вспомогательные функции и классы
        self._add_runtime_helpers()
        
        # Объявляем переменные для госабов и циклов
        self._add_line("")
        self._add_line("# Переменные для управления потоком выполнения")
        self._add_line("_gosub_return_points = []")
        
        # Точка входа - основная часть программы
        self._add_line("")
        self._add_line("def main():")
        self.indent_level += 1
        
        # Объявляем, что переменные будут глобальными
        self._add_line("# Все переменные будут глобальными")
        self._add_line("global _gosub_return_points")
        
        # Генерируем код для всех инструкций программы
        self._add_line("")
        
        # Добавляем метки для каждой строки
        self._collect_labels(ast_root)
        
        # Генерируем код для всех инструкций
        self._generate_statements(ast_root.statements)
        
        # Добавляем инструкцию возврата для конца программы
        if self.code_lines and not self.code_lines[-1].endswith("sys.exit(0)"):
            self._add_line("return  # Конец программы")
        
        # Добавляем точку входа
        self.indent_level = 0
        self._add_line("")
        self._add_line("if __name__ == '__main__':")
        self.indent_level += 1
        self._add_line("main()")
        
        # Возвращаем сгенерированный код
        return "\n".join(self.code_lines)
    
    def _add_runtime_helpers(self):
        """Добавляет вспомогательные функции и классы для runtime"""
        self._add_line("")
        self._add_line("# Вспомогательные функции для runtime BASIC")
        
        # Функция для PRINT
        self._add_line("def basic_print(*args, sep=''):")
        self.indent_level += 1
        self._add_line("for i, arg in enumerate(args):")
        self._add_line("    if i > 0:")
        self._add_line("        sys.stdout.write(sep)")
        self._add_line("    sys.stdout.write(str(arg))")
        self._add_line("sys.stdout.write('\\n')")
        self.indent_level -= 1
        
        # Функция для INPUT
        self._add_line("")
        self._add_line("def basic_input(prompt=None):")
        self.indent_level += 1
        self._add_line("if prompt:")
        self._add_line("    sys.stdout.write(prompt)")
        self._add_line("return input()")
        self.indent_level -= 1
        
        # Класс для строк BASIC с автоматическим приведением типов
        self._add_line("")
        self._add_line("class BasicString(str):")
        self.indent_level += 1
        self._add_line("def __add__(self, other):")
        self._add_line("    return BasicString(super().__add__(str(other)))")
        self._add_line("")
        self._add_line("def __radd__(self, other):")
        self._add_line("    return BasicString(str(other) + self)")
        self.indent_level -= 1
        
        self.indent_level = 0
    
    def _collect_labels(self, program_node):
        """Собирает все метки для GOTO и GOSUB"""
        for i, stmt in enumerate(program_node.statements):
            if isinstance(stmt, LabelNode):
                self.labels[stmt.name] = f"label_{stmt.name.replace(':', '')}"
    
    def _add_line(self, line):
        """Добавляет строку кода с соответствующим отступом"""
        self.code_lines.append("    " * self.indent_level + line)
        self.current_line += 1
    
    def _generate_statements(self, statements):
        """Генерирует код для последовательности инструкций"""
        for stmt in statements:
            if isinstance(stmt, LetNode):
                self._generate_let(stmt)
            elif isinstance(stmt, PrintNode):
                self._generate_print(stmt)
            elif isinstance(stmt, IfNode):
                self._generate_if(stmt)
            elif isinstance(stmt, GotoNode):
                self._generate_goto(stmt)
            elif isinstance(stmt, ForNode):
                self._generate_for(stmt)
            elif isinstance(stmt, NextNode):
                self._generate_next(stmt)
            elif isinstance(stmt, GosubNode):
                self._generate_gosub(stmt)
            elif isinstance(stmt, ReturnNode):
                self._generate_return(stmt)
            elif isinstance(stmt, WhileNode):
                self._generate_while(stmt)
            elif isinstance(stmt, InputNode):
                self._generate_input(stmt)
            elif isinstance(stmt, EndNode):
                self._generate_end(stmt)
            elif isinstance(stmt, LabelNode):
                self._generate_label(stmt)
    
    def _generate_let(self, let_node):
        """Генерирует код для инструкции LET"""
        var_name = self._format_variable_name(let_node.variable)
        value_expr = self._generate_expression(let_node.value)
        
        # Добавляем приведение типа, если нужно
        if let_node.variable.type_suffix == '$':
            value_expr = f"BasicString({value_expr})"
        elif let_node.variable.type_suffix == '%':
            value_expr = f"int({value_expr})"
        
        self._add_line(f"{var_name} = {value_expr}")
    
    def _generate_print(self, print_node):
        """Генерирует код для инструкции PRINT"""
        if not print_node.expressions_with_separators:
            self._add_line("basic_print()")
            return
        
        args = []
        for item in print_node.expressions_with_separators:
            expr = self._generate_expression(item['expression'])
            args.append(expr)
        
        args_str = ", ".join(args)
        self._add_line(f"basic_print({args_str})")
    
    def _generate_if(self, if_node):
        """Генерирует код для инструкции IF"""
        condition = self._generate_expression(if_node.condition)
        self._add_line(f"if {condition}:")
        self.indent_level += 1
        
        # Генерируем код для ветки THEN
        if if_node.then_branch:
            self._generate_statements([if_node.then_branch])
        else:
            self._add_line("pass")
        
        self.indent_level -= 1
        
        # Генерируем код для ветки ELSE, если есть
        if if_node.else_branch:
            self._add_line("else:")
            self.indent_level += 1
            self._generate_statements([if_node.else_branch])
            self.indent_level -= 1
    
    def _generate_goto(self, goto_node):
        """Генерирует код для инструкции GOTO"""
        target_ref = goto_node.target_label_ref
        label_name = target_ref.name_or_number
        
        if label_name in self.labels:
            # Если метка уже есть, генерируем переход
            self._add_line(f"# GOTO {label_name}")
            self._add_line(f"return {self.labels[label_name]}()")
        else:
            # Если метки еще нет, добавляем в список для последующего разрешения
            self._add_line(f"# GOTO {label_name} (forward jump)")
            self._add_line(f"return label_{label_name}()")
            self.forward_jumps[label_name] = True
    
    def _generate_for(self, for_node):
        """Генерирует код для инструкции FOR"""
        loop_var = self._format_variable_name(for_node.loop_variable)
        start_expr = self._generate_expression(for_node.start_value)
        end_expr = self._generate_expression(for_node.end_value)
        
        # Генерируем инициализацию переменной цикла
        self._add_line(f"{loop_var} = {start_expr}")
        
        # Определяем шаг цикла
        if for_node.step_value:
            step_expr = self._generate_expression(for_node.step_value)
            self._add_line(f"{loop_var}_step = {step_expr}")
        else:
            self._add_line(f"{loop_var}_step = 1")
        
        # Определяем конечное значение
        self._add_line(f"{loop_var}_end = {end_expr}")
        
        # Генерируем проверку условия цикла
        loop_label = f"for_loop_{loop_var}_{self.current_line}"
        self._add_line(f"# FOR {loop_var} = {start_expr} TO {end_expr}")
        self._add_line(f"def {loop_label}():")
        self.indent_level += 1
        
        # Проверка условия продолжения цикла
        self._add_line(f"if ({loop_var}_step > 0 and {loop_var} <= {loop_var}_end) or ({loop_var}_step < 0 and {loop_var} >= {loop_var}_end):")
        
        # Сохраняем информацию о цикле
        self.for_loops[loop_var] = {
            "label": loop_label,
            "step_var": f"{loop_var}_step",
            "end_var": f"{loop_var}_end"
        }
    
    def _generate_next(self, next_node):
        """Генерирует код для инструкции NEXT"""
        for var in next_node.variables:
            var_name = self._format_variable_name(var)
            
            if var_name in self.for_loops:
                loop_info = self.for_loops[var_name]
                
                # Инкрементируем переменную цикла
                self._add_line(f"{var_name} += {loop_info['step_var']}")
                
                # Повторяем цикл
                self._add_line(f"return {loop_info['label']}()")
                
                # Закрываем блок if от предыдущего цикла
                self.indent_level -= 1
                
                # Удаляем цикл из стека
                del self.for_loops[var_name]
            else:
                self._add_line(f"# Ошибка: NEXT {var_name} без соответствующего FOR")
    
    def _generate_gosub(self, gosub_node):
        """Генерирует код для инструкции GOSUB"""
        target_ref = gosub_node.target_label_ref
        return_label = f"gosub_return_{self.current_line}"
        
        # Добавляем метку возврата в стек
        self._add_line(f"# GOSUB {target_ref.name_or_number}")
        self._add_line(f"_gosub_return_points.append({return_label})")
        
        # Генерируем переход на подпрограмму
        if target_ref.name_or_number in self.labels:
            self._add_line(f"return {self.labels[target_ref.name_or_number]}()")
        else:
            self._add_line(f"return label_{target_ref.name_or_number}()")
            self.forward_jumps[target_ref.name_or_number] = True
        
        # Генерируем точку возврата
        self._add_line(f"def {return_label}():")
        self.indent_level += 1
        
        # Сохраняем информацию о вызове
        self.gosub_calls.append(return_label)
    
    def _generate_return(self, return_node):
        """Генерирует код для инструкции RETURN"""
        self._add_line("# RETURN")
        self._add_line("if _gosub_return_points:")
        self.indent_level += 1
        self._add_line("return_point = _gosub_return_points.pop()")
        self._add_line("return return_point()")
        self.indent_level -= 1
        self._add_line("else:")
        self.indent_level += 1
        self._add_line("# Ошибка: RETURN без соответствующего GOSUB")
        self._add_line("return")
        self.indent_level -= 1
        
        # Закрываем блок для предыдущего GOSUB, если был открыт
        if self.gosub_calls:
            self.indent_level -= 1
            self.gosub_calls.pop()
    
    def _generate_while(self, while_node):
        """Генерирует код для инструкции WHILE"""
        condition = self._generate_expression(while_node.condition)
        
        # Генерируем метку начала цикла
        loop_label = f"while_loop_{self.current_line}"
        self._add_line(f"# WHILE {condition}")
        self._add_line(f"def {loop_label}():")
        self.indent_level += 1
        
        # Проверка условия
        self._add_line(f"if {condition}:")
        self.indent_level += 1
        
        # Сохраняем информацию о цикле
        self.while_stack.append(loop_label)
        
        # Генерируем тело цикла
        self._generate_statements(while_node.body)
        
        # Повторяем цикл
        self._add_line(f"return {loop_label}()")
        self.indent_level -= 1
        self._add_line("# WEND")
        
        # Удаляем цикл из стека
        self.while_stack.pop()
    
    def _generate_input(self, input_node):
        """Генерирует код для инструкции INPUT"""
        if input_node.prompt:
            prompt_expr = self._generate_expression(input_node.prompt)
            self._add_line(f"input_value = basic_input({prompt_expr})")
        else:
            self._add_line("input_value = basic_input()")
        
        # Если переменных несколько, разбиваем ввод по запятым
        if len(input_node.variables) > 1:
            self._add_line("input_values = input_value.split(',')")
            
            for i, var in enumerate(input_node.variables):
                var_name = self._format_variable_name(var)
                self._add_line(f"if len(input_values) > {i}:")
                self.indent_level += 1
                
                # Преобразуем значение в зависимости от типа переменной
                if var.type_suffix == '$':
                    self._add_line(f"{var_name} = BasicString(input_values[{i}].strip())")
                elif var.type_suffix == '%':
                    self._add_line(f"try:")
                    self._add_line(f"    {var_name} = int(float(input_values[{i}].strip()))")
                    self._add_line("except ValueError:")
                    self._add_line(f"    {var_name} = 0")
                else:
                    self._add_line(f"try:")
                    self._add_line(f"    {var_name} = float(input_values[{i}].strip())")
                    self._add_line("except ValueError:")
                    self._add_line(f"    {var_name} = 0.0")
                
                self.indent_level -= 1
        else:
            # Если переменная одна, присваиваем напрямую
            var = input_node.variables[0]
            var_name = self._format_variable_name(var)
            
            # Преобразуем значение в зависимости от типа переменной
            if var.type_suffix == '$':
                self._add_line(f"{var_name} = BasicString(input_value)")
            elif var.type_suffix == '%':
                self._add_line(f"try:")
                self._add_line(f"    {var_name} = int(float(input_value))")
                self._add_line("except ValueError:")
                self._add_line(f"    {var_name} = 0")
            else:
                self._add_line(f"try:")
                self._add_line(f"    {var_name} = float(input_value)")
                self._add_line("except ValueError:")
                self._add_line(f"    {var_name} = 0.0")
    
    def _generate_end(self, end_node):
        """Генерирует код для инструкции END"""
        self._add_line("# END программы")
        self._add_line("sys.exit(0)")
    
    def _generate_label(self, label_node):
        """Генерирует код для метки"""
        label_name = label_node.name
        function_name = self.labels.get(label_name)
        
        # Если текущий уровень отступа > 0, то функция закрывается
        while self.indent_level > 1:
            self.indent_level -= 1
            
            # Если мы внутри GOSUB, закрываем функцию возврата
            if self.gosub_calls and self.indent_level == 1:
                self.gosub_calls.pop()
        
        # Генерируем метку как функцию для GOTO/GOSUB
        self._add_line("")
        self._add_line(f"def {function_name}():")
        self.indent_level = 2
        self._add_line(f"# Метка {label_name}")
    
    def _generate_expression(self, expr_node):
        """Генерирует код для выражения"""
        if isinstance(expr_node, NumberNode):
            return str(expr_node.value)
        
        elif isinstance(expr_node, StringNode):
            # Экранируем кавычки
            escaped_value = expr_node.value.replace('"', '\\"')
            return f'BasicString("{escaped_value}")'
        
        elif isinstance(expr_node, VariableNode):
            return self._format_variable_name(expr_node)
        
        elif isinstance(expr_node, BinaryOpNode):
            left = self._generate_expression(expr_node.left)
            right = self._generate_expression(expr_node.right)
            
            # Преобразуем операторы BASIC в операторы Python
            op = expr_node.op
            if op == '=':
                op = '=='  # В BASIC = используется для сравнения, а не для присваивания
            elif op == '<>':
                op = '!='
            
            return f"({left} {op} {right})"
        
        elif isinstance(expr_node, UnaryOpNode):
            operand = self._generate_expression(expr_node.operand)
            return f"{expr_node.op}{operand}"
        
        else:
            raise ValueError(f"Неизвестный тип узла выражения: {type(expr_node)}")
    
    def _format_variable_name(self, var_node):
        """Форматирует имя переменной для Python кода"""
        name = var_node.name
        suffix = var_node.type_suffix or ""
        
        # Используем суффикс как часть имени переменной
        if suffix:
            return f"{name}_{suffix.replace('$', 'S').replace('%', 'I').replace('!', 'F')}"
        else:
            return name 