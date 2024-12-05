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
        4,1,28,192,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,46,8,2,1,2,1,2,1,2,1,2,3,2,52,8,2,5,2,54,8,2,10,
        2,12,2,57,9,2,1,3,1,3,1,3,3,3,62,8,3,1,3,1,3,1,3,5,3,67,8,3,10,3,
        12,3,70,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,82,8,4,1,
        4,1,4,1,4,1,4,1,4,1,4,5,4,90,8,4,10,4,12,4,93,9,4,1,5,1,5,3,5,97,
        8,5,1,5,1,5,3,5,101,8,5,1,5,1,5,4,5,105,8,5,11,5,12,5,106,1,5,1,
        5,3,5,111,8,5,1,5,1,5,3,5,115,8,5,1,5,1,5,4,5,119,8,5,11,5,12,5,
        120,5,5,123,8,5,10,5,12,5,126,9,5,1,5,1,5,1,5,4,5,131,8,5,11,5,12,
        5,132,3,5,135,8,5,1,6,1,6,3,6,139,8,6,1,6,1,6,3,6,143,8,6,1,6,1,
        6,4,6,147,8,6,11,6,12,6,148,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        3,7,160,8,7,1,7,3,7,163,8,7,1,7,1,7,4,7,167,8,7,11,7,12,7,168,1,
        8,1,8,3,8,173,8,8,1,9,1,9,1,10,1,10,1,10,1,10,5,10,181,8,10,10,10,
        12,10,184,9,10,3,10,186,8,10,1,10,1,10,1,11,1,11,1,11,0,3,4,6,8,
        12,0,2,4,6,8,10,12,14,16,18,20,22,0,2,1,0,1,2,1,0,22,24,216,0,27,
        1,0,0,0,2,36,1,0,0,0,4,45,1,0,0,0,6,61,1,0,0,0,8,81,1,0,0,0,10,94,
        1,0,0,0,12,136,1,0,0,0,14,150,1,0,0,0,16,172,1,0,0,0,18,174,1,0,
        0,0,20,176,1,0,0,0,22,189,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,
        29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,
        0,30,31,5,0,0,1,31,1,1,0,0,0,32,37,3,10,5,0,33,37,3,4,2,0,34,37,
        3,12,6,0,35,37,3,14,7,0,36,32,1,0,0,0,36,33,1,0,0,0,36,34,1,0,0,
        0,36,35,1,0,0,0,37,3,1,0,0,0,38,39,6,2,-1,0,39,46,5,25,0,0,40,46,
        5,21,0,0,41,46,5,23,0,0,42,46,5,22,0,0,43,46,5,24,0,0,44,46,3,20,
        10,0,45,38,1,0,0,0,45,40,1,0,0,0,45,41,1,0,0,0,45,42,1,0,0,0,45,
        43,1,0,0,0,45,44,1,0,0,0,46,55,1,0,0,0,47,48,10,7,0,0,48,51,5,18,
        0,0,49,52,3,4,2,0,50,52,3,6,3,0,51,49,1,0,0,0,51,50,1,0,0,0,52,54,
        1,0,0,0,53,47,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,
        56,5,1,0,0,0,57,55,1,0,0,0,58,59,6,3,-1,0,59,62,5,21,0,0,60,62,5,
        23,0,0,61,58,1,0,0,0,61,60,1,0,0,0,62,68,1,0,0,0,63,64,10,3,0,0,
        64,65,5,17,0,0,65,67,3,6,3,4,66,63,1,0,0,0,67,70,1,0,0,0,68,66,1,
        0,0,0,68,69,1,0,0,0,69,7,1,0,0,0,70,68,1,0,0,0,71,72,6,4,-1,0,72,
        73,5,3,0,0,73,82,3,8,4,5,74,75,5,4,0,0,75,76,3,8,4,0,76,77,5,5,0,
        0,77,82,1,0,0,0,78,82,5,21,0,0,79,82,5,23,0,0,80,82,5,25,0,0,81,
        71,1,0,0,0,81,74,1,0,0,0,81,78,1,0,0,0,81,79,1,0,0,0,81,80,1,0,0,
        0,82,91,1,0,0,0,83,84,10,7,0,0,84,85,7,0,0,0,85,90,3,8,4,8,86,87,
        10,6,0,0,87,88,5,19,0,0,88,90,3,8,4,7,89,83,1,0,0,0,89,86,1,0,0,
        0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,9,1,0,0,0,93,91,1,
        0,0,0,94,96,5,6,0,0,95,97,5,4,0,0,96,95,1,0,0,0,96,97,1,0,0,0,97,
        98,1,0,0,0,98,100,3,8,4,0,99,101,5,5,0,0,100,99,1,0,0,0,100,101,
        1,0,0,0,101,102,1,0,0,0,102,104,5,7,0,0,103,105,3,18,9,0,104,103,
        1,0,0,0,105,106,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,124,
        1,0,0,0,108,110,5,8,0,0,109,111,5,4,0,0,110,109,1,0,0,0,110,111,
        1,0,0,0,111,112,1,0,0,0,112,114,3,8,4,0,113,115,5,5,0,0,114,113,
        1,0,0,0,114,115,1,0,0,0,115,116,1,0,0,0,116,118,5,7,0,0,117,119,
        3,18,9,0,118,117,1,0,0,0,119,120,1,0,0,0,120,118,1,0,0,0,120,121,
        1,0,0,0,121,123,1,0,0,0,122,108,1,0,0,0,123,126,1,0,0,0,124,122,
        1,0,0,0,124,125,1,0,0,0,125,134,1,0,0,0,126,124,1,0,0,0,127,128,
        5,9,0,0,128,130,5,7,0,0,129,131,3,18,9,0,130,129,1,0,0,0,131,132,
        1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,135,1,0,0,0,134,127,
        1,0,0,0,134,135,1,0,0,0,135,11,1,0,0,0,136,138,5,10,0,0,137,139,
        5,4,0,0,138,137,1,0,0,0,138,139,1,0,0,0,139,140,1,0,0,0,140,142,
        3,8,4,0,141,143,5,5,0,0,142,141,1,0,0,0,142,143,1,0,0,0,143,144,
        1,0,0,0,144,146,5,7,0,0,145,147,3,18,9,0,146,145,1,0,0,0,147,148,
        1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,13,1,0,0,0,150,151,5,
        11,0,0,151,152,5,21,0,0,152,162,5,12,0,0,153,163,3,16,8,0,154,155,
        5,13,0,0,155,156,5,4,0,0,156,159,5,23,0,0,157,158,5,14,0,0,158,160,
        5,23,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,161,1,0,0,0,161,163,
        5,5,0,0,162,153,1,0,0,0,162,154,1,0,0,0,163,164,1,0,0,0,164,166,
        5,7,0,0,165,167,3,18,9,0,166,165,1,0,0,0,167,168,1,0,0,0,168,166,
        1,0,0,0,168,169,1,0,0,0,169,15,1,0,0,0,170,173,3,20,10,0,171,173,
        5,21,0,0,172,170,1,0,0,0,172,171,1,0,0,0,173,17,1,0,0,0,174,175,
        3,2,1,0,175,19,1,0,0,0,176,185,5,15,0,0,177,182,3,22,11,0,178,179,
        5,14,0,0,179,181,3,22,11,0,180,178,1,0,0,0,181,184,1,0,0,0,182,180,
        1,0,0,0,182,183,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,185,177,
        1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,188,5,16,0,0,188,21,
        1,0,0,0,189,190,7,1,0,0,190,23,1,0,0,0,28,27,36,45,51,55,61,68,81,
        89,91,96,100,106,110,114,120,124,132,134,138,142,148,159,162,168,
        172,182,185
    ]

class PythonParserParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'('", "')'", 
                     "'if'", "':'", "'elif'", "'else'", "'while'", "'for'", 
                     "'in'", "'range'", "','", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ARITH_OP", "ASSIGN_OP", "COND_OP", "NEWLINE", 
                      "VAR", "CHAR", "NUM", "STRING", "BOOL", "WS", "COMMENT", 
                      "MULTICOMMENT" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_arithmetic = 3
    RULE_condition = 4
    RULE_ifStatement = 5
    RULE_whileStatement = 6
    RULE_forStatement = 7
    RULE_loopStructure = 8
    RULE_block = 9
    RULE_array = 10
    RULE_expr = 11

    ruleNames =  [ "start", "statement", "assignment", "arithmetic", "condition", 
                   "ifStatement", "whileStatement", "forStatement", "loopStructure", 
                   "block", "array", "expr" ]

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
    ARITH_OP=17
    ASSIGN_OP=18
    COND_OP=19
    NEWLINE=20
    VAR=21
    CHAR=22
    NUM=23
    STRING=24
    BOOL=25
    WS=26
    COMMENT=27
    MULTICOMMENT=28

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
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 65047616) != 0):
                self.state = 24
                self.statement()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
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

        def ifStatement(self):
            return self.getTypedRuleContext(PythonParserParser.IfStatementContext,0)


        def assignment(self):
            return self.getTypedRuleContext(PythonParserParser.AssignmentContext,0)


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
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.ifStatement()
                pass
            elif token in [15, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.assignment(0)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.whileStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(PythonParserParser.BOOL, 0)

        def VAR(self):
            return self.getToken(PythonParserParser.VAR, 0)

        def NUM(self):
            return self.getToken(PythonParserParser.NUM, 0)

        def CHAR(self):
            return self.getToken(PythonParserParser.CHAR, 0)

        def STRING(self):
            return self.getToken(PythonParserParser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(PythonParserParser.ArrayContext,0)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.AssignmentContext,i)


        def ASSIGN_OP(self):
            return self.getToken(PythonParserParser.ASSIGN_OP, 0)

        def arithmetic(self):
            return self.getTypedRuleContext(PythonParserParser.ArithmeticContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)



    def assignment(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParserParser.AssignmentContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_assignment, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 39
                self.match(PythonParserParser.BOOL)
                pass
            elif token in [21]:
                self.state = 40
                self.match(PythonParserParser.VAR)
                pass
            elif token in [23]:
                self.state = 41
                self.match(PythonParserParser.NUM)
                pass
            elif token in [22]:
                self.state = 42
                self.match(PythonParserParser.CHAR)
                pass
            elif token in [24]:
                self.state = 43
                self.match(PythonParserParser.STRING)
                pass
            elif token in [15]:
                self.state = 44
                self.array()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonParserParser.AssignmentContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignment)
                    self.state = 47
                    if not self.precpred(self._ctx, 7):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                    self.state = 48
                    self.match(PythonParserParser.ASSIGN_OP)
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        self.state = 49
                        self.assignment(0)
                        pass

                    elif la_ == 2:
                        self.state = 50
                        self.arithmetic(0)
                        pass

             
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(PythonParserParser.VAR, 0)

        def NUM(self):
            return self.getToken(PythonParserParser.NUM, 0)

        def arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ArithmeticContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ArithmeticContext,i)


        def ARITH_OP(self):
            return self.getToken(PythonParserParser.ARITH_OP, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)



    def arithmetic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParserParser.ArithmeticContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_arithmetic, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 59
                self.match(PythonParserParser.VAR)
                pass
            elif token in [23]:
                self.state = 60
                self.match(PythonParserParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonParserParser.ArithmeticContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                    self.state = 63
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 64
                    self.match(PythonParserParser.ARITH_OP)
                    self.state = 65
                    self.arithmetic(4) 
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ConditionContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ConditionContext,i)


        def VAR(self):
            return self.getToken(PythonParserParser.VAR, 0)

        def NUM(self):
            return self.getToken(PythonParserParser.NUM, 0)

        def BOOL(self):
            return self.getToken(PythonParserParser.BOOL, 0)

        def COND_OP(self):
            return self.getToken(PythonParserParser.COND_OP, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParserParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_condition, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 72
                self.match(PythonParserParser.T__2)
                self.state = 73
                self.condition(5)
                pass
            elif token in [4]:
                self.state = 74
                self.match(PythonParserParser.T__3)
                self.state = 75
                self.condition(0)
                self.state = 76
                self.match(PythonParserParser.T__4)
                pass
            elif token in [21]:
                self.state = 78
                self.match(PythonParserParser.VAR)
                pass
            elif token in [23]:
                self.state = 79
                self.match(PythonParserParser.NUM)
                pass
            elif token in [25]:
                self.state = 80
                self.match(PythonParserParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 89
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = PythonParserParser.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 83
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 84
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 85
                        self.condition(8)
                        pass

                    elif la_ == 2:
                        localctx = PythonParserParser.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 86
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 87
                        self.match(PythonParserParser.COND_OP)
                        self.state = 88
                        self.condition(7)
                        pass

             
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ConditionContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ConditionContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.BlockContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.BlockContext,i)


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
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(PythonParserParser.T__5)
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 95
                self.match(PythonParserParser.T__3)


            self.state = 98
            self.condition(0)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 99
                self.match(PythonParserParser.T__4)


            self.state = 102
            self.match(PythonParserParser.T__6)
            self.state = 104 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 103
                    self.block()

                else:
                    raise NoViableAltException(self)
                self.state = 106 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 108
                    self.match(PythonParserParser.T__7)
                    self.state = 110
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        self.state = 109
                        self.match(PythonParserParser.T__3)


                    self.state = 112
                    self.condition(0)
                    self.state = 114
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 113
                        self.match(PythonParserParser.T__4)


                    self.state = 116
                    self.match(PythonParserParser.T__6)
                    self.state = 118 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 117
                            self.block()

                        else:
                            raise NoViableAltException(self)
                        self.state = 120 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
             
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 127
                self.match(PythonParserParser.T__8)
                self.state = 128
                self.match(PythonParserParser.T__6)
                self.state = 130 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 129
                        self.block()

                    else:
                        raise NoViableAltException(self)
                    self.state = 132 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)



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

        def condition(self):
            return self.getTypedRuleContext(PythonParserParser.ConditionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.BlockContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.BlockContext,i)


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
            self.state = 136
            self.match(PythonParserParser.T__9)
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 137
                self.match(PythonParserParser.T__3)


            self.state = 140
            self.condition(0)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 141
                self.match(PythonParserParser.T__4)


            self.state = 144
            self.match(PythonParserParser.T__6)
            self.state = 146 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 145
                    self.block()

                else:
                    raise NoViableAltException(self)
                self.state = 148 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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

        def VAR(self):
            return self.getToken(PythonParserParser.VAR, 0)

        def loopStructure(self):
            return self.getTypedRuleContext(PythonParserParser.LoopStructureContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.BlockContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.BlockContext,i)


        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.NUM)
            else:
                return self.getToken(PythonParserParser.NUM, i)

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
        self.enterRule(localctx, 14, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(PythonParserParser.T__10)
            self.state = 151
            self.match(PythonParserParser.VAR)
            self.state = 152
            self.match(PythonParserParser.T__11)
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 21]:
                self.state = 153
                self.loopStructure()
                pass
            elif token in [13]:
                self.state = 154
                self.match(PythonParserParser.T__12)
                self.state = 155
                self.match(PythonParserParser.T__3)
                self.state = 156
                self.match(PythonParserParser.NUM)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 157
                    self.match(PythonParserParser.T__13)
                    self.state = 158
                    self.match(PythonParserParser.NUM)


                self.state = 161
                self.match(PythonParserParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 164
            self.match(PythonParserParser.T__6)
            self.state = 166 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 165
                    self.block()

                else:
                    raise NoViableAltException(self)
                self.state = 168 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStructureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(PythonParserParser.ArrayContext,0)


        def VAR(self):
            return self.getToken(PythonParserParser.VAR, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_loopStructure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStructure" ):
                listener.enterLoopStructure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStructure" ):
                listener.exitLoopStructure(self)




    def loopStructure(self):

        localctx = PythonParserParser.LoopStructureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_loopStructure)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.array()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(PythonParserParser.VAR)
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


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(PythonParserParser.StatementContext,0)


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
        self.enterRule(localctx, 18, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
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
            return PythonParserParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = PythonParserParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(PythonParserParser.T__14)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0):
                self.state = 177
                self.expr()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 178
                    self.match(PythonParserParser.T__13)
                    self.state = 179
                    self.expr()
                    self.state = 184
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 187
            self.match(PythonParserParser.T__15)
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

        def CHAR(self):
            return self.getToken(PythonParserParser.CHAR, 0)

        def NUM(self):
            return self.getToken(PythonParserParser.NUM, 0)

        def STRING(self):
            return self.getToken(PythonParserParser.STRING, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = PythonParserParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.assignment_sempred
        self._predicates[3] = self.arithmetic_sempred
        self._predicates[4] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def assignment_sempred(self, localctx:AssignmentContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

    def arithmetic_sempred(self, localctx:ArithmeticContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




