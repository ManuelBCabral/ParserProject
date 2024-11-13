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
        4,1,32,109,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,3,0,19,8,0,5,0,21,8,0,10,0,12,0,24,9,0,1,0,1,0,
        1,1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,39,8,2,1,3,1,
        3,1,3,1,3,5,3,45,8,3,10,3,12,3,48,9,3,1,3,1,3,3,3,52,8,3,1,4,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,3,5,62,8,5,5,5,64,8,5,10,5,12,5,67,9,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,82,8,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,93,8,6,10,6,12,6,96,9,6,1,7,
        1,7,1,7,1,7,5,7,102,8,7,10,7,12,7,105,9,7,1,7,1,7,1,7,0,1,12,8,0,
        2,4,6,8,10,12,14,0,3,1,0,6,10,1,0,11,16,1,0,29,30,120,0,22,1,0,0,
        0,2,30,1,0,0,0,4,32,1,0,0,0,6,40,1,0,0,0,8,53,1,0,0,0,10,58,1,0,
        0,0,12,81,1,0,0,0,14,97,1,0,0,0,16,18,3,2,1,0,17,19,5,1,0,0,18,17,
        1,0,0,0,18,19,1,0,0,0,19,21,1,0,0,0,20,16,1,0,0,0,21,24,1,0,0,0,
        22,20,1,0,0,0,22,23,1,0,0,0,23,25,1,0,0,0,24,22,1,0,0,0,25,26,5,
        0,0,1,26,1,1,0,0,0,27,31,3,4,2,0,28,31,3,12,6,0,29,31,3,6,3,0,30,
        27,1,0,0,0,30,28,1,0,0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,5,21,0,
        0,33,38,5,20,0,0,34,39,3,12,6,0,35,39,3,14,7,0,36,39,5,24,0,0,37,
        39,5,25,0,0,38,34,1,0,0,0,38,35,1,0,0,0,38,36,1,0,0,0,38,37,1,0,
        0,0,39,5,1,0,0,0,40,41,5,26,0,0,41,46,3,8,4,0,42,43,5,27,0,0,43,
        45,3,8,4,0,44,42,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,
        0,47,51,1,0,0,0,48,46,1,0,0,0,49,50,5,28,0,0,50,52,3,10,5,0,51,49,
        1,0,0,0,51,52,1,0,0,0,52,7,1,0,0,0,53,54,5,2,0,0,54,55,3,12,6,0,
        55,56,5,3,0,0,56,57,3,10,5,0,57,9,1,0,0,0,58,65,5,4,0,0,59,61,3,
        2,1,0,60,62,5,1,0,0,61,60,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,
        59,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,
        0,67,65,1,0,0,0,68,69,5,5,0,0,69,11,1,0,0,0,70,71,6,6,-1,0,71,72,
        5,31,0,0,72,82,3,12,6,6,73,74,5,2,0,0,74,75,3,12,6,0,75,76,5,3,0,
        0,76,82,1,0,0,0,77,82,5,23,0,0,78,82,5,22,0,0,79,82,5,21,0,0,80,
        82,3,14,7,0,81,70,1,0,0,0,81,73,1,0,0,0,81,77,1,0,0,0,81,78,1,0,
        0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,94,1,0,0,0,83,84,10,9,0,0,84,
        85,7,0,0,0,85,93,3,12,6,10,86,87,10,8,0,0,87,88,7,1,0,0,88,93,3,
        12,6,9,89,90,10,7,0,0,90,91,7,2,0,0,91,93,3,12,6,8,92,83,1,0,0,0,
        92,86,1,0,0,0,92,89,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,
        0,0,0,95,13,1,0,0,0,96,94,1,0,0,0,97,98,5,17,0,0,98,103,3,12,6,0,
        99,100,5,18,0,0,100,102,3,12,6,0,101,99,1,0,0,0,102,105,1,0,0,0,
        103,101,1,0,0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,103,1,0,0,0,
        106,107,5,19,0,0,107,15,1,0,0,0,12,18,22,30,38,46,51,61,65,81,92,
        94,103
    ]

class PythonParserParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "'{'", "'}'", "'*'", 
                     "'/'", "'%'", "'+'", "'-'", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'!='", "'['", "','", "']'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'True'", "'False'", "'if'", 
                     "'elif'", "'else'", "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ASSIGN_OP", "ID", "STRING", "NUMBER", "TRUE", "FALSE", 
                      "IF", "ELIF", "ELSE", "AND", "OR", "NOT", "WS" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_assign = 2
    RULE_ifStatement = 3
    RULE_conditionBlock = 4
    RULE_block = 5
    RULE_expr = 6
    RULE_arrayLiteral = 7

    ruleNames =  [ "start", "statement", "assign", "ifStatement", "conditionBlock", 
                   "block", "expr", "arrayLiteral" ]

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
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    ASSIGN_OP=20
    ID=21
    STRING=22
    NUMBER=23
    TRUE=24
    FALSE=25
    IF=26
    ELIF=27
    ELSE=28
    AND=29
    OR=30
    NOT=31
    WS=32

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
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229403652) != 0):
                self.state = 16
                self.statement()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 17
                    self.match(PythonParserParser.T__0)


                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
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

        def assign(self):
            return self.getTypedRuleContext(PythonParserParser.AssignContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonParserParser.ExprContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(PythonParserParser.IfStatementContext,0)


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
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.ifStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonParserParser.ID, 0)

        def ASSIGN_OP(self):
            return self.getToken(PythonParserParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonParserParser.ExprContext,0)


        def arrayLiteral(self):
            return self.getTypedRuleContext(PythonParserParser.ArrayLiteralContext,0)


        def TRUE(self):
            return self.getToken(PythonParserParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(PythonParserParser.FALSE, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = PythonParserParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(PythonParserParser.ID)
            self.state = 33
            self.match(PythonParserParser.ASSIGN_OP)
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 34
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 35
                self.arrayLiteral()
                pass

            elif la_ == 3:
                self.state = 36
                self.match(PythonParserParser.TRUE)
                pass

            elif la_ == 4:
                self.state = 37
                self.match(PythonParserParser.FALSE)
                pass


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

        def IF(self):
            return self.getToken(PythonParserParser.IF, 0)

        def conditionBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ConditionBlockContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ConditionBlockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.ELIF)
            else:
                return self.getToken(PythonParserParser.ELIF, i)

        def ELSE(self):
            return self.getToken(PythonParserParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(PythonParserParser.BlockContext,0)


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
            self.state = 40
            self.match(PythonParserParser.IF)
            self.state = 41
            self.conditionBlock()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 42
                self.match(PythonParserParser.ELIF)
                self.state = 43
                self.conditionBlock()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 49
                self.match(PythonParserParser.ELSE)
                self.state = 50
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PythonParserParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(PythonParserParser.BlockContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_conditionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionBlock" ):
                listener.enterConditionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionBlock" ):
                listener.exitConditionBlock(self)




    def conditionBlock(self):

        localctx = PythonParserParser.ConditionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditionBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(PythonParserParser.T__1)
            self.state = 54
            self.expr(0)
            self.state = 55
            self.match(PythonParserParser.T__2)
            self.state = 56
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.StatementContext,i)


        def getRuleIndex(self):
            return PythonParserParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = PythonParserParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(PythonParserParser.T__3)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2229403652) != 0):
                self.state = 59
                self.statement()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 60
                    self.match(PythonParserParser.T__0)


                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(PythonParserParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(PythonParserParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ExprContext,i)


        def NUMBER(self):
            return self.getToken(PythonParserParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(PythonParserParser.STRING, 0)

        def ID(self):
            return self.getToken(PythonParserParser.ID, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(PythonParserParser.ArrayLiteralContext,0)


        def AND(self):
            return self.getToken(PythonParserParser.AND, 0)

        def OR(self):
            return self.getToken(PythonParserParser.OR, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParserParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.state = 71
                self.match(PythonParserParser.NOT)
                self.state = 72
                self.expr(6)
                pass
            elif token in [2]:
                self.state = 73
                self.match(PythonParserParser.T__1)
                self.state = 74
                self.expr(0)
                self.state = 75
                self.match(PythonParserParser.T__2)
                pass
            elif token in [23]:
                self.state = 77
                self.match(PythonParserParser.NUMBER)
                pass
            elif token in [22]:
                self.state = 78
                self.match(PythonParserParser.STRING)
                pass
            elif token in [21]:
                self.state = 79
                self.match(PythonParserParser.ID)
                pass
            elif token in [17]:
                self.state = 80
                self.arrayLiteral()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 92
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = PythonParserParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 83
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 84
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1984) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 85
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = PythonParserParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 87
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129024) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 88
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = PythonParserParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 90
                        _la = self._input.LA(1)
                        if not(_la==29 or _la==30):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 91
                        self.expr(8)
                        pass

             
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ExprContext,i)


        def getRuleIndex(self):
            return PythonParserParser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)




    def arrayLiteral(self):

        localctx = PythonParserParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(PythonParserParser.T__16)
            self.state = 98
            self.expr(0)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 99
                self.match(PythonParserParser.T__17)
                self.state = 100
                self.expr(0)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(PythonParserParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         




