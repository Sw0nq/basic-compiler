# Generated from C:/Users/danil/PycharmProjects/basic-compiler/grammar/Basic.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,40,227,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,3,0,52,8,0,1,0,
        5,0,55,8,0,10,0,12,0,58,9,0,1,0,3,0,61,8,0,1,0,1,0,1,1,1,1,3,1,67,
        8,1,1,1,3,1,70,8,1,3,1,72,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,88,8,3,1,4,1,4,3,4,92,8,4,1,5,1,5,1,5,
        5,5,97,8,5,10,5,12,5,100,9,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,3,7,109,
        8,7,1,7,1,7,3,7,113,8,7,1,7,1,7,3,7,117,8,7,1,7,1,7,1,7,3,7,122,
        8,7,1,7,3,7,125,8,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        3,9,138,8,9,1,10,1,10,1,10,1,10,5,10,144,8,10,10,10,12,10,147,9,
        10,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,3,13,157,8,13,1,13,5,
        13,160,8,13,10,13,12,13,163,9,13,1,13,1,13,1,14,1,14,1,14,3,14,170,
        8,14,1,14,1,14,1,14,5,14,175,8,14,10,14,12,14,178,9,14,1,15,1,15,
        1,16,1,16,1,17,1,17,3,17,186,8,17,1,18,1,18,1,19,1,19,1,20,1,20,
        1,20,3,20,195,8,20,1,21,1,21,1,21,5,21,200,8,21,10,21,12,21,203,
        9,21,1,22,1,22,1,22,5,22,208,8,22,10,22,12,22,211,9,22,1,23,1,23,
        1,23,3,23,216,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,225,8,
        24,1,24,0,0,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,0,5,1,0,38,39,1,0,21,22,1,0,25,30,1,0,31,32,
        1,0,33,34,238,0,56,1,0,0,0,2,71,1,0,0,0,4,73,1,0,0,0,6,87,1,0,0,
        0,8,89,1,0,0,0,10,93,1,0,0,0,12,101,1,0,0,0,14,106,1,0,0,0,16,126,
        1,0,0,0,18,129,1,0,0,0,20,139,1,0,0,0,22,148,1,0,0,0,24,151,1,0,
        0,0,26,153,1,0,0,0,28,166,1,0,0,0,30,179,1,0,0,0,32,181,1,0,0,0,
        34,183,1,0,0,0,36,187,1,0,0,0,38,189,1,0,0,0,40,191,1,0,0,0,42,196,
        1,0,0,0,44,204,1,0,0,0,46,215,1,0,0,0,48,224,1,0,0,0,50,52,3,2,1,
        0,51,50,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,55,5,1,0,0,54,51,
        1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,60,1,0,0,0,
        58,56,1,0,0,0,59,61,3,2,1,0,60,59,1,0,0,0,60,61,1,0,0,0,61,62,1,
        0,0,0,62,63,5,0,0,1,63,1,1,0,0,0,64,72,3,4,2,0,65,67,5,22,0,0,66,
        65,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,70,3,6,3,0,69,68,1,0,0,
        0,69,70,1,0,0,0,70,72,1,0,0,0,71,64,1,0,0,0,71,66,1,0,0,0,72,3,1,
        0,0,0,73,74,5,21,0,0,74,75,5,37,0,0,75,5,1,0,0,0,76,88,3,8,4,0,77,
        88,3,12,6,0,78,88,3,14,7,0,79,88,3,16,8,0,80,88,3,18,9,0,81,88,3,
        20,10,0,82,88,3,22,11,0,83,88,3,24,12,0,84,88,3,26,13,0,85,88,3,
        28,14,0,86,88,3,32,16,0,87,76,1,0,0,0,87,77,1,0,0,0,87,78,1,0,0,
        0,87,79,1,0,0,0,87,80,1,0,0,0,87,81,1,0,0,0,87,82,1,0,0,0,87,83,
        1,0,0,0,87,84,1,0,0,0,87,85,1,0,0,0,87,86,1,0,0,0,88,7,1,0,0,0,89,
        91,5,8,0,0,90,92,3,10,5,0,91,90,1,0,0,0,91,92,1,0,0,0,92,9,1,0,0,
        0,93,98,3,38,19,0,94,95,7,0,0,0,95,97,3,38,19,0,96,94,1,0,0,0,97,
        100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,11,1,0,0,0,100,98,1,0,
        0,0,101,102,5,9,0,0,102,103,3,34,17,0,103,104,5,24,0,0,104,105,3,
        38,19,0,105,13,1,0,0,0,106,108,5,5,0,0,107,109,5,2,0,0,108,107,1,
        0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,110,112,3,36,18,0,111,113,
        5,2,0,0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,116,
        5,6,0,0,115,117,5,2,0,0,116,115,1,0,0,0,116,117,1,0,0,0,117,118,
        1,0,0,0,118,124,3,6,3,0,119,121,5,7,0,0,120,122,5,2,0,0,121,120,
        1,0,0,0,121,122,1,0,0,0,122,123,1,0,0,0,123,125,3,6,3,0,124,119,
        1,0,0,0,124,125,1,0,0,0,125,15,1,0,0,0,126,127,5,11,0,0,127,128,
        3,30,15,0,128,17,1,0,0,0,129,130,5,12,0,0,130,131,3,34,17,0,131,
        132,5,24,0,0,132,133,3,38,19,0,133,134,5,13,0,0,134,137,3,38,19,
        0,135,136,5,14,0,0,136,138,3,38,19,0,137,135,1,0,0,0,137,138,1,0,
        0,0,138,19,1,0,0,0,139,140,5,15,0,0,140,145,3,34,17,0,141,142,5,
        38,0,0,142,144,3,34,17,0,143,141,1,0,0,0,144,147,1,0,0,0,145,143,
        1,0,0,0,145,146,1,0,0,0,146,21,1,0,0,0,147,145,1,0,0,0,148,149,5,
        16,0,0,149,150,3,30,15,0,150,23,1,0,0,0,151,152,5,17,0,0,152,25,
        1,0,0,0,153,154,5,18,0,0,154,161,3,36,18,0,155,157,3,2,1,0,156,155,
        1,0,0,0,156,157,1,0,0,0,157,158,1,0,0,0,158,160,5,1,0,0,159,156,
        1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,164,
        1,0,0,0,163,161,1,0,0,0,164,165,5,19,0,0,165,27,1,0,0,0,166,169,
        5,20,0,0,167,168,5,23,0,0,168,170,5,38,0,0,169,167,1,0,0,0,169,170,
        1,0,0,0,170,171,1,0,0,0,171,176,3,34,17,0,172,173,5,38,0,0,173,175,
        3,34,17,0,174,172,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,
        1,0,0,0,177,29,1,0,0,0,178,176,1,0,0,0,179,180,7,1,0,0,180,31,1,
        0,0,0,181,182,5,10,0,0,182,33,1,0,0,0,183,185,5,21,0,0,184,186,5,
        40,0,0,185,184,1,0,0,0,185,186,1,0,0,0,186,35,1,0,0,0,187,188,3,
        38,19,0,188,37,1,0,0,0,189,190,3,40,20,0,190,39,1,0,0,0,191,194,
        3,42,21,0,192,193,7,2,0,0,193,195,3,42,21,0,194,192,1,0,0,0,194,
        195,1,0,0,0,195,41,1,0,0,0,196,201,3,44,22,0,197,198,7,3,0,0,198,
        200,3,44,22,0,199,197,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,
        202,1,0,0,0,202,43,1,0,0,0,203,201,1,0,0,0,204,209,3,46,23,0,205,
        206,7,4,0,0,206,208,3,46,23,0,207,205,1,0,0,0,208,211,1,0,0,0,209,
        207,1,0,0,0,209,210,1,0,0,0,210,45,1,0,0,0,211,209,1,0,0,0,212,213,
        5,32,0,0,213,216,3,48,24,0,214,216,3,48,24,0,215,212,1,0,0,0,215,
        214,1,0,0,0,216,47,1,0,0,0,217,225,5,22,0,0,218,225,5,23,0,0,219,
        225,3,34,17,0,220,221,5,35,0,0,221,222,3,38,19,0,222,223,5,36,0,
        0,223,225,1,0,0,0,224,217,1,0,0,0,224,218,1,0,0,0,224,219,1,0,0,
        0,224,220,1,0,0,0,225,49,1,0,0,0,26,51,56,60,66,69,71,87,91,98,108,
        112,116,121,124,137,145,156,161,169,176,185,194,201,209,215,224
    ]

