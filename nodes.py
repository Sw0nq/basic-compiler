class Node:
    """ Базовый класс узла AST """
    pass

class PrintNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"PrintNode(value={self.value})"

class LetNode(Node):
    def __init__(self, var_name, value):
        self.var_name = var_name
        self.value = value

    def __repr__(self):
        return f"LetNode(var_name={self.var_name}, value={self.value})"

class ConditionNode(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"ConditionNode(left={self.left}, operator={self.operator}, right={self.right})"

class IfNode(Node):
    def __init__(self, condition, then_branch):
        self.condition = condition
        self.then_branch = then_branch

    def __repr__(self):
        return f"IfNode(condition={self.condition}, then_branch={self.then_branch})"
