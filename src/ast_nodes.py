# Файл: BasicCompiler/src/ast_nodes.py

class Node:
    """
    Базовый класс для всех узлов AST.
    Предоставляет стандартный способ печати узла для отладки.
    """
    def __repr__(self):
        # Получаем имя класса (PrintNode, LetNode и т.д.)
        class_name = self.__class__.__name__
        # Получаем все атрибуты узла (например, value у PrintNode)
        # Исключаем внутренние атрибуты или слишком большие для печати, если нужно
        attrs = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        # Формируем строку типа "PrintNode(value='Hello')"
        attrs_str = ", ".join(f"{k}={v!r}" for k, v in attrs.items())
        return f"{class_name}({attrs_str})"

    def display(self, indent=0, stream=None):
        """
        Более наглядный способ печати дерева AST с отступами.
        """
        import sys
        if stream is None:
            stream = sys.stdout
        
        prefix = "  " * indent
        stream.write(f"{prefix}{self.__class__.__name__}(\n")
        
        children_to_display = []
        for k, v in self.__dict__.items():
            if k.startswith('_'):
                continue
            
            # Собираем детей, которые являются узлами или списками узлов
            is_node_child = isinstance(v, Node)
            is_list_of_nodes = isinstance(v, list) and all(isinstance(item, Node) for item in v if item is not None)
            is_dict_list_of_nodes = (
                isinstance(v, list) and 
                all(isinstance(item, dict) and 'expression' in item and isinstance(item['expression'], Node) for item in v if item is not None)
            ) # Для PrintNode.expressions_with_separators

            if is_node_child or is_list_of_nodes or is_dict_list_of_nodes:
                children_to_display.append((k, v))
            else:
                stream.write(f"{prefix}  {k}={v!r}\n") # Печатаем простые атрибуты

        for k, v_child in children_to_display:
            stream.write(f"{prefix}  {k}=(\n")
            if isinstance(v_child, list):
                if is_dict_list_of_nodes: # Специальная обработка для PrintNode
                     for item_dict in v_child:
                        stream.write(f"{prefix}    Item(\n")
                        item_dict['expression'].display(indent + 3, stream)
                        if item_dict.get('separator') is not None:
                             stream.write(f"{prefix}      separator='{item_dict['separator']}'\n")
                        stream.write(f"{prefix}    )\n")
                else: # Список узлов
                    for item_node in v_child:
                        if item_node is not None:
                            item_node.display(indent + 3, stream)
                        else:
                            stream.write(f"{prefix}    None\n")
            elif isinstance(v_child, Node): # Один узел
                v_child.display(indent + 3, stream)
            stream.write(f"{prefix}  )\n")
            
        stream.write(f"{prefix})\n")


# --- Узлы верхнего уровня ---
class ProgramNode(Node):
    def __init__(self, statements):
        self.statements = statements # Список всех инструкций в программе

# --- Базовый узел для инструкций ---
class StatementNode(Node):
    pass

# --- Узлы для конкретных инструкций ---
class PrintNode(StatementNode):
    # expressions_with_separators: список словарей, каждый словарь:
    # {'expression': ASTNode, 'separator': строковый символ (',' или ';') или None}
    def __init__(self, expressions_with_separators):
        self.expressions_with_separators = expressions_with_separators

class LetNode(StatementNode):
    def __init__(self, variable_node, value_expression_node):
        self.variable = variable_node         # VariableNode
        self.value = value_expression_node  # Узел выражения

class IfNode(StatementNode):
    def __init__(self, condition_node, then_statement_node, else_statement_node=None):
        self.condition = condition_node
        self.then_branch = then_statement_node
        self.else_branch = else_statement_node # Может быть None

class GotoNode(StatementNode):
    def __init__(self, target_label_ref_node):
        self.target_label_ref = target_label_ref_node # LabelReferenceNode

class ForNode(StatementNode):
    def __init__(self, loop_variable_node, start_value_expr_node, end_value_expr_node, step_value_expr_node=None):
        self.loop_variable = loop_variable_node     # VariableNode
        self.start_value = start_value_expr_node
        self.end_value = end_value_expr_node
        self.step_value = step_value_expr_node      # Может быть None (тогда шаг 1)

class NextNode(StatementNode):
    def __init__(self, variable_nodes_list): # Список из VariableNode
        self.variables = variable_nodes_list

class GosubNode(StatementNode):
    def __init__(self, target_label_ref_node):
        self.target_label_ref = target_label_ref_node # LabelReferenceNode

class ReturnNode(StatementNode):
    pass # Нет атрибутов

class WhileNode(StatementNode):
    def __init__(self, condition_node, body_statements_list):
        self.condition = condition_node
        self.body = body_statements_list # Список узлов инструкций

# WendNode не нужен как отдельный узел, он закрывает блок WHILE в грамматике

class InputNode(StatementNode):
    def __init__(self, variable_list, prompt_node=None):
        self.prompt = prompt_node
        self.variables = variable_list

class EndNode(StatementNode):
    pass # Нет атрибутов

# --- Узлы для выражений и их частей ---
class VariableNode(Node):
    def __init__(self, name, type_suffix=None):
        self.name = str(name)
        self.type_suffix = type_suffix # Строка: '$', '!', '%' или None

class NumberNode(Node): # Для числовых литералов
    def __init__(self, value):
        self.value = float(value) # Храним как float для единообразия

class StringNode(Node): # Для строковых литералов
    def __init__(self, value):
        self.value = str(value) # Храним строку без внешних кавычек

class BinaryOpNode(Node): # Для бинарных операций: +, -, *, /, <, >, =, и т.д.
    def __init__(self, left_operand_node, operator_text, right_operand_node):
        self.left = left_operand_node
        self.op = operator_text # Строка, представляющая оператор: "+", ">", "EQ" и т.д.
        self.right = right_operand_node


class UnaryOpNode(Node): # Для унарных операций (например, унарный минус)
    def __init__(self, operator_text, operand_node):
        self.op = operator_text # Строка, представляющая оператор: "-"
        self.operand = operand_node


class LabelReferenceNode(Node):
    def __init__(self, name_or_number):
        self.name_or_number = name_or_number
        self.resolved = False
        self.target = None


class LabelNode(StatementNode):
    """Узел для определения метки (например, 'START:')"""
    def __init__(self, name):
        self.name = name