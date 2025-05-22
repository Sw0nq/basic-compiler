class Node:
    """
    Базовый класс для всех узлов AST.
    Предоставляет стандартный способ печати узла для отладки.
    """

    def __repr__(self):
        class_name = self.__class__.__name__
        attrs = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
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

            is_node_child = isinstance(v, Node)
            is_list_of_nodes = isinstance(v, list) and all(isinstance(item, Node) for item in v if item is not None)
            is_dict_list_of_nodes = (
                    isinstance(v, list) and
                    all(isinstance(item, dict) and 'expression' in item and isinstance(item['expression'], Node) for
                        item in v if item is not None)
            )

            if is_node_child or is_list_of_nodes or is_dict_list_of_nodes:
                children_to_display.append((k, v))
            else:
                stream.write(f"{prefix}  {k}={v!r}\n")

        for k, v_child in children_to_display:
            stream.write(f"{prefix}  {k}=(\n")
            if isinstance(v_child, list):
                if is_dict_list_of_nodes:
                    for item_dict in v_child:
                        stream.write(f"{prefix}    Item(\n")
                        item_dict['expression'].display(indent + 3, stream)
                        if item_dict.get('separator') is not None:
                            stream.write(f"{prefix}      separator='{item_dict['separator']}'\n")
                        stream.write(f"{prefix}    )\n")
                else:
                    for item_node in v_child:
                        if item_node is not None:
                            item_node.display(indent + 3, stream)
                        else:
                            stream.write(f"{prefix}    None\n")
            elif isinstance(v_child, Node):
                v_child.display(indent + 3, stream)
            stream.write(f"{prefix}  )\n")

        stream.write(f"{prefix})\n")


class ProgramNode(Node):
    def __init__(self, statements):
        self.statements = statements


class StatementNode(Node):
    pass


class PrintNode(StatementNode):
    def __init__(self, expressions_with_separators):
        self.expressions_with_separators = expressions_with_separators


class LetNode(StatementNode):
    def __init__(self, variable_node, value_expression_node):
        self.variable = variable_node
        self.value = value_expression_node


class IfNode(StatementNode):
    def __init__(self, condition_node, then_statement_node, else_statement_node=None):
        self.condition = condition_node
        self.then_branch = then_statement_node
        self.else_branch = else_statement_node


class GotoNode(StatementNode):
    def __init__(self, target_label_ref_node):
        self.target_label_ref = target_label_ref_node


class ForNode(StatementNode):
    def __init__(self, loop_variable_node, start_value_expr_node, end_value_expr_node, step_value_expr_node=None):
        self.loop_variable = loop_variable_node
        self.start_value = start_value_expr_node
        self.end_value = end_value_expr_node
        self.step_value = step_value_expr_node


class NextNode(StatementNode):
    def __init__(self, variable_nodes_list):
        self.variables = variable_nodes_list


class GosubNode(StatementNode):
    def __init__(self, target_label_ref_node):
        self.target_label_ref = target_label_ref_node


class ReturnNode(StatementNode):
    pass


class WhileNode(StatementNode):
    def __init__(self, condition_node, body_statements_list):
        self.condition = condition_node
        self.body = body_statements_list


class InputNode(StatementNode):
    def __init__(self, variable_list, prompt_node=None):
        self.prompt = prompt_node
        self.variables = variable_list


class EndNode(StatementNode):
    pass


class VariableNode(Node):
    def __init__(self, name, type_suffix=None):
        self.name = str(name)
        self.type_suffix = type_suffix


class NumberNode(Node):
    def __init__(self, value):
        self.value = float(value)


class StringNode(Node):
    def __init__(self, value):
        self.value = str(value)


class BinaryOpNode(Node):
    def __init__(self, left_operand_node, operator_text, right_operand_node):
        self.left = left_operand_node
        self.op = operator_text
        self.right = right_operand_node


class UnaryOpNode(Node):
    def __init__(self, operator_text, operand_node):
        self.op = operator_text
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