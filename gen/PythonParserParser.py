# Generated from PythonParser.g4 by ANTLR 4.13.2
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
        4,1,23,193,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,3,1,31,8,1,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,2,1,2,1,2,
        3,2,42,8,2,1,3,1,3,1,3,1,3,5,3,48,8,3,10,3,12,3,51,9,3,1,3,1,3,5,
        3,55,8,3,10,3,12,3,58,9,3,1,3,4,3,61,8,3,11,3,12,3,62,1,3,5,3,66,
        8,3,10,3,12,3,69,9,3,1,3,3,3,72,8,3,1,4,5,4,75,8,4,10,4,12,4,78,
        9,4,1,4,1,4,1,4,1,4,5,4,84,8,4,10,4,12,4,87,9,4,1,4,1,4,5,4,91,8,
        4,10,4,12,4,94,9,4,1,4,4,4,97,8,4,11,4,12,4,98,1,5,5,5,102,8,5,10,
        5,12,5,105,9,5,1,5,1,5,1,5,5,5,110,8,5,10,5,12,5,113,9,5,1,5,4,5,
        116,8,5,11,5,12,5,117,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,129,
        8,6,1,6,1,6,5,6,133,8,6,10,6,12,6,136,9,6,1,6,4,6,139,8,6,11,6,12,
        6,140,1,7,1,7,1,7,1,7,5,7,147,8,7,10,7,12,7,150,9,7,1,7,1,7,5,7,
        154,8,7,10,7,12,7,157,9,7,1,7,4,7,160,8,7,11,7,12,7,161,1,8,1,8,
        3,8,166,8,8,1,8,1,8,1,8,3,8,171,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        3,8,180,8,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,188,8,9,10,9,12,9,191,9,
        9,1,9,0,1,18,10,0,2,4,6,8,10,12,14,16,18,0,2,1,0,13,14,1,0,15,19,
        211,0,23,1,0,0,0,2,30,1,0,0,0,4,35,1,0,0,0,6,43,1,0,0,0,8,76,1,0,
        0,0,10,103,1,0,0,0,12,119,1,0,0,0,14,142,1,0,0,0,16,179,1,0,0,0,
        18,181,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,
        0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,0,0,1,27,
        1,1,0,0,0,28,31,3,16,8,0,29,31,3,4,2,0,30,28,1,0,0,0,30,29,1,0,0,
        0,31,3,1,0,0,0,32,34,5,21,0,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,
        1,0,0,0,35,36,1,0,0,0,36,41,1,0,0,0,37,35,1,0,0,0,38,42,3,6,3,0,
        39,42,3,14,7,0,40,42,3,12,6,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,
        1,0,0,0,42,5,1,0,0,0,43,44,5,1,0,0,44,49,3,16,8,0,45,46,5,14,0,0,
        46,48,3,16,8,0,47,45,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,
        0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,60,5,2,0,0,53,55,5,21,0,0,54,
        53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,
        0,58,56,1,0,0,0,59,61,3,2,1,0,60,56,1,0,0,0,61,62,1,0,0,0,62,60,
        1,0,0,0,62,63,1,0,0,0,63,67,1,0,0,0,64,66,3,8,4,0,65,64,1,0,0,0,
        66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,71,1,0,0,0,69,67,1,
        0,0,0,70,72,3,10,5,0,71,70,1,0,0,0,71,72,1,0,0,0,72,7,1,0,0,0,73,
        75,5,21,0,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,
        0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,3,0,0,80,85,3,16,8,0,81,
        82,5,14,0,0,82,84,3,16,8,0,83,81,1,0,0,0,84,87,1,0,0,0,85,83,1,0,
        0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,96,5,2,0,0,89,91,
        5,21,0,0,90,89,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,
        93,95,1,0,0,0,94,92,1,0,0,0,95,97,3,2,1,0,96,92,1,0,0,0,97,98,1,
        0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,9,1,0,0,0,100,102,5,21,0,0,
        101,100,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,
        104,106,1,0,0,0,105,103,1,0,0,0,106,107,5,4,0,0,107,115,5,2,0,0,
        108,110,5,21,0,0,109,108,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,
        111,112,1,0,0,0,112,114,1,0,0,0,113,111,1,0,0,0,114,116,3,2,1,0,
        115,111,1,0,0,0,116,117,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,
        118,11,1,0,0,0,119,120,5,5,0,0,120,121,5,16,0,0,121,128,5,6,0,0,
        122,129,5,16,0,0,123,124,5,7,0,0,124,125,5,17,0,0,125,126,5,8,0,
        0,126,127,5,17,0,0,127,129,5,9,0,0,128,122,1,0,0,0,128,123,1,0,0,
        0,129,130,1,0,0,0,130,138,5,2,0,0,131,133,5,21,0,0,132,131,1,0,0,
        0,133,136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,
        0,136,134,1,0,0,0,137,139,3,2,1,0,138,134,1,0,0,0,139,140,1,0,0,
        0,140,138,1,0,0,0,140,141,1,0,0,0,141,13,1,0,0,0,142,143,5,10,0,
        0,143,148,3,16,8,0,144,145,5,14,0,0,145,147,3,16,8,0,146,144,1,0,
        0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,151,1,0,
        0,0,150,148,1,0,0,0,151,159,5,2,0,0,152,154,5,21,0,0,153,152,1,0,
        0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,158,1,0,
        0,0,157,155,1,0,0,0,158,160,3,2,1,0,159,155,1,0,0,0,160,161,1,0,
        0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,15,1,0,0,0,163,166,3,18,
        9,0,164,166,5,16,0,0,165,163,1,0,0,0,165,164,1,0,0,0,166,167,1,0,
        0,0,167,170,7,0,0,0,168,171,3,18,9,0,169,171,5,16,0,0,170,168,1,
        0,0,0,170,169,1,0,0,0,171,180,1,0,0,0,172,173,5,14,0,0,173,180,5,
        16,0,0,174,180,5,15,0,0,175,176,5,11,0,0,176,177,3,16,8,0,177,178,
        5,9,0,0,178,180,1,0,0,0,179,165,1,0,0,0,179,172,1,0,0,0,179,174,
        1,0,0,0,179,175,1,0,0,0,180,17,1,0,0,0,181,182,6,9,-1,0,182,183,
        7,1,0,0,183,189,1,0,0,0,184,185,10,2,0,0,185,186,5,12,0,0,186,188,
        3,18,9,3,187,184,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,
        1,0,0,0,190,19,1,0,0,0,191,189,1,0,0,0,26,23,30,35,41,49,56,62,67,
        71,76,85,92,98,103,111,117,128,134,140,148,155,161,165,170,179,189
    ]

class PythonParserParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "':'", "'elif'", "'else'", "'for'", 
                     "'in'", "'range('", "','", "')'", "'while'", "'('", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\t'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ARITH_OP", "ASSGN_OP", "COND_OP", "BOOL", "VAR", 
                      "NUMBER", "STRING", "ARRAY", "COMMENT", "INDENT", 
                      "NEWLINE", "WS" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_indentStatement = 2
    RULE_ifStatement = 3
    RULE_elif = 4
    RULE_else = 5
    RULE_forStatement = 6
    RULE_whileStatement = 7
    RULE_expression = 8
    RULE_arithmatic = 9

    ruleNames =  [ "start", "statement", "indentStatement", "ifStatement", 
                   "elif", "else", "forStatement", "whileStatement", "expression", 
                   "arithmatic" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    ARITH_OP=12
    ASSGN_OP=13
    COND_OP=14
    BOOL=15
    VAR=16
    NUMBER=17
    STRING=18
    ARRAY=19
    COMMENT=20
    INDENT=21
    NEWLINE=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PythonParserParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.StatementContext,i)


        def getRuleIndex(self):
            return PythonParserParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = PythonParserParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3132450) != 0):
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(PythonParserParser.EOF)
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

        def expression(self):
            return self.getTypedRuleContext(PythonParserParser.ExpressionContext,0)


        def indentStatement(self):
            return self.getTypedRuleContext(PythonParserParser.IndentStatementContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PythonParserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 14, 15, 16, 17, 18, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.expression()
                pass
            elif token in [1, 5, 10, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.indentStatement()
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


    class IndentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(PythonParserParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(PythonParserParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(PythonParserParser.ForStatementContext,0)


        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.INDENT)
            else:
                return self.getToken(PythonParserParser.INDENT, i)

        def getRuleIndex(self):
            return PythonParserParser.RULE_indentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndentStatement" ):
                listener.enterIndentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndentStatement" ):
                listener.exitIndentStatement(self)




    def indentStatement(self):

        localctx = PythonParserParser.IndentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_indentStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 32
                self.match(PythonParserParser.INDENT)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 38
                self.ifStatement()
                pass
            elif token in [10]:
                self.state = 39
                self.whileStatement()
                pass
            elif token in [5]:
                self.state = 40
                self.forStatement()
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


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ExpressionContext,i)


        def COND_OP(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.COND_OP)
            else:
                return self.getToken(PythonParserParser.COND_OP, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.StatementContext,i)


        def elif_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ElifContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ElifContext,i)


        def else_(self):
            return self.getTypedRuleContext(PythonParserParser.ElseContext,0)


        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.INDENT)
            else:
                return self.getToken(PythonParserParser.INDENT, i)

        def getRuleIndex(self):
            return PythonParserParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = PythonParserParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(PythonParserParser.T__0)
            self.state = 44
            self.expression()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 45
                self.match(PythonParserParser.COND_OP)
                self.state = 46
                self.expression()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(PythonParserParser.T__1)
            self.state = 60 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 56
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 53
                            self.match(PythonParserParser.INDENT) 
                        self.state = 58
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                    self.state = 59
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 62 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 64
                    self.elif_() 
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 70
                self.else_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ExpressionContext,i)


        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.INDENT)
            else:
                return self.getToken(PythonParserParser.INDENT, i)

        def COND_OP(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.COND_OP)
            else:
                return self.getToken(PythonParserParser.COND_OP, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.StatementContext,i)


        def getRuleIndex(self):
            return PythonParserParser.RULE_elif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif" ):
                listener.enterElif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif" ):
                listener.exitElif(self)




    def elif_(self):

        localctx = PythonParserParser.ElifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_elif)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 73
                self.match(PythonParserParser.INDENT)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(PythonParserParser.T__2)
            self.state = 80
            self.expression()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 81
                self.match(PythonParserParser.COND_OP)
                self.state = 82
                self.expression()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(PythonParserParser.T__1)
            self.state = 96 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 92
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 89
                            self.match(PythonParserParser.INDENT) 
                        self.state = 94
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                    self.state = 95
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 98 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.INDENT)
            else:
                return self.getToken(PythonParserParser.INDENT, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.StatementContext,i)


        def getRuleIndex(self):
            return PythonParserParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)




    def else_(self):

        localctx = PythonParserParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 100
                self.match(PythonParserParser.INDENT)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(PythonParserParser.T__3)
            self.state = 107
            self.match(PythonParserParser.T__1)
            self.state = 115 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 111
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 108
                            self.match(PythonParserParser.INDENT) 
                        self.state = 113
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                    self.state = 114
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 117 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.VAR)
            else:
                return self.getToken(PythonParserParser.VAR, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.StatementContext,i)


        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.NUMBER)
            else:
                return self.getToken(PythonParserParser.NUMBER, i)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.INDENT)
            else:
                return self.getToken(PythonParserParser.INDENT, i)

        def getRuleIndex(self):
            return PythonParserParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = PythonParserParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(PythonParserParser.T__4)
            self.state = 120
            self.match(PythonParserParser.VAR)
            self.state = 121
            self.match(PythonParserParser.T__5)
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 122
                self.match(PythonParserParser.VAR)
                pass
            elif token in [7]:
                self.state = 123
                self.match(PythonParserParser.T__6)
                self.state = 124
                self.match(PythonParserParser.NUMBER)
                self.state = 125
                self.match(PythonParserParser.T__7)
                self.state = 126
                self.match(PythonParserParser.NUMBER)
                self.state = 127
                self.match(PythonParserParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 130
            self.match(PythonParserParser.T__1)
            self.state = 138 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 134
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 131
                            self.match(PythonParserParser.INDENT) 
                        self.state = 136
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                    self.state = 137
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 140 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ExpressionContext,i)


        def COND_OP(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.COND_OP)
            else:
                return self.getToken(PythonParserParser.COND_OP, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.StatementContext,i)


        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.INDENT)
            else:
                return self.getToken(PythonParserParser.INDENT, i)

        def getRuleIndex(self):
            return PythonParserParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = PythonParserParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(PythonParserParser.T__9)
            self.state = 143
            self.expression()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 144
                self.match(PythonParserParser.COND_OP)
                self.state = 145
                self.expression()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(PythonParserParser.T__1)
            self.state = 159 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 155
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 152
                            self.match(PythonParserParser.INDENT) 
                        self.state = 157
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                    self.state = 158
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 161 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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

        def ASSGN_OP(self):
            return self.getToken(PythonParserParser.ASSGN_OP, 0)

        def COND_OP(self):
            return self.getToken(PythonParserParser.COND_OP, 0)

        def arithmatic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ArithmaticContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ArithmaticContext,i)


        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.VAR)
            else:
                return self.getToken(PythonParserParser.VAR, i)

        def BOOL(self):
            return self.getToken(PythonParserParser.BOOL, 0)

        def expression(self):
            return self.getTypedRuleContext(PythonParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = PythonParserParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 163
                    self.arithmatic(0)
                    pass

                elif la_ == 2:
                    self.state = 164
                    self.match(PythonParserParser.VAR)
                    pass


                self.state = 167
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 170
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 168
                    self.arithmatic(0)
                    pass

                elif la_ == 2:
                    self.state = 169
                    self.match(PythonParserParser.VAR)
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(PythonParserParser.COND_OP)
                self.state = 173
                self.match(PythonParserParser.VAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.match(PythonParserParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.match(PythonParserParser.T__10)
                self.state = 176
                self.expression()
                self.state = 177
                self.match(PythonParserParser.T__8)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmaticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(PythonParserParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(PythonParserParser.STRING, 0)

        def ARRAY(self):
            return self.getToken(PythonParserParser.ARRAY, 0)

        def BOOL(self):
            return self.getToken(PythonParserParser.BOOL, 0)

        def VAR(self):
            return self.getToken(PythonParserParser.VAR, 0)

        def arithmatic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ArithmaticContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ArithmaticContext,i)


        def ARITH_OP(self):
            return self.getToken(PythonParserParser.ARITH_OP, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_arithmatic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmatic" ):
                listener.enterArithmatic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmatic" ):
                listener.exitArithmatic(self)



    def arithmatic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParserParser.ArithmaticContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_arithmatic, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1015808) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonParserParser.ArithmaticContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmatic)
                    self.state = 184
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 185
                    self.match(PythonParserParser.ARITH_OP)
                    self.state = 186
                    self.arithmatic(3) 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.arithmatic_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmatic_sempred(self, localctx:ArithmaticContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




