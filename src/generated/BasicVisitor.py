# Generated from C:/Users/danil/PycharmProjects/basic-compiler/grammar/Basic.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BasicParser import BasicParser
else:
    from BasicParser import BasicParser

# This class defines a complete generic visitor for a parse tree produced by BasicParser.

class BasicVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BasicParser#program.
    def visitProgram(self, ctx:BasicParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#lineContent.
    def visitLineContent(self, ctx:BasicParser.LineContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#labelDef.
    def visitLabelDef(self, ctx:BasicParser.LabelDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#statement.
    def visitStatement(self, ctx:BasicParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#printStmt.
    def visitPrintStmt(self, ctx:BasicParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#expressionList.
    def visitExpressionList(self, ctx:BasicParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#letStmt.
    def visitLetStmt(self, ctx:BasicParser.LetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#ifStmt.
    def visitIfStmt(self, ctx:BasicParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#gotoStmt.
    def visitGotoStmt(self, ctx:BasicParser.GotoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#forStmt.
    def visitForStmt(self, ctx:BasicParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#nextStmt.
    def visitNextStmt(self, ctx:BasicParser.NextStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#gosubStmt.
    def visitGosubStmt(self, ctx:BasicParser.GosubStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#returnStmt.
    def visitReturnStmt(self, ctx:BasicParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#whileStmt.
    def visitWhileStmt(self, ctx:BasicParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#inputStmt.
    def visitInputStmt(self, ctx:BasicParser.InputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#targetLabel.
    def visitTargetLabel(self, ctx:BasicParser.TargetLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#endStmt.
    def visitEndStmt(self, ctx:BasicParser.EndStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#variable.
    def visitVariable(self, ctx:BasicParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#condition.
    def visitCondition(self, ctx:BasicParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#expression.
    def visitExpression(self, ctx:BasicParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:BasicParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:BasicParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:BasicParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#unaryExpr.
    def visitUnaryExpr(self, ctx:BasicParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#atom.
    def visitAtom(self, ctx:BasicParser.AtomContext):
        return self.visitChildren(ctx)



del BasicParser