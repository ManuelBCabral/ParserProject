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
        4,1,23,202,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,3,1,31,8,1,3,1,33,8,1,1,2,5,2,36,8,2,10,2,12,2,39,9,2,
        1,2,1,2,1,2,1,2,5,2,45,8,2,10,2,12,2,48,9,2,1,2,1,2,5,2,52,8,2,10,
        2,12,2,55,9,2,1,2,4,2,58,8,2,11,2,12,2,59,1,2,5,2,63,8,2,10,2,12,
        2,66,9,2,1,2,3,2,69,8,2,1,3,5,3,72,8,3,10,3,12,3,75,9,3,1,3,1,3,
        1,3,1,3,5,3,81,8,3,10,3,12,3,84,9,3,1,3,1,3,5,3,88,8,3,10,3,12,3,
        91,9,3,1,3,4,3,94,8,3,11,3,12,3,95,1,4,5,4,99,8,4,10,4,12,4,102,
        9,4,1,4,1,4,1,4,5,4,107,8,4,10,4,12,4,110,9,4,1,4,4,4,113,8,4,11,
        4,12,4,114,1,5,5,5,118,8,5,10,5,12,5,121,9,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,3,5,132,8,5,1,5,1,5,5,5,136,8,5,10,5,12,5,139,9,
        5,1,5,4,5,142,8,5,11,5,12,5,143,1,6,5,6,147,8,6,10,6,12,6,150,9,
        6,1,6,1,6,1,6,1,6,5,6,156,8,6,10,6,12,6,159,9,6,1,6,1,6,5,6,163,
        8,6,10,6,12,6,166,9,6,1,6,4,6,169,8,6,11,6,12,6,170,1,7,1,7,3,7,
        175,8,7,1,7,1,7,1,7,3,7,180,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,
        189,8,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,197,8,8,10,8,12,8,200,9,8,1,
        8,0,1,16,9,0,2,4,6,8,10,12,14,16,0,2,1,0,13,14,1,0,15,19,223,0,21,
        1,0,0,0,2,32,1,0,0,0,4,37,1,0,0,0,6,73,1,0,0,0,8,100,1,0,0,0,10,
        119,1,0,0,0,12,148,1,0,0,0,14,188,1,0,0,0,16,190,1,0,0,0,18,20,3,
        2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,
        24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,33,3,14,7,
        0,27,31,3,4,2,0,28,31,3,12,6,0,29,31,3,10,5,0,30,27,1,0,0,0,30,28,
        1,0,0,0,30,29,1,0,0,0,31,33,1,0,0,0,32,26,1,0,0,0,32,30,1,0,0,0,
        33,3,1,0,0,0,34,36,5,21,0,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,
        0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,41,5,1,0,0,41,
        46,3,14,7,0,42,43,5,14,0,0,43,45,3,14,7,0,44,42,1,0,0,0,45,48,1,
        0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,
        57,5,2,0,0,50,52,5,21,0,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,
        0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,0,56,58,3,2,1,0,57,53,
        1,0,0,0,58,59,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,64,1,0,0,0,
        61,63,3,6,3,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,
        0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,67,69,3,8,4,0,68,67,1,0,0,0,68,
        69,1,0,0,0,69,5,1,0,0,0,70,72,5,21,0,0,71,70,1,0,0,0,72,75,1,0,0,
        0,73,71,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,73,1,0,0,0,76,77,
        5,3,0,0,77,82,3,14,7,0,78,79,5,14,0,0,79,81,3,14,7,0,80,78,1,0,0,
        0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,
        1,0,0,0,85,93,5,2,0,0,86,88,5,21,0,0,87,86,1,0,0,0,88,91,1,0,0,0,
        89,87,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,94,3,
        2,1,0,93,89,1,0,0,0,94,95,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,
        7,1,0,0,0,97,99,5,21,0,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,
        0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,104,5,4,
        0,0,104,112,5,2,0,0,105,107,5,21,0,0,106,105,1,0,0,0,107,110,1,0,
        0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,108,1,0,
        0,0,111,113,3,2,1,0,112,108,1,0,0,0,113,114,1,0,0,0,114,112,1,0,
        0,0,114,115,1,0,0,0,115,9,1,0,0,0,116,118,5,21,0,0,117,116,1,0,0,
        0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,122,1,0,0,
        0,121,119,1,0,0,0,122,123,5,5,0,0,123,124,5,16,0,0,124,131,5,6,0,
        0,125,132,5,16,0,0,126,127,5,7,0,0,127,128,5,17,0,0,128,129,5,8,
        0,0,129,130,5,17,0,0,130,132,5,9,0,0,131,125,1,0,0,0,131,126,1,0,
        0,0,132,133,1,0,0,0,133,141,5,2,0,0,134,136,5,21,0,0,135,134,1,0,
        0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,140,1,0,
        0,0,139,137,1,0,0,0,140,142,3,2,1,0,141,137,1,0,0,0,142,143,1,0,
        0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,11,1,0,0,0,145,147,5,21,
        0,0,146,145,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,1,0,
        0,0,149,151,1,0,0,0,150,148,1,0,0,0,151,152,5,10,0,0,152,157,3,14,
        7,0,153,154,5,14,0,0,154,156,3,14,7,0,155,153,1,0,0,0,156,159,1,
        0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,157,1,
        0,0,0,160,168,5,2,0,0,161,163,5,21,0,0,162,161,1,0,0,0,163,166,1,
        0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,164,1,
        0,0,0,167,169,3,2,1,0,168,164,1,0,0,0,169,170,1,0,0,0,170,168,1,
        0,0,0,170,171,1,0,0,0,171,13,1,0,0,0,172,175,3,16,8,0,173,175,5,
        16,0,0,174,172,1,0,0,0,174,173,1,0,0,0,175,176,1,0,0,0,176,179,7,
        0,0,0,177,180,3,16,8,0,178,180,5,16,0,0,179,177,1,0,0,0,179,178,
        1,0,0,0,180,189,1,0,0,0,181,182,5,14,0,0,182,189,5,16,0,0,183,189,
        5,15,0,0,184,185,5,11,0,0,185,186,3,14,7,0,186,187,5,9,0,0,187,189,
        1,0,0,0,188,174,1,0,0,0,188,181,1,0,0,0,188,183,1,0,0,0,188,184,
        1,0,0,0,189,15,1,0,0,0,190,191,6,8,-1,0,191,192,7,1,0,0,192,198,
        1,0,0,0,193,194,10,2,0,0,194,195,5,12,0,0,195,197,3,16,8,3,196,193,
        1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,17,1,
        0,0,0,200,198,1,0,0,0,28,21,30,32,37,46,53,59,64,68,73,82,89,95,
        100,108,114,119,131,137,143,148,157,164,170,174,179,188,198
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3132450) != 0):
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
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 14, 15, 16, 17, 18, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.expression()
                pass
            elif token in [1, 5, 10, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 27
                    self.ifStatement()
                    pass

                elif la_ == 2:
                    self.state = 28
                    self.whileStatement()
                    pass

                elif la_ == 3:
                    self.state = 29
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
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 34
                self.match(PythonParserParser.INDENT)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(PythonParserParser.T__0)
            self.state = 41
            self.expression()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 42
                self.match(PythonParserParser.COND_OP)
                self.state = 43
                self.expression()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(PythonParserParser.T__1)
            self.state = 57 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 53
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 50
                            self.match(PythonParserParser.INDENT) 
                        self.state = 55
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                    self.state = 56
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 59 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 61
                    self.elif_() 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 67
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
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 70
                self.match(PythonParserParser.INDENT)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.match(PythonParserParser.T__2)
            self.state = 77
            self.expression()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 78
                self.match(PythonParserParser.COND_OP)
                self.state = 79
                self.expression()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(PythonParserParser.T__1)
            self.state = 93 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 89
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 86
                            self.match(PythonParserParser.INDENT) 
                        self.state = 91
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                    self.state = 92
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 95 
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
        self.enterRule(localctx, 8, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 97
                self.match(PythonParserParser.INDENT)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(PythonParserParser.T__3)
            self.state = 104
            self.match(PythonParserParser.T__1)
            self.state = 112 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 108
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 105
                            self.match(PythonParserParser.INDENT) 
                        self.state = 110
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                    self.state = 111
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 114 
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
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 116
                self.match(PythonParserParser.INDENT)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.match(PythonParserParser.T__4)
            self.state = 123
            self.match(PythonParserParser.VAR)
            self.state = 124
            self.match(PythonParserParser.T__5)
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 125
                self.match(PythonParserParser.VAR)
                pass
            elif token in [7]:
                self.state = 126
                self.match(PythonParserParser.T__6)
                self.state = 127
                self.match(PythonParserParser.NUMBER)
                self.state = 128
                self.match(PythonParserParser.T__7)
                self.state = 129
                self.match(PythonParserParser.NUMBER)
                self.state = 130
                self.match(PythonParserParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 133
            self.match(PythonParserParser.T__1)
            self.state = 141 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 137
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 134
                            self.match(PythonParserParser.INDENT) 
                        self.state = 139
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                    self.state = 140
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 143 
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
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 145
                self.match(PythonParserParser.INDENT)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(PythonParserParser.T__9)
            self.state = 152
            self.expression()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 153
                self.match(PythonParserParser.COND_OP)
                self.state = 154
                self.expression()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
            self.match(PythonParserParser.T__1)
            self.state = 168 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 164
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 161
                            self.match(PythonParserParser.INDENT) 
                        self.state = 166
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                    self.state = 167
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 170 
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
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 172
                    self.arithmatic(0)
                    pass

                elif la_ == 2:
                    self.state = 173
                    self.match(PythonParserParser.VAR)
                    pass


                self.state = 176
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 179
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 177
                    self.arithmatic(0)
                    pass

                elif la_ == 2:
                    self.state = 178
                    self.match(PythonParserParser.VAR)
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(PythonParserParser.COND_OP)
                self.state = 182
                self.match(PythonParserParser.VAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.match(PythonParserParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 184
                self.match(PythonParserParser.T__10)
                self.state = 185
                self.expression()
                self.state = 186
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
            self.state = 191
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1015808) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self._ctx.stop = self._input.LT(-1)
            self.state = 198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonParserParser.ArithmaticContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmatic)
                    self.state = 193
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 194
                    self.match(PythonParserParser.ARITH_OP)
                    self.state = 195
                    self.arithmatic(3) 
                self.state = 200
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
         




