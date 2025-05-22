from generated.BasicParser import BasicParser
from generated.BasicVisitor import BasicVisitor
from ast_nodes import (
    ProgramNode, PrintNode, LetNode, EndNode, IfNode, GotoNode, LabelReferenceNode,
    ForNode, NextNode, GosubNode, ReturnNode, WhileNode, InputNode,
    NumberNode, StringNode, VariableNode, BinaryOpNode, UnaryOpNode, LabelNode
)


class AstBuilder(BasicVisitor):
    def visitProgram(self, ctx: BasicParser.ProgramContext):
        statements = []
        for lc_node_ctx in ctx.lineContent():  # Обходим все lineContent
            stmt_node = self.visit(lc_node_ctx)
            if stmt_node:
                statements.append(stmt_node)
        return ProgramNode(statements)

    def visitLineContent(self, ctx: BasicParser.LineContentContext):
        if ctx.labelDef():
            return LabelNode(ctx.labelDef().ID().getText())  # Возвращаем узел метки
        if ctx.statement():
            return self.visit(ctx.statement())
        return None

    # --- Методы для инструкций ---
    def visitPrintStmt(self, ctx: BasicParser.PrintStmtContext):
        expressions_data = []
        if ctx.expressionList():
            expr_list_ctx = ctx.expressionList()
            expressions = expr_list_ctx.expression()

            commas = [token.getText() for token in expr_list_ctx.COMMA()]
            semicolons = [token.getText() for token in expr_list_ctx.SEMICOLON()]

            for i, expr_ctx in enumerate(expressions):
                expr_node = self.visit(expr_ctx)
                separator_text = None

                if i < len(expressions) - 1:
                    expr_stop_index = expr_ctx.stop.tokenIndex

                    nearest_comma_index = None
                    nearest_semicolon_index = None

                    if i < len(commas):
                        comma_token = expr_list_ctx.COMMA(i)
                        if comma_token:
                            nearest_comma_index = comma_token.symbol.tokenIndex

                    if i < len(semicolons):
                        semicolon_token = expr_list_ctx.SEMICOLON(i)
                        if semicolon_token:
                            nearest_semicolon_index = semicolon_token.symbol.tokenIndex

                    if nearest_comma_index is not None and (
                            nearest_semicolon_index is None or nearest_comma_index < nearest_semicolon_index):
                        separator_text = ','
                    elif nearest_semicolon_index is not None:
                        separator_text = ';'

                expressions_data.append({'expression': expr_node, 'separator': separator_text})
        return PrintNode(expressions_data)

    def visitLetStmt(self, ctx: BasicParser.LetStmtContext):
        var_node = self.visit(ctx.variable())
        expr_node = self.visit(ctx.expression())
        return LetNode(var_node, expr_node)

    def visitIfStmt(self, ctx: BasicParser.IfStmtContext):
        condition_node = self.visit(ctx.condition())
        then_stmt_node = self.visit(ctx.statement(0))

        else_stmt_node = None
        if ctx.ELSE() and len(ctx.statement()) > 1:
            else_stmt_node = self.visit(ctx.statement(1))

        return IfNode(condition_node, then_stmt_node, else_stmt_node)

    def visitGotoStmt(self, ctx: BasicParser.GotoStmtContext):
        target_label = ctx.targetLabel()
        if target_label.ID():
            return GotoNode(LabelReferenceNode(target_label.ID().getText()))
        elif target_label.NUMBER():
            return GotoNode(LabelReferenceNode(int(target_label.NUMBER().getText())))
        return None

    def visitForStmt(self, ctx: BasicParser.ForStmtContext):
        loop_var_node = self.visit(ctx.variable())
        start_expr_node = self.visit(ctx.expression(0))
        end_expr_node = self.visit(ctx.expression(1))
        step_expr_node = None
        if ctx.STEP():
            if len(ctx.expression()) > 2:
                step_expr_node = self.visit(ctx.expression(2))
        return ForNode(loop_var_node, start_expr_node, end_expr_node, step_expr_node)

    def visitNextStmt(self, ctx: BasicParser.NextStmtContext):
        variables = [self.visit(var_ctx) for var_ctx in ctx.variable()]
        return NextNode(variables)

    def visitGosubStmt(self, ctx: BasicParser.GosubStmtContext):
        target_label_node = self.visit(ctx.targetLabel())
        return GosubNode(target_label_node)

    def visitReturnStmt(self, ctx: BasicParser.ReturnStmtContext):
        return ReturnNode()

    def visitWhileStmt(self, ctx: BasicParser.WhileStmtContext):
        condition_node = self.visit(ctx.condition())
        body_statements = []

        for lc_ctx in ctx.lineContent():
            stmt = self.visit(lc_ctx)
            if stmt:
                body_statements.append(stmt)

        return WhileNode(condition_node, body_statements)

    def visitInputStmt(self, ctx: BasicParser.InputStmtContext):
        prompt_node = None
        if ctx.STRING():
            text = ctx.STRING().getText()
            prompt_node = StringNode(text[1:-1])

        variables = [self.visit(var_ctx) for var_ctx in ctx.variable()]

        return InputNode(variables, prompt_node=prompt_node)

    def visitTargetLabel(self, ctx: BasicParser.TargetLabelContext):
        if ctx.ID():
            return LabelReferenceNode(ctx.ID().getText())
        elif ctx.NUMBER():
            return LabelReferenceNode(int(ctx.NUMBER().getText()))
        return None

    def visitVariable(self, ctx: BasicParser.VariableContext):
        name = ctx.ID().getText()
        type_suffix_node = ctx.TYPE_SUFFIX()
        suffix_text = type_suffix_node.getText() if type_suffix_node else None
        return VariableNode(name, suffix_text)

    def visitCondition(self, ctx: BasicParser.ConditionContext):
        return self.visit(ctx.expression())

    def visitExpression(self, ctx: BasicParser.ExpressionContext):
        return self.visit(ctx.comparisonExpr())

    def visitComparisonExpr(self, ctx: BasicParser.ComparisonExprContext):
        left_node = self.visit(ctx.left)
        if ctx.op is not None:
            op_text = ctx.op.text
            right_node = self.visit(ctx.right)
            return BinaryOpNode(left_node, op_text, right_node)
        return left_node

    def visitAdditiveExpr(self, ctx: BasicParser.AdditiveExprContext):
        left_node = self.visit(ctx.left)

        ops_list = []
        if ctx.op:
            if isinstance(ctx.op, list):
                ops_list = ctx.op
            else:
                ops_list = [ctx.op]

        rights_list = []
        if ctx.right:
            if isinstance(ctx.right, list):
                rights_list = ctx.right
            else:
                rights_list = [ctx.right]

        if len(ops_list) == len(rights_list):
            for i in range(len(ops_list)):
                op_text = ops_list[i].text
                right_node = self.visit(rights_list[i])
                left_node = BinaryOpNode(left_node, op_text, right_node)
        return left_node

    def visitMultiplicativeExpr(self, ctx: BasicParser.MultiplicativeExprContext):
        left_node = self.visit(ctx.left)

        ops_list = []
        if ctx.op:
            if isinstance(ctx.op, list):
                ops_list = ctx.op
            else:
                ops_list = [ctx.op]

        rights_list = []
        if ctx.right:
            if isinstance(ctx.right, list):
                rights_list = ctx.right
            else:
                rights_list = [ctx.right]

        if len(ops_list) == len(rights_list):
            for i in range(len(ops_list)):
                op_text = ops_list[i].text
                right_node = self.visit(rights_list[i])
                left_node = BinaryOpNode(left_node, op_text, right_node)
        return left_node

    def visitUnaryExpr(self, ctx: BasicParser.UnaryExprContext):
        if ctx.MINUS():
            operand_node = self.visit(ctx.atom())
            return UnaryOpNode(ctx.MINUS().getText(), operand_node)
        else:
            return self.visit(ctx.atom())

    def visitAtom(self, ctx: BasicParser.AtomContext):
        if ctx.NUMBER():
            return NumberNode(float(ctx.NUMBER().getText()))
        elif ctx.STRING():
            text = ctx.STRING().getText()
            return StringNode(text[1:-1])
        elif ctx.variable():
            return self.visit(ctx.variable())
        elif ctx.LPAREN():
            return self.visit(ctx.expression())
        return None
