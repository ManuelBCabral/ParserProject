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
        4,1,23,200,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,3,1,29,8,1,1,1,1,1,1,1,3,1,34,8,1,3,1,36,8,1,1,2,5,2,39,8,2,10,
        2,12,2,42,9,2,1,2,1,2,1,2,1,2,5,2,48,8,2,10,2,12,2,51,9,2,1,2,1,
        2,5,2,55,8,2,10,2,12,2,58,9,2,1,2,4,2,61,8,2,11,2,12,2,62,1,2,5,
        2,66,8,2,10,2,12,2,69,9,2,1,2,3,2,72,8,2,1,3,5,3,75,8,3,10,3,12,
        3,78,9,3,1,3,1,3,1,3,1,3,5,3,84,8,3,10,3,12,3,87,9,3,1,3,1,3,5,3,
        91,8,3,10,3,12,3,94,9,3,1,3,4,3,97,8,3,11,3,12,3,98,1,4,5,4,102,
        8,4,10,4,12,4,105,9,4,1,4,1,4,1,4,5,4,110,8,4,10,4,12,4,113,9,4,
        1,4,4,4,116,8,4,11,4,12,4,117,1,5,5,5,121,8,5,10,5,12,5,124,9,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,135,8,5,1,5,1,5,1,5,4,5,
        140,8,5,11,5,12,5,141,1,6,5,6,145,8,6,10,6,12,6,148,9,6,1,6,1,6,
        1,6,1,6,5,6,154,8,6,10,6,12,6,157,9,6,1,6,1,6,5,6,161,8,6,10,6,12,
        6,164,9,6,1,6,4,6,167,8,6,11,6,12,6,168,1,7,1,7,3,7,173,8,7,1,7,
        1,7,1,7,3,7,178,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,187,8,7,1,8,
        1,8,1,8,1,8,1,8,1,8,5,8,195,8,8,10,8,12,8,198,9,8,1,8,0,1,16,9,0,
        2,4,6,8,10,12,14,16,0,2,1,0,13,14,1,0,15,19,221,0,21,1,0,0,0,2,35,
        1,0,0,0,4,40,1,0,0,0,6,76,1,0,0,0,8,103,1,0,0,0,10,122,1,0,0,0,12,
        146,1,0,0,0,14,186,1,0,0,0,16,188,1,0,0,0,18,20,3,2,1,0,19,18,1,
        0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,
        21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,29,3,14,7,0,27,29,5,20,
        0,0,28,26,1,0,0,0,28,27,1,0,0,0,29,36,1,0,0,0,30,34,3,4,2,0,31,34,
        3,12,6,0,32,34,3,10,5,0,33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,0,
        0,34,36,1,0,0,0,35,28,1,0,0,0,35,33,1,0,0,0,36,3,1,0,0,0,37,39,5,
        21,0,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,
        43,1,0,0,0,42,40,1,0,0,0,43,44,5,1,0,0,44,49,3,14,7,0,45,46,5,14,
        0,0,46,48,3,14,7,0,47,45,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,
        50,1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,60,5,2,0,0,53,55,5,21,
        0,0,54,53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,
        1,0,0,0,58,56,1,0,0,0,59,61,3,2,1,0,60,56,1,0,0,0,61,62,1,0,0,0,
        62,60,1,0,0,0,62,63,1,0,0,0,63,67,1,0,0,0,64,66,3,6,3,0,65,64,1,
        0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,71,1,0,0,0,69,
        67,1,0,0,0,70,72,3,8,4,0,71,70,1,0,0,0,71,72,1,0,0,0,72,5,1,0,0,
        0,73,75,5,21,0,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,
        1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,3,0,0,80,85,3,14,7,0,
        81,82,5,14,0,0,82,84,3,14,7,0,83,81,1,0,0,0,84,87,1,0,0,0,85,83,
        1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,96,5,2,0,0,
        89,91,5,21,0,0,90,89,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,
        0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,95,97,3,2,1,0,96,92,1,0,0,0,97,
        98,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,7,1,0,0,0,100,102,5,21,
        0,0,101,100,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,
        0,0,104,106,1,0,0,0,105,103,1,0,0,0,106,107,5,4,0,0,107,115,5,2,
        0,0,108,110,5,21,0,0,109,108,1,0,0,0,110,113,1,0,0,0,111,109,1,0,
        0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,111,1,0,0,0,114,116,3,2,
        1,0,115,111,1,0,0,0,116,117,1,0,0,0,117,115,1,0,0,0,117,118,1,0,
        0,0,118,9,1,0,0,0,119,121,5,21,0,0,120,119,1,0,0,0,121,124,1,0,0,
        0,122,120,1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,122,1,0,0,
        0,125,126,5,5,0,0,126,127,5,16,0,0,127,134,5,6,0,0,128,135,5,16,
        0,0,129,130,5,7,0,0,130,131,5,17,0,0,131,132,5,8,0,0,132,133,5,17,
        0,0,133,135,5,9,0,0,134,128,1,0,0,0,134,129,1,0,0,0,135,136,1,0,
        0,0,136,139,5,2,0,0,137,138,5,21,0,0,138,140,3,2,1,0,139,137,1,0,
        0,0,140,141,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,11,1,0,0,
        0,143,145,5,21,0,0,144,143,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,
        0,146,147,1,0,0,0,147,149,1,0,0,0,148,146,1,0,0,0,149,150,5,10,0,
        0,150,155,3,14,7,0,151,152,5,14,0,0,152,154,3,14,7,0,153,151,1,0,
        0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,158,1,0,
        0,0,157,155,1,0,0,0,158,166,5,2,0,0,159,161,5,21,0,0,160,159,1,0,
        0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,165,1,0,
        0,0,164,162,1,0,0,0,165,167,3,2,1,0,166,162,1,0,0,0,167,168,1,0,
        0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,13,1,0,0,0,170,173,3,16,
        8,0,171,173,5,16,0,0,172,170,1,0,0,0,172,171,1,0,0,0,173,174,1,0,
        0,0,174,177,7,0,0,0,175,178,3,16,8,0,176,178,5,16,0,0,177,175,1,
        0,0,0,177,176,1,0,0,0,178,187,1,0,0,0,179,180,5,14,0,0,180,187,5,
        16,0,0,181,187,5,15,0,0,182,183,5,11,0,0,183,184,3,14,7,0,184,185,
        5,9,0,0,185,187,1,0,0,0,186,172,1,0,0,0,186,179,1,0,0,0,186,181,
        1,0,0,0,186,182,1,0,0,0,187,15,1,0,0,0,188,189,6,8,-1,0,189,190,
        7,1,0,0,190,196,1,0,0,0,191,192,10,2,0,0,192,193,5,12,0,0,193,195,
        3,16,8,3,194,191,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,
        1,0,0,0,197,17,1,0,0,0,198,196,1,0,0,0,28,21,28,33,35,40,49,56,62,
        67,71,76,85,92,98,103,111,117,122,134,141,146,155,162,168,172,177,
        186,196
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
    RULE_ifStatement = 2
    RULE_elif = 3
    RULE_else = 4
    RULE_forStatement = 5
    RULE_whileStatement = 6
    RULE_expression = 7
    RULE_arithmatic = 8

    ruleNames =  [ "start", "statement", "ifStatement", "elif", "else", 
                   "forStatement", "whileStatement", "expression", "arithmatic" ]

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
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4181026) != 0):
                self.state = 18
                self.statement()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
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


        def COMMENT(self):
            return self.getToken(PythonParserParser.COMMENT, 0)

        def ifStatement(self):
            return self.getTypedRuleContext(PythonParserParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(PythonParserParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(PythonParserParser.ForStatementContext,0)


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
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 14, 15, 16, 17, 18, 19, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 14, 15, 16, 17, 18, 19]:
                    self.state = 26
                    self.expression()
                    pass
                elif token in [20]:
                    self.state = 27
                    self.match(PythonParserParser.COMMENT)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [1, 5, 10, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.ifStatement()
                    pass

                elif la_ == 2:
                    self.state = 31
                    self.whileStatement()
                    pass

                elif la_ == 3:
                    self.state = 32
                    self.forStatement()
                    pass


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


        def elif_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ElifContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ElifContext,i)


        def else_(self):
            return self.getTypedRuleContext(PythonParserParser.ElseContext,0)


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
        self.enterRule(localctx, 4, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 37
                self.match(PythonParserParser.INDENT)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 53
                            self.match(PythonParserParser.INDENT) 
                        self.state = 58
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                    self.state = 59
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 62 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 64
                    self.elif_() 
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
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
        self.enterRule(localctx, 6, self.RULE_elif)
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
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 89
                            self.match(PythonParserParser.INDENT) 
                        self.state = 94
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                    self.state = 95
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 98 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 8, self.RULE_else)
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
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 108
                            self.match(PythonParserParser.INDENT) 
                        self.state = 113
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                    self.state = 114
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 117 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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


        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.NUMBER)
            else:
                return self.getToken(PythonParserParser.NUMBER, i)

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
        self.enterRule(localctx, 10, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 119
                self.match(PythonParserParser.INDENT)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self.match(PythonParserParser.T__4)
            self.state = 126
            self.match(PythonParserParser.VAR)
            self.state = 127
            self.match(PythonParserParser.T__5)
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 128
                self.match(PythonParserParser.VAR)
                pass
            elif token in [7]:
                self.state = 129
                self.match(PythonParserParser.T__6)
                self.state = 130
                self.match(PythonParserParser.NUMBER)
                self.state = 131
                self.match(PythonParserParser.T__7)
                self.state = 132
                self.match(PythonParserParser.NUMBER)
                self.state = 133
                self.match(PythonParserParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 136
            self.match(PythonParserParser.T__1)
            self.state = 139 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 137
                    self.match(PythonParserParser.INDENT)
                    self.state = 138
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 141 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            return PythonParserParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = PythonParserParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 143
                self.match(PythonParserParser.INDENT)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.match(PythonParserParser.T__9)
            self.state = 150
            self.expression()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 151
                self.match(PythonParserParser.COND_OP)
                self.state = 152
                self.expression()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
            self.match(PythonParserParser.T__1)
            self.state = 166 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 162
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 159
                            self.match(PythonParserParser.INDENT) 
                        self.state = 164
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                    self.state = 165
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 168 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 170
                    self.arithmatic(0)
                    pass

                elif la_ == 2:
                    self.state = 171
                    self.match(PythonParserParser.VAR)
                    pass


                self.state = 174
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 177
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 175
                    self.arithmatic(0)
                    pass

                elif la_ == 2:
                    self.state = 176
                    self.match(PythonParserParser.VAR)
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(PythonParserParser.COND_OP)
                self.state = 180
                self.match(PythonParserParser.VAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.match(PythonParserParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 182
                self.match(PythonParserParser.T__10)
                self.state = 183
                self.expression()
                self.state = 184
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_arithmatic, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1015808) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonParserParser.ArithmaticContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmatic)
                    self.state = 191
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 192
                    self.match(PythonParserParser.ARITH_OP)
                    self.state = 193
                    self.arithmatic(3) 
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        self._predicates[8] = self.arithmatic_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmatic_sempred(self, localctx:ArithmaticContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




