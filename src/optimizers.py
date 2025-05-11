# Файл: BasicCompiler/src/optimizers.py

from ast_nodes import (
    ProgramNode, PrintNode, LetNode, EndNode, IfNode, GotoNode, LabelReferenceNode,
    ForNode, NextNode, GosubNode, ReturnNode, WhileNode, InputNode,
    NumberNode, StringNode, VariableNode, BinaryOpNode, UnaryOpNode, LabelNode
)

class Optimizer:
    """Базовый класс для всех оптимизаторов"""
    def optimize(self, ast_root):
        """Метод, который должны реализовать все наследники"""
        raise NotImplementedError("Метод optimize должен быть реализован в наследниках")

class ConstantFoldingOptimizer(Optimizer):
    """
    Оптимизатор для вычисления константных выражений на этапе компиляции.
    Например, выражение 2 + 3 * 4 будет заменено на 14.
    """
    def optimize(self, ast_root):
        """Оптимизирует дерево AST, заменяя константные выражения на их значения"""
        if not isinstance(ast_root, ProgramNode):
            raise ValueError("Ожидается корень AST дерева типа ProgramNode")
        
        # Список для хранения измененных инструкций
        optimized_statements = []
        
        # Проходим по всем инструкциям
        for stmt in ast_root.statements:
            optimized_stmt = self._optimize_statement(stmt)
            optimized_statements.append(optimized_stmt)
        
        # Обновляем инструкции в программе
        ast_root.statements = optimized_statements
        return ast_root
    
    def _optimize_statement(self, stmt):
        """Оптимизирует инструкцию"""
        if isinstance(stmt, LetNode):
            # Оптимизируем выражение в правой части присваивания
            value = self._optimize_expression(stmt.value)
            return LetNode(stmt.variable, value)
        
        elif isinstance(stmt, PrintNode):
            # Оптимизируем выражения в PRINT
            optimized_items = []
            for item in stmt.expressions_with_separators:
                expr = self._optimize_expression(item['expression'])
                optimized_items.append({'expression': expr, 'separator': item['separator']})
            
            # Создаем новый узел PRINT с оптимизированными выражениями
            optimized_node = PrintNode(optimized_items)
            return optimized_node
        
        elif isinstance(stmt, IfNode):
            # Оптимизируем условие
            condition = self._optimize_expression(stmt.condition)
            
            # Проверяем, можно ли предсказать результат условия на этапе компиляции
            if isinstance(condition, NumberNode):
                # Если условие всегда истинно (не равно 0)
                if condition.value != 0:
                    # Возвращаем только ветку THEN
                    return self._optimize_statement(stmt.then_branch) if stmt.then_branch else None
                # Если условие всегда ложно (равно 0)
                else:
                    # Возвращаем только ветку ELSE или ничего
                    return self._optimize_statement(stmt.else_branch) if stmt.else_branch else None
            
            # Оптимизируем ветки THEN и ELSE
            then_branch = self._optimize_statement(stmt.then_branch) if stmt.then_branch else None
            else_branch = self._optimize_statement(stmt.else_branch) if stmt.else_branch else None
            
            return IfNode(condition, then_branch, else_branch)
        
        elif isinstance(stmt, GotoNode) or isinstance(stmt, GosubNode):
            # GOTO и GOSUB не оптимизируются
            return stmt
        
        elif isinstance(stmt, ForNode):
            # Оптимизируем начальное, конечное и шаговое значения
            start_value = self._optimize_expression(stmt.start_value)
            end_value = self._optimize_expression(stmt.end_value)
            step_value = self._optimize_expression(stmt.step_value) if stmt.step_value else None
            
            return ForNode(stmt.loop_variable, start_value, end_value, step_value)
        
        elif isinstance(stmt, WhileNode):
            # Оптимизируем условие цикла
            condition = self._optimize_expression(stmt.condition)
            
            # Если условие всегда ложно, можно удалить цикл
            if isinstance(condition, NumberNode) and condition.value == 0:
                return None
            
            # Оптимизируем тело цикла
            optimized_body = []
            for body_stmt in stmt.body:
                optimized_body_stmt = self._optimize_statement(body_stmt)
                if optimized_body_stmt:
                    optimized_body.append(optimized_body_stmt)
            
            return WhileNode(condition, optimized_body)
        
        elif isinstance(stmt, InputNode):
            # INPUT не оптимизируется, но можно оптимизировать prompt, если он есть
            if stmt.prompt:
                prompt = self._optimize_expression(stmt.prompt)
                return InputNode(stmt.variables, prompt)
            return stmt
        
        # Другие инструкции не оптимизируются
        return stmt
    
    def _optimize_expression(self, expr):
        """Оптимизирует выражение"""
        # Константы (литералы) уже оптимизированы
        if isinstance(expr, NumberNode) or isinstance(expr, StringNode):
            return expr
        
        # Переменные не оптимизируются
        elif isinstance(expr, VariableNode):
            return expr
        
        # Бинарные операции
        elif isinstance(expr, BinaryOpNode):
            # Сначала оптимизируем левую и правую части
            left = self._optimize_expression(expr.left)
            right = self._optimize_expression(expr.right)
            
            # Если обе части - константы, можем вычислить результат
            if isinstance(left, NumberNode) and isinstance(right, NumberNode):
                # Вычисляем значение
                result = self._evaluate_binary_op(left.value, expr.op, right.value)
                if result is not None:
                    return NumberNode(result)
            
            # Если правая часть - NumberNode(0) и операции + или -
            if isinstance(right, NumberNode) and right.value == 0 and expr.op in ['+', '-']:
                return left
            
            # Если левая часть - NumberNode(0) и операция +
            if isinstance(left, NumberNode) and left.value == 0 and expr.op == '+':
                return right
            
            # Если правая часть - NumberNode(1) и операция *
            if isinstance(right, NumberNode) and right.value == 1 and expr.op == '*':
                return left
            
            # Если левая часть - NumberNode(1) и операция *
            if isinstance(left, NumberNode) and left.value == 1 and expr.op == '*':
                return right
            
            # Иначе возвращаем новый узел с оптимизированными частями
            return BinaryOpNode(left, expr.op, right)
        
        # Унарные операции
        elif isinstance(expr, UnaryOpNode):
            # Оптимизируем операнд
            operand = self._optimize_expression(expr.operand)
            
            # Если операнд - константа, можем вычислить результат
            if isinstance(operand, NumberNode):
                if expr.op == '-':
                    return NumberNode(-operand.value)
            
            # Иначе возвращаем новый узел с оптимизированным операндом
            return UnaryOpNode(expr.op, operand)
        
        # Другие типы выражений не поддерживаются
        return expr
    
    def _evaluate_binary_op(self, left, op, right):
        """Вычисляет значение бинарной операции"""
        try:
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right if right != 0 else None  # Избегаем деления на ноль
            elif op == '=':  # В BASIC = используется для сравнения
                return float(left == right)
            elif op == '<>':
                return float(left != right)
            elif op == '<':
                return float(left < right)
            elif op == '>':
                return float(left > right)
            elif op == '<=':
                return float(left <= right)
            elif op == '>=':
                return float(left >= right)
            else:
                return None
        except:
            return None  # Если возникли ошибки, не оптимизируем

