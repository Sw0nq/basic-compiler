# Generated from C:/Users/danil/PycharmProjects/basic-compiler/grammar/Basic.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BasicParser import BasicParser
else:
    from BasicParser import BasicParser

# This class defines a complete listener for a parse tree produced by BasicParser.
class BasicListener(ParseTreeListener):

    # Enter a parse tree produced by BasicParser#program.
    def enterProgram(self, ctx:BasicParser.ProgramContext):
        pass

    # Exit a parse tree produced by BasicParser#program.
    def exitProgram(self, ctx:BasicParser.ProgramContext):
        pass


    # Enter a parse tree produced by BasicParser#lineContent.
    def enterLineContent(self, ctx:BasicParser.LineContentContext):
        pass

    # Exit a parse tree produced by BasicParser#lineContent.
    def exitLineContent(self, ctx:BasicParser.LineContentContext):
        pass


    # Enter a parse tree produced by BasicParser#labelDef.
    def enterLabelDef(self, ctx:BasicParser.LabelDefContext):
        pass

    # Exit a parse tree produced by BasicParser#labelDef.
    def exitLabelDef(self, ctx:BasicParser.LabelDefContext):
        pass


    # Enter a parse tree produced by BasicParser#statement.
    def enterStatement(self, ctx:BasicParser.StatementContext):
        pass

    # Exit a parse tree produced by BasicParser#statement.
    def exitStatement(self, ctx:BasicParser.StatementContext):
        pass


    # Enter a parse tree produced by BasicParser#printStmt.
    def enterPrintStmt(self, ctx:BasicParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#printStmt.
    def exitPrintStmt(self, ctx:BasicParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#expressionList.
    def enterExpressionList(self, ctx:BasicParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by BasicParser#expressionList.
    def exitExpressionList(self, ctx:BasicParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by BasicParser#letStmt.
    def enterLetStmt(self, ctx:BasicParser.LetStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#letStmt.
    def exitLetStmt(self, ctx:BasicParser.LetStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#ifStmt.
    def enterIfStmt(self, ctx:BasicParser.IfStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#ifStmt.
    def exitIfStmt(self, ctx:BasicParser.IfStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#gotoStmt.
    def enterGotoStmt(self, ctx:BasicParser.GotoStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#gotoStmt.
    def exitGotoStmt(self, ctx:BasicParser.GotoStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#forStmt.
    def enterForStmt(self, ctx:BasicParser.ForStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#forStmt.
    def exitForStmt(self, ctx:BasicParser.ForStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#nextStmt.
    def enterNextStmt(self, ctx:BasicParser.NextStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#nextStmt.
    def exitNextStmt(self, ctx:BasicParser.NextStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#gosubStmt.
    def enterGosubStmt(self, ctx:BasicParser.GosubStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#gosubStmt.
    def exitGosubStmt(self, ctx:BasicParser.GosubStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#returnStmt.
    def enterReturnStmt(self, ctx:BasicParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#returnStmt.
    def exitReturnStmt(self, ctx:BasicParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#whileStmt.
    def enterWhileStmt(self, ctx:BasicParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#whileStmt.
    def exitWhileStmt(self, ctx:BasicParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#inputStmt.
    def enterInputStmt(self, ctx:BasicParser.InputStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#inputStmt.
    def exitInputStmt(self, ctx:BasicParser.InputStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#targetLabel.
    def enterTargetLabel(self, ctx:BasicParser.TargetLabelContext):
        pass

    # Exit a parse tree produced by BasicParser#targetLabel.
    def exitTargetLabel(self, ctx:BasicParser.TargetLabelContext):
        pass


    # Enter a parse tree produced by BasicParser#endStmt.
    def enterEndStmt(self, ctx:BasicParser.EndStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#endStmt.
    def exitEndStmt(self, ctx:BasicParser.EndStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#variable.
    def enterVariable(self, ctx:BasicParser.VariableContext):
        pass

    # Exit a parse tree produced by BasicParser#variable.
    def exitVariable(self, ctx:BasicParser.VariableContext):
        pass


    # Enter a parse tree produced by BasicParser#condition.
    def enterCondition(self, ctx:BasicParser.ConditionContext):
        pass

    # Exit a parse tree produced by BasicParser#condition.
    def exitCondition(self, ctx:BasicParser.ConditionContext):
        pass


    # Enter a parse tree produced by BasicParser#expression.
    def enterExpression(self, ctx:BasicParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BasicParser#expression.
    def exitExpression(self, ctx:BasicParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BasicParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:BasicParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by BasicParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:BasicParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by BasicParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:BasicParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by BasicParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:BasicParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by BasicParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:BasicParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by BasicParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:BasicParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by BasicParser#unaryExpr.
    def enterUnaryExpr(self, ctx:BasicParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by BasicParser#unaryExpr.
    def exitUnaryExpr(self, ctx:BasicParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by BasicParser#atom.
    def enterAtom(self, ctx:BasicParser.AtomContext):
        pass

    # Exit a parse tree produced by BasicParser#atom.
    def exitAtom(self, ctx:BasicParser.AtomContext):
        pass



del BasicParser