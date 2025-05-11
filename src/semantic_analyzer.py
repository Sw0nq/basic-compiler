# Файл: BasicCompiler/src/semantic_analyzer.py

from ast_nodes import (
    ProgramNode, PrintNode, LetNode, EndNode, IfNode, GotoNode, LabelReferenceNode,
    ForNode, NextNode, GosubNode, ReturnNode, WhileNode, InputNode,
    NumberNode, StringNode, VariableNode, BinaryOpNode, UnaryOpNode, LabelNode
)

class SemanticError(Exception):
    """Исключение для семантических ошибок"""
    pass

class Symbol:
    """Класс для представления символа в таблице символов"""
    def __init__(self, name, type_suffix=None, value=None, initialized=False, line_number=None):
        self.name = name
        self.type_suffix = type_suffix
        self.value = value
        self.initialized = initialized
        self.line_number = line_number  # Номер строки, где символ был объявлен
    
    def __repr__(self):
        return f"Symbol({self.name}, type={self.type_suffix}, initialized={self.initialized})"

class SymbolTable:
    """Таблица символов для хранения переменных и их типов"""
    def __init__(self):
        self.symbols = {}  # name -> Symbol
        self.labels = {}   # name -> LabelNode
    
    def add_variable(self, name, type_suffix=None, initialized=False, line_number=None):
        """Добавляет или обновляет переменную в таблице символов"""
        if name in self.symbols:
            self.symbols[name].initialized = initialized or self.symbols[name].initialized
            return self.symbols[name]
        
        symbol = Symbol(name, type_suffix, initialized=initialized, line_number=line_number)
        self.symbols[name] = symbol
        return symbol
    
    def add_label(self, label_node):
        """Добавляет метку в таблицу символов"""
        self.labels[label_node.name] = label_node
    
    def get_variable(self, name):
        """Возвращает переменную из таблицы символов или None, если не найдена"""
        return self.symbols.get(name)
    
    def get_label(self, name_or_number):
        """Возвращает метку из таблицы символов или None, если не найдена"""
        return self.labels.get(name_or_number)
    
    def __repr__(self):
        return f"SymbolTable(variables={list(self.symbols.keys())}, labels={list(self.labels.keys())})"

class TypeAnalyzer:
    """Анализатор типов выражений"""
    
    # Типы в BASIC (для суффиксов)
    STRING_TYPE = '$'  # Строковый тип (A$)
    SINGLE_TYPE = '!'  # Числа с плавающей точкой одинарной точности (A!)
    INTEGER_TYPE = '%' # Целые числа (A%)
    DEFAULT_TYPE = None  # Числа с плавающей точкой двойной точности (без суффикса)
    
    @staticmethod
    def get_expression_type(node, symbol_table):
        """Определяет тип выражения"""
        if isinstance(node, NumberNode):
            # Целое или с плавающей точкой, в зависимости от значения
            return TypeAnalyzer.INTEGER_TYPE if node.value.is_integer() else TypeAnalyzer.DEFAULT_TYPE
        
        elif isinstance(node, StringNode):
            return TypeAnalyzer.STRING_TYPE
        
        elif isinstance(node, VariableNode):
            variable = symbol_table.get_variable(node.name)
            if not variable:
                raise SemanticError(f"Использование необъявленной переменной: {node.name}")
            return variable.type_suffix
        
        elif isinstance(node, BinaryOpNode):
            left_type = TypeAnalyzer.get_expression_type(node.left, symbol_table)
            right_type = TypeAnalyzer.get_expression_type(node.right, symbol_table)
            
            # Если один из операндов строка, результат строка (для + это конкатенация)
            if left_type == TypeAnalyzer.STRING_TYPE or right_type == TypeAnalyzer.STRING_TYPE:
                if node.op == '+':
                    return TypeAnalyzer.STRING_TYPE
                else:
                    raise SemanticError(f"Недопустимая операция {node.op} для строковых операндов")
            
            # Для числовых типов, результат зависит от операции
            if node.op in ['+', '-', '*', '/']:
                # Для числовых операций
                if left_type == TypeAnalyzer.INTEGER_TYPE and right_type == TypeAnalyzer.INTEGER_TYPE:
                    return TypeAnalyzer.INTEGER_TYPE
                return TypeAnalyzer.DEFAULT_TYPE
            elif node.op in ['=', '<>', '<', '>', '<=', '>=']:
                # Для сравнений результат логический (обрабатываем как целое)
                return TypeAnalyzer.INTEGER_TYPE
            else:
                raise SemanticError(f"Неизвестный оператор: {node.op}")
        
        elif isinstance(node, UnaryOpNode):
            operand_type = TypeAnalyzer.get_expression_type(node.operand, symbol_table)
            if operand_type == TypeAnalyzer.STRING_TYPE and node.op == '-':
                raise SemanticError("Унарный минус не может быть применен к строке")
            # Унарные операции сохраняют тип операнда
            return operand_type
        
        else:
            raise SemanticError(f"Неизвестный тип узла для анализа типа: {type(node)}")