class DeadCodeEliminationOptimizer(Optimizer):
    """
    Оптимизатор для удаления недостижимого кода.
    Например, код после инструкции GOTO или END недостижим.
    """
    def optimize(self, ast_root):
        """Оптимизирует дерево AST, удаляя недостижимый код"""
        if not isinstance(ast_root, ProgramNode):
            raise ValueError("Ожидается корень AST дерева типа ProgramNode")
        
        # Список для хранения измененных инструкций
        optimized_statements = []
        
        # Флаг, указывающий, что следующий код недостижим
        unreachable = False
        
        # Проходим по всем инструкциям
        for stmt in ast_root.statements:
            # Если код недостижим, но это метка, то код снова достижим
            if unreachable and isinstance(stmt, LabelNode):
                unreachable = False
                optimized_statements.append(stmt)
                continue
            
            # Если код недостижим, пропускаем инструкцию
            if unreachable:
                continue
            
            # Если инструкция END или неусловный GOTO, помечаем следующий код как недостижимый
            if isinstance(stmt, EndNode) or isinstance(stmt, GotoNode):
                unreachable = True
            
            # Добавляем инструкцию в оптимизированный список
            optimized_statements.append(stmt)
        
        # Обновляем инструкции в программе
        ast_root.statements = optimized_statements
        return ast_root

class UnusedLabelEliminationOptimizer(Optimizer):
    """
    Оптимизатор для удаления неиспользуемых меток.
    """
    def optimize(self, ast_root):
        """Оптимизирует дерево AST, удаляя неиспользуемые метки"""
        if not isinstance(ast_root, ProgramNode):
            raise ValueError("Ожидается корень AST дерева типа ProgramNode")
        
        # Собираем все метки и их использования
        labels = {}  # name -> LabelNode
        used_labels = set()  # Множество имен используемых меток
        
        # Проходим по всем инструкциям и собираем метки
        for stmt in ast_root.statements:
            if isinstance(stmt, LabelNode):
                labels[stmt.name] = stmt
            elif isinstance(stmt, GotoNode) or isinstance(stmt, GosubNode):
                # Добавляем имя метки в множество используемых меток
                used_labels.add(stmt.target_label_ref.name_or_number)
        
        # Список для хранения измененных инструкций
        optimized_statements = []
        
        # Проходим по всем инструкциям и удаляем неиспользуемые метки
        for stmt in ast_root.statements:
            if isinstance(stmt, LabelNode) and stmt.name not in used_labels:
                # Пропускаем неиспользуемую метку
                continue
            
            # Добавляем инструкцию в оптимизированный список
            optimized_statements.append(stmt)
        
        # Обновляем инструкции в программе
        ast_root.statements = optimized_statements
        return ast_root

class OptimizationPipeline:
    """
    Класс для последовательного применения нескольких оптимизаций.
    """
    def __init__(self, optimizers=None):
        """
        Инициализирует конвейер оптимизаций.
        
        Args:
            optimizers: Список оптимизаторов для применения.
        """
        self.optimizers = optimizers or []
    
    def add_optimizer(self, optimizer):
        """Добавляет оптимизатор в конвейер"""
        self.optimizers.append(optimizer)
    
    def optimize(self, ast_root):
        """Применяет все оптимизаторы последовательно к дереву AST"""
        for optimizer in self.optimizers:
            ast_root = optimizer.optimize(ast_root)
        return ast_root

def create_default_pipeline():
    """Создает конвейер оптимизаций с оптимизаторами по умолчанию"""
    pipeline = OptimizationPipeline()
    pipeline.add_optimizer(ConstantFoldingOptimizer())
    pipeline.add_optimizer(DeadCodeEliminationOptimizer())
    pipeline.add_optimizer(UnusedLabelEliminationOptimizer())
    return pipeline 