class BasicParser ( Parser ):

    grammarFileName = "Basic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'IF'", "'THEN'", "'ELSE'", "'PRINT'", 
                     "'LET'", "'END'", "'GOTO'", "'FOR'", "'TO'", "'STEP'", 
                     "'NEXT'", "'GOSUB'", "'RETURN'", "'WHILE'", "'WEND'", 
                     "'INPUT'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'<'", "'>'", "'<='", "'>='", "'<>'", 
                     "'+'", "'-'", "'*'", "'/'", "'('", "')'", "':'", "','", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "WS", "REM_COMMENT", "APOSTROPHE_COMMENT", 
                      "IF", "THEN", "ELSE", "PRINT", "LET", "END", "GOTO", 
                      "FOR", "TO", "STEP", "NEXT", "GOSUB", "RETURN", "WHILE", 
                      "WEND", "INPUT", "ID", "NUMBER", "STRING", "ASSIGN", 
                      "EQ", "LT", "GT", "LTE", "GTE", "NEQ", "PLUS", "MINUS", 
                      "MUL", "DIV", "LPAREN", "RPAREN", "COLON", "COMMA", 
                      "SEMICOLON", "TYPE_SUFFIX" ]

    RULE_program = 0
    RULE_lineContent = 1
    RULE_labelDef = 2
    RULE_statement = 3
    RULE_printStmt = 4
    RULE_expressionList = 5
    RULE_letStmt = 6
    RULE_ifStmt = 7
    RULE_gotoStmt = 8
    RULE_forStmt = 9
    RULE_nextStmt = 10
    RULE_gosubStmt = 11
    RULE_returnStmt = 12
    RULE_whileStmt = 13
    RULE_inputStmt = 14
    RULE_targetLabel = 15
    RULE_endStmt = 16
    RULE_variable = 17
    RULE_condition = 18
    RULE_expression = 19
    RULE_comparisonExpr = 20
    RULE_additiveExpr = 21
    RULE_multiplicativeExpr = 22
    RULE_unaryExpr = 23
    RULE_atom = 24

    ruleNames =  [ "program", "lineContent", "labelDef", "statement", "printStmt", 
                   "expressionList", "letStmt", "ifStmt", "gotoStmt", "forStmt", 
                   "nextStmt", "gosubStmt", "returnStmt", "whileStmt", "inputStmt", 
                   "targetLabel", "endStmt", "variable", "condition", "expression", 
                   "comparisonExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "atom" ]

    EOF = Token.EOF
    NEWLINE=1
    WS=2
    REM_COMMENT=3
    APOSTROPHE_COMMENT=4
    IF=5
    THEN=6
    ELSE=7
    PRINT=8
    LET=9
    END=10
    GOTO=11
    FOR=12
    TO=13
    STEP=14
    NEXT=15
    GOSUB=16
    RETURN=17
    WHILE=18
    WEND=19
    INPUT=20
    ID=21
    NUMBER=22
    STRING=23
    ASSIGN=24
    EQ=25
    LT=26
    GT=27
    LTE=28
    GTE=29
    NEQ=30
    PLUS=31
    MINUS=32
    MUL=33
    DIV=34
    LPAREN=35
    RPAREN=36
    COLON=37
    COMMA=38
    SEMICOLON=39
    TYPE_SUFFIX=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BasicParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.NEWLINE)
            else:
                return self.getToken(BasicParser.NEWLINE, i)

        def lineContent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.LineContentContext)
            else:
                return self.getTypedRuleContext(BasicParser.LineContentContext,i)


        def getRuleIndex(self):
            return BasicParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BasicParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 50
                        self.lineContent()


                    self.state = 53
                    self.match(BasicParser.NEWLINE) 
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 59
                self.lineContent()


            self.state = 62
            self.match(BasicParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labelDef(self):
            return self.getTypedRuleContext(BasicParser.LabelDefContext,0)


        def NUMBER(self):
            return self.getToken(BasicParser.NUMBER, 0)

        def statement(self):
            return self.getTypedRuleContext(BasicParser.StatementContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_lineContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLineContent" ):
                listener.enterLineContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLineContent" ):
                listener.exitLineContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineContent" ):
                return visitor.visitLineContent(self)
            else:
                return visitor.visitChildren(self)




    def lineContent(self):

        localctx = BasicParser.LineContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_lineContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 64
                self.labelDef()
                pass
            elif token in [-1, 1, 5, 8, 9, 10, 11, 12, 15, 16, 17, 18, 20, 22]:
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 65
                    self.match(BasicParser.NUMBER)


                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1548064) != 0):
                    self.state = 68
                    self.statement()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BasicParser.ID, 0)

        def COLON(self):
            return self.getToken(BasicParser.COLON, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_labelDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelDef" ):
                listener.enterLabelDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelDef" ):
                listener.exitLabelDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelDef" ):
                return visitor.visitLabelDef(self)
            else:
                return visitor.visitChildren(self)




    def labelDef(self):

        localctx = BasicParser.LabelDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_labelDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(BasicParser.ID)
            self.state = 74
            self.match(BasicParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printStmt(self):
            return self.getTypedRuleContext(BasicParser.PrintStmtContext,0)


        def letStmt(self):
            return self.getTypedRuleContext(BasicParser.LetStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(BasicParser.IfStmtContext,0)


        def gotoStmt(self):
            return self.getTypedRuleContext(BasicParser.GotoStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BasicParser.ForStmtContext,0)


        def nextStmt(self):
            return self.getTypedRuleContext(BasicParser.NextStmtContext,0)


        def gosubStmt(self):
            return self.getTypedRuleContext(BasicParser.GosubStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(BasicParser.ReturnStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(BasicParser.WhileStmtContext,0)


        def inputStmt(self):
            return self.getTypedRuleContext(BasicParser.InputStmtContext,0)


        def endStmt(self):
            return self.getTypedRuleContext(BasicParser.EndStmtContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BasicParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.printStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.letStmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.ifStmt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.gotoStmt()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.forStmt()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.nextStmt()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 7)
                self.state = 82
                self.gosubStmt()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 8)
                self.state = 83
                self.returnStmt()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 9)
                self.state = 84
                self.whileStmt()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 10)
                self.state = 85
                self.inputStmt()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 11)
                self.state = 86
                self.endStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(BasicParser.PRINT, 0)

        def expressionList(self):
            return self.getTypedRuleContext(BasicParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = BasicParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(BasicParser.PRINT)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 38669385728) != 0):
                self.state = 90
                self.expressionList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.COMMA)
            else:
                return self.getToken(BasicParser.COMMA, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.SEMICOLON)
            else:
                return self.getToken(BasicParser.SEMICOLON, i)

        def getRuleIndex(self):
            return BasicParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = BasicParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.expression()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38 or _la==39:
                self.state = 94
                _la = self._input.LA(1)
                if not(_la==38 or _la==39):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 95
                self.expression()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(BasicParser.LET, 0)

        def variable(self):
            return self.getTypedRuleContext(BasicParser.VariableContext,0)


        def ASSIGN(self):
            return self.getToken(BasicParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_letStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetStmt" ):
                listener.enterLetStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetStmt" ):
                listener.exitLetStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetStmt" ):
                return visitor.visitLetStmt(self)
            else:
                return visitor.visitChildren(self)




    def letStmt(self):

        localctx = BasicParser.LetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_letStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(BasicParser.LET)
            self.state = 102
            self.variable()
            self.state = 103
            self.match(BasicParser.ASSIGN)
            self.state = 104
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BasicParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(BasicParser.ConditionContext,0)


        def THEN(self):
            return self.getToken(BasicParser.THEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.StatementContext)
            else:
                return self.getTypedRuleContext(BasicParser.StatementContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.WS)
            else:
                return self.getToken(BasicParser.WS, i)

        def ELSE(self):
            return self.getToken(BasicParser.ELSE, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = BasicParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(BasicParser.IF)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 107
                self.match(BasicParser.WS)


            self.state = 110
            self.condition()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 111
                self.match(BasicParser.WS)


            self.state = 114
            self.match(BasicParser.THEN)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 115
                self.match(BasicParser.WS)


            self.state = 118
            self.statement()
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 119
                self.match(BasicParser.ELSE)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 120
                    self.match(BasicParser.WS)


                self.state = 123
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOTO(self):
            return self.getToken(BasicParser.GOTO, 0)

        def targetLabel(self):
            return self.getTypedRuleContext(BasicParser.TargetLabelContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_gotoStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotoStmt" ):
                listener.enterGotoStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotoStmt" ):
                listener.exitGotoStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotoStmt" ):
                return visitor.visitGotoStmt(self)
            else:
                return visitor.visitChildren(self)




    def gotoStmt(self):

        localctx = BasicParser.GotoStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_gotoStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(BasicParser.GOTO)
            self.state = 127
            self.targetLabel()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BasicParser.FOR, 0)

        def variable(self):
            return self.getTypedRuleContext(BasicParser.VariableContext,0)


        def ASSIGN(self):
            return self.getToken(BasicParser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicParser.ExpressionContext,i)


        def TO(self):
            return self.getToken(BasicParser.TO, 0)

        def STEP(self):
            return self.getToken(BasicParser.STEP, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = BasicParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(BasicParser.FOR)
            self.state = 130
            self.variable()
            self.state = 131
            self.match(BasicParser.ASSIGN)
            self.state = 132
            self.expression()
            self.state = 133
            self.match(BasicParser.TO)
            self.state = 134
            self.expression()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 135
                self.match(BasicParser.STEP)
                self.state = 136
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NextStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEXT(self):
            return self.getToken(BasicParser.NEXT, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.VariableContext)
            else:
                return self.getTypedRuleContext(BasicParser.VariableContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.COMMA)
            else:
                return self.getToken(BasicParser.COMMA, i)

        def getRuleIndex(self):
            return BasicParser.RULE_nextStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNextStmt" ):
                listener.enterNextStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNextStmt" ):
                listener.exitNextStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNextStmt" ):
                return visitor.visitNextStmt(self)
            else:
                return visitor.visitChildren(self)




    def nextStmt(self):

        localctx = BasicParser.NextStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_nextStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(BasicParser.NEXT)
            self.state = 140
            self.variable()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 141
                self.match(BasicParser.COMMA)
                self.state = 142
                self.variable()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GosubStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOSUB(self):
            return self.getToken(BasicParser.GOSUB, 0)

        def targetLabel(self):
            return self.getTypedRuleContext(BasicParser.TargetLabelContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_gosubStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGosubStmt" ):
                listener.enterGosubStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGosubStmt" ):
                listener.exitGosubStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGosubStmt" ):
                return visitor.visitGosubStmt(self)
            else:
                return visitor.visitChildren(self)




    def gosubStmt(self):

        localctx = BasicParser.GosubStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_gosubStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(BasicParser.GOSUB)
            self.state = 149
            self.targetLabel()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BasicParser.RETURN, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = BasicParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(BasicParser.RETURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BasicParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(BasicParser.ConditionContext,0)


        def WEND(self):
            return self.getToken(BasicParser.WEND, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.NEWLINE)
            else:
                return self.getToken(BasicParser.NEWLINE, i)

        def lineContent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.LineContentContext)
            else:
                return self.getTypedRuleContext(BasicParser.LineContentContext,i)


        def getRuleIndex(self):
            return BasicParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = BasicParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_whileStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(BasicParser.WHILE)
            self.state = 154
            self.condition()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7839522) != 0):
                self.state = 156
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 155
                    self.lineContent()


                self.state = 158
                self.match(BasicParser.NEWLINE)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.match(BasicParser.WEND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(BasicParser.INPUT, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.VariableContext)
            else:
                return self.getTypedRuleContext(BasicParser.VariableContext,i)


        def STRING(self):
            return self.getToken(BasicParser.STRING, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.COMMA)
            else:
                return self.getToken(BasicParser.COMMA, i)

        def getRuleIndex(self):
            return BasicParser.RULE_inputStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStmt" ):
                listener.enterInputStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStmt" ):
                listener.exitInputStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStmt" ):
                return visitor.visitInputStmt(self)
            else:
                return visitor.visitChildren(self)




    def inputStmt(self):

        localctx = BasicParser.InputStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_inputStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(BasicParser.INPUT)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 167
                self.match(BasicParser.STRING)
                self.state = 168
                self.match(BasicParser.COMMA)


            self.state = 171
            self.variable()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 172
                self.match(BasicParser.COMMA)
                self.state = 173
                self.variable()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TargetLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BasicParser.ID, 0)

        def NUMBER(self):
            return self.getToken(BasicParser.NUMBER, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_targetLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTargetLabel" ):
                listener.enterTargetLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTargetLabel" ):
                listener.exitTargetLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTargetLabel" ):
                return visitor.visitTargetLabel(self)
            else:
                return visitor.visitChildren(self)




    def targetLabel(self):

        localctx = BasicParser.TargetLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_targetLabel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(BasicParser.END, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_endStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndStmt" ):
                listener.enterEndStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndStmt" ):
                listener.exitEndStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndStmt" ):
                return visitor.visitEndStmt(self)
            else:
                return visitor.visitChildren(self)




    def endStmt(self):

        localctx = BasicParser.EndStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_endStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(BasicParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BasicParser.ID, 0)

        def TYPE_SUFFIX(self):
            return self.getToken(BasicParser.TYPE_SUFFIX, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BasicParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(BasicParser.ID)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 184
                self.match(BasicParser.TYPE_SUFFIX)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BasicParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = BasicParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonExpr(self):
            return self.getTypedRuleContext(BasicParser.ComparisonExprContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BasicParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.comparisonExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # AdditiveExprContext
            self.op = None # Token
            self.right = None # AdditiveExprContext

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(BasicParser.AdditiveExprContext,i)


        def EQ(self):
            return self.getToken(BasicParser.EQ, 0)

        def LT(self):
            return self.getToken(BasicParser.LT, 0)

        def GT(self):
            return self.getToken(BasicParser.GT, 0)

        def LTE(self):
            return self.getToken(BasicParser.LTE, 0)

        def GTE(self):
            return self.getToken(BasicParser.GTE, 0)

        def NEQ(self):
            return self.getToken(BasicParser.NEQ, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_comparisonExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpr" ):
                listener.enterComparisonExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpr" ):
                listener.exitComparisonExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)




    def comparisonExpr(self):

        localctx = BasicParser.ComparisonExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_comparisonExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            localctx.left = self.additiveExpr()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0):
                self.state = 192
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 193
                localctx.right = self.additiveExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # MultiplicativeExprContext
            self.op = None # Token
            self.right = None # MultiplicativeExprContext

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(BasicParser.MultiplicativeExprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.PLUS)
            else:
                return self.getToken(BasicParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.MINUS)
            else:
                return self.getToken(BasicParser.MINUS, i)

        def getRuleIndex(self):
            return BasicParser.RULE_additiveExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpr(self):

        localctx = BasicParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            localctx.left = self.multiplicativeExpr()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31 or _la==32:
                self.state = 197
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==31 or _la==32):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 198
                localctx.right = self.multiplicativeExpr()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # UnaryExprContext
            self.op = None # Token
            self.right = None # UnaryExprContext

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(BasicParser.UnaryExprContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.MUL)
            else:
                return self.getToken(BasicParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.DIV)
            else:
                return self.getToken(BasicParser.DIV, i)

        def getRuleIndex(self):
            return BasicParser.RULE_multiplicativeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpr(self):

        localctx = BasicParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            localctx.left = self.unaryExpr()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33 or _la==34:
                self.state = 205
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==33 or _la==34):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 206
                localctx.right = self.unaryExpr()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(BasicParser.MINUS, 0)

        def atom(self):
            return self.getTypedRuleContext(BasicParser.AtomContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = BasicParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unaryExpr)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(BasicParser.MINUS)
                self.state = 213
                self.atom()
                pass
            elif token in [21, 22, 23, 35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(BasicParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(BasicParser.STRING, 0)

        def variable(self):
            return self.getTypedRuleContext(BasicParser.VariableContext,0)


        def LPAREN(self):
            return self.getToken(BasicParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BasicParser.RPAREN, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = BasicParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_atom)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(BasicParser.NUMBER)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(BasicParser.STRING)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
                self.variable()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 4)
                self.state = 220
                self.match(BasicParser.LPAREN)
                self.state = 221
                self.expression()
                self.state = 222
                self.match(BasicParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





