from ast_nodes import (
    ProgramNode, PrintNode, LetNode, EndNode, IfNode, GotoNode, LabelReferenceNode,
    ForNode, NextNode, GosubNode, ReturnNode, WhileNode, InputNode,
    NumberNode, StringNode, VariableNode, BinaryOpNode, UnaryOpNode, LabelNode
)

class Optimizer:
    def optimize(self, ast_root):
        raise NotImplementedError("Метод optimize должен быть реализован в наследниках")

class ConstantFoldingOptimizer(Optimizer):
    def optimize(self, ast_root):
        if not isinstance(ast_root, ProgramNode):
            raise ValueError("Ожидается корень AST дерева типа ProgramNode")

        optimized_statements = []

        for stmt in ast_root.statements:
            optimized_stmt = self._optimize_statement(stmt)
            optimized_statements.append(optimized_stmt)

        ast_root.statements = optimized_statements
        return ast_root
    
    def _optimize_statement(self, stmt):
        if isinstance(stmt, LetNode):
            value = self._optimize_expression(stmt.value)
            return LetNode(stmt.variable, value)
        
        elif isinstance(stmt, PrintNode):
            optimized_items = []
            for item in stmt.expressions_with_separators:
                expr = self._optimize_expression(item['expression'])
                optimized_items.append({'expression': expr, 'separator': item['separator']})
            optimized_node = PrintNode(optimized_items)
            return optimized_node
        
        elif isinstance(stmt, IfNode):
            condition = self._optimize_expression(stmt.condition)

            if isinstance(condition, NumberNode):
                if condition.value != 0:
                    return self._optimize_statement(stmt.then_branch) if stmt.then_branch else None
                else:
                    return self._optimize_statement(stmt.else_branch) if stmt.else_branch else None

            then_branch = self._optimize_statement(stmt.then_branch) if stmt.then_branch else None
            else_branch = self._optimize_statement(stmt.else_branch) if stmt.else_branch else None
            
            return IfNode(condition, then_branch, else_branch)
        
        elif isinstance(stmt, GotoNode) or isinstance(stmt, GosubNode):
            return stmt
        
        elif isinstance(stmt, ForNode):
            start_value = self._optimize_expression(stmt.start_value)
            end_value = self._optimize_expression(stmt.end_value)
            step_value = self._optimize_expression(stmt.step_value) if stmt.step_value else None
            
            return ForNode(stmt.loop_variable, start_value, end_value, step_value)
        
        elif isinstance(stmt, WhileNode):
            condition = self._optimize_expression(stmt.condition)

            if isinstance(condition, NumberNode) and condition.value == 0:
                return None

            optimized_body = []
            for body_stmt in stmt.body:
                optimized_body_stmt = self._optimize_statement(body_stmt)
                if optimized_body_stmt:
                    optimized_body.append(optimized_body_stmt)
            
            return WhileNode(condition, optimized_body)
        
        elif isinstance(stmt, InputNode):
            if stmt.prompt:
                prompt = self._optimize_expression(stmt.prompt)
                return InputNode(stmt.variables, prompt)
            return stmt
        return stmt
    
    def _optimize_expression(self, expr):
        if isinstance(expr, NumberNode) or isinstance(expr, StringNode):
            return expr

        elif isinstance(expr, VariableNode):
            return expr

        elif isinstance(expr, BinaryOpNode):
            left = self._optimize_expression(expr.left)
            right = self._optimize_expression(expr.right)

            if isinstance(left, NumberNode) and isinstance(right, NumberNode):
                result = self._evaluate_binary_op(left.value, expr.op, right.value)
                if result is not None:
                    return NumberNode(result)

            if isinstance(right, NumberNode) and right.value == 0 and expr.op in ['+', '-']:
                return left

            if isinstance(left, NumberNode) and left.value == 0 and expr.op == '+':
                return right

            if isinstance(right, NumberNode) and right.value == 1 and expr.op == '*':
                return left

            if isinstance(left, NumberNode) and left.value == 1 and expr.op == '*':
                return right

            return BinaryOpNode(left, expr.op, right)
        

        elif isinstance(expr, UnaryOpNode):
            operand = self._optimize_expression(expr.operand)

            if isinstance(operand, NumberNode):
                if expr.op == '-':
                    return NumberNode(-operand.value)

            return UnaryOpNode(expr.op, operand)

        return expr
    
    def _evaluate_binary_op(self, left, op, right):
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
    def optimize(self, ast_root):
        if not isinstance(ast_root, ProgramNode):
            raise ValueError("Ожидается корень AST дерева типа ProgramNode")

        optimized_statements = []

        unreachable = False

        for stmt in ast_root.statements:
            if unreachable and isinstance(stmt, LabelNode):
                unreachable = False
                optimized_statements.append(stmt)
                continue

            if unreachable:
                continue

            if isinstance(stmt, EndNode) or isinstance(stmt, GotoNode):
                unreachable = True

            optimized_statements.append(stmt)

        ast_root.statements = optimized_statements
        return ast_root

class UnusedLabelEliminationOptimizer(Optimizer):
    def optimize(self, ast_root):
        if not isinstance(ast_root, ProgramNode):
            raise ValueError("Ожидается корень AST дерева типа ProgramNode")

        labels = {}
        used_labels = set()

        for stmt in ast_root.statements:
            if isinstance(stmt, LabelNode):
                labels[stmt.name] = stmt
            elif isinstance(stmt, GotoNode) or isinstance(stmt, GosubNode):
                used_labels.add(stmt.target_label_ref.name_or_number)

        optimized_statements = []

        for stmt in ast_root.statements:
            if isinstance(stmt, LabelNode) and stmt.name not in used_labels:
                continue

            optimized_statements.append(stmt)

        ast_root.statements = optimized_statements
        return ast_root

class OptimizationPipeline:
    def __init__(self, optimizers=None):
        self.optimizers = optimizers or []
    
    def add_optimizer(self, optimizer):
        self.optimizers.append(optimizer)
    
    def optimize(self, ast_root):
        for optimizer in self.optimizers:
            ast_root = optimizer.optimize(ast_root)
        return ast_root

def create_default_pipeline():
    pipeline = OptimizationPipeline()
    pipeline.add_optimizer(ConstantFoldingOptimizer())
    pipeline.add_optimizer(DeadCodeEliminationOptimizer())
    pipeline.add_optimizer(UnusedLabelEliminationOptimizer())
    return pipeline 