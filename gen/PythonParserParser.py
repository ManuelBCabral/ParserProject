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
        4,1,17,52,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,3,0,11,8,0,1,1,
        1,1,1,1,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,28,
        8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,36,8,2,10,2,12,2,39,9,2,1,3,1,3,
        1,3,1,3,5,3,45,8,3,10,3,12,3,48,9,3,1,3,1,3,1,3,0,1,4,4,0,2,4,6,
        0,2,1,0,15,16,1,0,3,7,56,0,10,1,0,0,0,2,12,1,0,0,0,4,27,1,0,0,0,
        6,40,1,0,0,0,8,11,3,2,1,0,9,11,3,4,2,0,10,8,1,0,0,0,10,9,1,0,0,0,
        11,1,1,0,0,0,12,13,5,14,0,0,13,17,5,13,0,0,14,18,3,4,2,0,15,18,5,
        1,0,0,16,18,5,2,0,0,17,14,1,0,0,0,17,15,1,0,0,0,17,16,1,0,0,0,18,
        3,1,0,0,0,19,20,6,2,-1,0,20,21,5,8,0,0,21,22,3,4,2,0,22,23,5,9,0,
        0,23,28,1,0,0,0,24,28,7,0,0,0,25,28,5,14,0,0,26,28,3,6,3,0,27,19,
        1,0,0,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,0,28,37,1,0,0,0,
        29,30,10,6,0,0,30,31,5,13,0,0,31,36,3,4,2,7,32,33,10,5,0,0,33,34,
        7,1,0,0,34,36,3,4,2,6,35,29,1,0,0,0,35,32,1,0,0,0,36,39,1,0,0,0,
        37,35,1,0,0,0,37,38,1,0,0,0,38,5,1,0,0,0,39,37,1,0,0,0,40,41,5,10,
        0,0,41,46,3,4,2,0,42,43,5,11,0,0,43,45,3,4,2,0,44,42,1,0,0,0,45,
        48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,
        0,49,50,5,12,0,0,50,7,1,0,0,0,6,10,17,27,35,37,46
    ]

class PythonParserParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'True'", "'False'", "'*'", "'/'", "'%'", 
                     "'+'", "'-'", "'('", "')'", "'['", "','", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ASSIGN_OP", "ID", "STRING", "NUMBER", 
                      "WS" ]

    RULE_start = 0
    RULE_assign = 1
    RULE_expr = 2
    RULE_arrayLiteral = 3

    ruleNames =  [ "start", "assign", "expr", "arrayLiteral" ]

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
    ASSIGN_OP=13
    ID=14
    STRING=15
    NUMBER=16
    WS=17

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

        def assign(self):
            return self.getTypedRuleContext(PythonParserParser.AssignContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonParserParser.ExprContext,0)


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
        try:
            self.state = 10
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.expr(0)
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
        self.enterRule(localctx, 2, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(PythonParserParser.ID)
            self.state = 13
            self.match(PythonParserParser.ASSIGN_OP)
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 10, 14, 15, 16]:
                self.state = 14
                self.expr(0)
                pass
            elif token in [1]:
                self.state = 15
                self.match(PythonParserParser.T__0)
                pass
            elif token in [2]:
                self.state = 16
                self.match(PythonParserParser.T__1)
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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


        def ASSIGN_OP(self):
            return self.getToken(PythonParserParser.ASSIGN_OP, 0)

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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 20
                self.match(PythonParserParser.T__7)
                self.state = 21
                self.expr(0)
                self.state = 22
                self.match(PythonParserParser.T__8)
                pass
            elif token in [15, 16]:
                self.state = 24
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [14]:
                self.state = 25
                self.match(PythonParserParser.ID)
                pass
            elif token in [10]:
                self.state = 26
                self.arrayLiteral()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 35
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = PythonParserParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 30
                        self.match(PythonParserParser.ASSIGN_OP)
                        self.state = 31
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = PythonParserParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 33
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 248) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 34
                        self.expr(6)
                        pass

             
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(PythonParserParser.T__9)
            self.state = 41
            self.expr(0)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 42
                self.match(PythonParserParser.T__10)
                self.state = 43
                self.expr(0)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(PythonParserParser.T__11)
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
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