class SemanticAnalyzer:
    """Класс для семантического анализа AST дерева"""
    
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []
        # Стек для хранения контекста для циклов FOR (для проверки NEXT)
        self.for_loops_stack = []
        # Стек для хранения меток для GOSUB (для проверки RETURN)
        self.gosub_stack = []
        # Флаг для отслеживания, были ли мы внутри подпрограммы
        self.in_subroutine = False
    
    def analyze(self, ast_root):
        """Основной метод для семантического анализа AST дерева"""
        if not isinstance(ast_root, ProgramNode):
            raise SemanticError("Ожидается корень AST дерева типа ProgramNode")
        
        # Первый проход: сбор всех меток
        self._collect_labels(ast_root)
        
        # Второй проход: проверка правильности ссылок и типов
        self._analyze_statements(ast_root.statements)
        
        # Возвращаем список ошибок
        return self.errors
    
    def _collect_labels(self, program_node):
        """Собирает все метки в программе"""
        for stmt in program_node.statements:
            if isinstance(stmt, LabelNode):
                if stmt.name in self.symbol_table.labels:
                    self.errors.append(f"Дублирование метки: {stmt.name}")
                else:
                    self.symbol_table.add_label(stmt)
    
    def _analyze_statements(self, statements):
        """Анализирует последовательность инструкций"""
        for stmt in statements:
            try:
                if isinstance(stmt, LetNode):
                    self._analyze_let(stmt)
                elif isinstance(stmt, PrintNode):
                    self._analyze_print(stmt)
                elif isinstance(stmt, IfNode):
                    self._analyze_if(stmt)
                elif isinstance(stmt, GotoNode):
                    self._analyze_goto(stmt)
                elif isinstance(stmt, ForNode):
                    self._analyze_for(stmt)
                elif isinstance(stmt, NextNode):
                    self._analyze_next(stmt)
                elif isinstance(stmt, GosubNode):
                    self._analyze_gosub(stmt)
                elif isinstance(stmt, ReturnNode):
                    self._analyze_return(stmt)
                elif isinstance(stmt, WhileNode):
                    self._analyze_while(stmt)
                elif isinstance(stmt, InputNode):
                    self._analyze_input(stmt)
                elif isinstance(stmt, EndNode):
                    # END просто завершает программу, нет семантических проверок
                    pass
                elif isinstance(stmt, LabelNode):
                    # Метки уже обработаны на первом проходе
                    pass
                else:
                    self.errors.append(f"Неизвестный тип инструкции: {type(stmt)}")
            except SemanticError as e:
                self.errors.append(str(e))
    
    def _analyze_let(self, let_node):
        """Анализирует инструкцию LET"""
        variable = let_node.variable
        value = let_node.value
        
        # Проверяем, что переменная правильно определена
        self.symbol_table.add_variable(variable.name, variable.type_suffix, initialized=True)
        
        # Проверяем тип выражения
        try:
            expr_type = TypeAnalyzer.get_expression_type(value, self.symbol_table)
            var_type = variable.type_suffix
            
            # Проверка совместимости типов
            if var_type == TypeAnalyzer.STRING_TYPE and expr_type != TypeAnalyzer.STRING_TYPE:
                self.errors.append(f"Несоответствие типов: нельзя присвоить нестроковое значение строковой переменной {variable.name}$")
            elif var_type == TypeAnalyzer.INTEGER_TYPE and expr_type == TypeAnalyzer.STRING_TYPE:
                self.errors.append(f"Несоответствие типов: нельзя присвоить строковое значение числовой переменной {variable.name}%")
            
        except SemanticError as e:
            self.errors.append(str(e))
    
    def _analyze_print(self, print_node):
        """Анализирует инструкцию PRINT"""
        for item in print_node.expressions_with_separators:
            expr = item['expression']
            try:
                # Проверяем, что все выражения и их типы корректны
                TypeAnalyzer.get_expression_type(expr, self.symbol_table)
            except SemanticError as e:
                self.errors.append(str(e))
    
    def _analyze_if(self, if_node):
        """Анализирует инструкцию IF"""
        condition = if_node.condition
        try:
            # Проверяем, что условие корректно типизировано
            TypeAnalyzer.get_expression_type(condition, self.symbol_table)
            
            # Анализируем ветку THEN
            if if_node.then_branch:
                self._analyze_statements([if_node.then_branch])
            
            # Анализируем ветку ELSE, если есть
            if if_node.else_branch:
                self._analyze_statements([if_node.else_branch])
                
        except SemanticError as e:
            self.errors.append(str(e))
    
    def _analyze_goto(self, goto_node):
        """Анализирует инструкцию GOTO"""
        target_ref = goto_node.target_label_ref
        # Проверяем, что целевая метка существует
        if not self.symbol_table.get_label(target_ref.name_or_number):
            self.errors.append(f"Переход на несуществующую метку: {target_ref.name_or_number}")
    
    def _analyze_for(self, for_node):
        """Анализирует инструкцию FOR"""
        loop_var = for_node.loop_variable
        
        # Добавляем переменную цикла в таблицу символов
        self.symbol_table.add_variable(loop_var.name, loop_var.type_suffix, initialized=True)
        
        # Проверяем типы начального, конечного и шагового значений
        try:
            start_type = TypeAnalyzer.get_expression_type(for_node.start_value, self.symbol_table)
            end_type = TypeAnalyzer.get_expression_type(for_node.end_value, self.symbol_table)
            
            if start_type == TypeAnalyzer.STRING_TYPE or end_type == TypeAnalyzer.STRING_TYPE:
                self.errors.append("Начальное и конечное значения цикла FOR должны быть числами")
            
            if for_node.step_value:
                step_type = TypeAnalyzer.get_expression_type(for_node.step_value, self.symbol_table)
                if step_type == TypeAnalyzer.STRING_TYPE:
                    self.errors.append("Шаг цикла FOR должен быть числом")
        
            # Добавляем цикл в стек для проверки NEXT
            self.for_loops_stack.append(loop_var.name)
            
        except SemanticError as e:
            self.errors.append(str(e))
    
    def _analyze_next(self, next_node):
        """Анализирует инструкцию NEXT"""
        for var in next_node.variables:
            # Проверяем, что переменная объявлена
            if not self.symbol_table.get_variable(var.name):
                self.errors.append(f"Использование необъявленной переменной в NEXT: {var.name}")
            
            # Проверяем, что переменная соответствует открытому циклу FOR
            if not self.for_loops_stack or var.name != self.for_loops_stack[-1]:
                self.errors.append(f"NEXT {var.name} без соответствующего FOR")
            else:
                # Убираем переменную из стека, так как цикл закрыт
                self.for_loops_stack.pop()
    
    def _analyze_gosub(self, gosub_node):
        """Анализирует инструкцию GOSUB"""
        target_ref = gosub_node.target_label_ref
        # Проверяем, что целевая метка существует
        if not self.symbol_table.get_label(target_ref.name_or_number):
            self.errors.append(f"Вызов несуществующей подпрограммы: {target_ref.name_or_number}")
        
        # Добавляем метку в стек для проверки RETURN
        self.gosub_stack.append(target_ref.name_or_number)
        self.in_subroutine = True
    
    def _analyze_return(self, return_node):
        """Анализирует инструкцию RETURN"""
        # Проверяем, что был соответствующий GOSUB
        if not self.gosub_stack:
            self.errors.append("RETURN без соответствующего GOSUB")
        else:
            # Убираем метку из стека, так как произошел возврат
            self.gosub_stack.pop()
            if not self.gosub_stack:
                self.in_subroutine = False
    
    def _analyze_while(self, while_node):
        """Анализирует инструкцию WHILE"""
        condition = while_node.condition
        try:
            # Проверяем, что условие корректно типизировано
            TypeAnalyzer.get_expression_type(condition, self.symbol_table)
            
            # Анализируем тело цикла
            self._analyze_statements(while_node.body)
                
        except SemanticError as e:
            self.errors.append(str(e))
    
    def _analyze_input(self, input_node):
        """Анализирует инструкцию INPUT"""
        # Проверяем подсказку, если есть
        if input_node.prompt:
            try:
                prompt_type = TypeAnalyzer.get_expression_type(input_node.prompt, self.symbol_table)
                if prompt_type != TypeAnalyzer.STRING_TYPE:
                    self.errors.append("Подсказка INPUT должна быть строкой")
            except SemanticError as e:
                self.errors.append(str(e))
        
        # Добавляем переменные в таблицу символов
        for var in input_node.variables:
            self.symbol_table.add_variable(var.name, var.type_suffix, initialized=True) 