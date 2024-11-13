# Generated from ParserProject.g4 by ANTLR 4.13.2
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
        4,1,33,149,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        3,0,29,8,0,5,0,31,8,0,10,0,12,0,34,9,0,1,0,1,0,1,1,1,1,1,1,3,1,41,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,49,8,2,1,3,1,3,1,3,5,3,54,8,3,10,
        3,12,3,57,9,3,1,4,1,4,1,4,5,4,62,8,4,10,4,12,4,65,9,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,3,5,75,8,5,1,6,1,6,1,6,5,6,80,8,6,10,6,12,
        6,83,9,6,1,7,1,7,1,7,5,7,88,8,7,10,7,12,7,91,9,7,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,3,8,103,8,8,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,5,10,116,8,10,10,10,12,10,119,9,10,1,10,
        1,10,1,10,3,10,124,8,10,1,11,1,11,1,11,3,11,129,8,11,5,11,131,8,
        11,10,11,12,11,134,9,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,142,8,
        12,10,12,12,12,145,9,12,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,
        16,18,20,22,24,0,3,1,0,10,11,1,0,12,14,1,0,15,20,157,0,32,1,0,0,
        0,2,40,1,0,0,0,4,42,1,0,0,0,6,50,1,0,0,0,8,58,1,0,0,0,10,74,1,0,
        0,0,12,76,1,0,0,0,14,84,1,0,0,0,16,102,1,0,0,0,18,104,1,0,0,0,20,
        106,1,0,0,0,22,125,1,0,0,0,24,137,1,0,0,0,26,28,3,2,1,0,27,29,5,
        29,0,0,28,27,1,0,0,0,28,29,1,0,0,0,29,31,1,0,0,0,30,26,1,0,0,0,31,
        34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,32,1,0,0,
        0,35,36,5,0,0,1,36,1,1,0,0,0,37,41,3,4,2,0,38,41,3,6,3,0,39,41,3,
        20,10,0,40,37,1,0,0,0,40,38,1,0,0,0,40,39,1,0,0,0,41,3,1,0,0,0,42,
        43,5,30,0,0,43,48,5,1,0,0,44,49,3,6,3,0,45,49,3,24,12,0,46,49,5,
        5,0,0,47,49,5,6,0,0,48,44,1,0,0,0,48,45,1,0,0,0,48,46,1,0,0,0,48,
        47,1,0,0,0,49,5,1,0,0,0,50,55,3,8,4,0,51,52,7,0,0,0,52,54,3,8,4,
        0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,7,1,
        0,0,0,57,55,1,0,0,0,58,63,3,10,5,0,59,60,7,1,0,0,60,62,3,10,5,0,
        61,59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,9,1,0,
        0,0,65,63,1,0,0,0,66,67,5,21,0,0,67,68,3,6,3,0,68,69,5,22,0,0,69,
        75,1,0,0,0,70,75,5,32,0,0,71,75,5,31,0,0,72,75,5,30,0,0,73,75,3,
        24,12,0,74,66,1,0,0,0,74,70,1,0,0,0,74,71,1,0,0,0,74,72,1,0,0,0,
        74,73,1,0,0,0,75,11,1,0,0,0,76,81,3,14,7,0,77,78,5,9,0,0,78,80,3,
        14,7,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,
        13,1,0,0,0,83,81,1,0,0,0,84,89,3,16,8,0,85,86,5,8,0,0,86,88,3,16,
        8,0,87,85,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,15,
        1,0,0,0,91,89,1,0,0,0,92,93,5,7,0,0,93,103,3,16,8,0,94,95,3,6,3,
        0,95,96,3,18,9,0,96,97,3,6,3,0,97,103,1,0,0,0,98,99,5,21,0,0,99,
        100,3,12,6,0,100,101,5,22,0,0,101,103,1,0,0,0,102,92,1,0,0,0,102,
        94,1,0,0,0,102,98,1,0,0,0,103,17,1,0,0,0,104,105,7,2,0,0,105,19,
        1,0,0,0,106,107,5,2,0,0,107,108,3,12,6,0,108,109,5,27,0,0,109,117,
        3,22,11,0,110,111,5,3,0,0,111,112,3,12,6,0,112,113,5,27,0,0,113,
        114,3,22,11,0,114,116,1,0,0,0,115,110,1,0,0,0,116,119,1,0,0,0,117,
        115,1,0,0,0,117,118,1,0,0,0,118,123,1,0,0,0,119,117,1,0,0,0,120,
        121,5,4,0,0,121,122,5,27,0,0,122,124,3,22,11,0,123,120,1,0,0,0,123,
        124,1,0,0,0,124,21,1,0,0,0,125,132,5,23,0,0,126,128,3,2,1,0,127,
        129,5,29,0,0,128,127,1,0,0,0,128,129,1,0,0,0,129,131,1,0,0,0,130,
        126,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,
        135,1,0,0,0,134,132,1,0,0,0,135,136,5,24,0,0,136,23,1,0,0,0,137,
        138,5,25,0,0,138,143,3,6,3,0,139,140,5,28,0,0,140,142,3,6,3,0,141,
        139,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,
        146,1,0,0,0,145,143,1,0,0,0,146,147,5,26,0,0,147,25,1,0,0,0,15,28,
        32,40,48,55,63,74,81,89,102,117,123,128,132,143
    ]

class ParserProjectParser ( Parser ):

    grammarFileName = "ParserProject.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'if'", "'elif'", "'else'", 
                     "'True'", "'False'", "'!'", "'&&'", "'||'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'!='", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "':'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "ASSIGN_OP", "IF", "ELIF", "ELSE", "TRUE", 
                      "FALSE", "NOT", "AND", "OR", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "LT", "LE", "GT", "GE", "EQ", "NE", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                      "RBRACKET", "COLON", "COMMA", "SEMICOLON", "ID", "STRING", 
                      "NUMBER", "WS" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_assign = 2
    RULE_expr = 3
    RULE_term = 4
    RULE_factor = 5
    RULE_conditionExpr = 6
    RULE_conditionTerm = 7
    RULE_conditionFactor = 8
    RULE_comparisonOp = 9
    RULE_ifStatement = 10
    RULE_statementBlock = 11
    RULE_arrayLiteral = 12

    ruleNames =  [ "start", "statement", "assign", "expr", "term", "factor", 
                   "conditionExpr", "conditionTerm", "conditionFactor", 
                   "comparisonOp", "ifStatement", "statementBlock", "arrayLiteral" ]

    EOF = Token.EOF
    ASSIGN_OP=1
    IF=2
    ELIF=3
    ELSE=4
    TRUE=5
    FALSE=6
    NOT=7
    AND=8
    OR=9
    ADD=10
    SUB=11
    MUL=12
    DIV=13
    MOD=14
    LT=15
    LE=16
    GT=17
    GE=18
    EQ=19
    NE=20
    LPAREN=21
    RPAREN=22
    LBRACE=23
    RBRACE=24
    LBRACKET=25
    RBRACKET=26
    COLON=27
    COMMA=28
    SEMICOLON=29
    ID=30
    STRING=31
    NUMBER=32
    WS=33

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
            return self.getToken(ParserProjectParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProjectParser.StatementContext)
            else:
                return self.getTypedRuleContext(ParserProjectParser.StatementContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProjectParser.SEMICOLON)
            else:
                return self.getToken(ParserProjectParser.SEMICOLON, i)

        def getRuleIndex(self):
            return ParserProjectParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = ParserProjectParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7551844356) != 0):
                self.state = 26
                self.statement()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 27
                    self.match(ParserProjectParser.SEMICOLON)


                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(ParserProjectParser.EOF)
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
            return self.getTypedRuleContext(ParserProjectParser.AssignContext,0)


        def expr(self):
            return self.getTypedRuleContext(ParserProjectParser.ExprContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ParserProjectParser.IfStatementContext,0)


        def getRuleIndex(self):
            return ParserProjectParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ParserProjectParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
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
            return self.getToken(ParserProjectParser.ID, 0)

        def ASSIGN_OP(self):
            return self.getToken(ParserProjectParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(ParserProjectParser.ExprContext,0)


        def arrayLiteral(self):
            return self.getTypedRuleContext(ParserProjectParser.ArrayLiteralContext,0)


        def TRUE(self):
            return self.getToken(ParserProjectParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ParserProjectParser.FALSE, 0)

        def getRuleIndex(self):
            return ParserProjectParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = ParserProjectParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(ParserProjectParser.ID)
            self.state = 43
            self.match(ParserProjectParser.ASSIGN_OP)
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 44
                self.expr()
                pass

            elif la_ == 2:
                self.state = 45
                self.arrayLiteral()
                pass

            elif la_ == 3:
                self.state = 46
                self.match(ParserProjectParser.TRUE)
                pass

            elif la_ == 4:
                self.state = 47
                self.match(ParserProjectParser.FALSE)
                pass


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

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProjectParser.TermContext)
            else:
                return self.getTypedRuleContext(ParserProjectParser.TermContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProjectParser.ADD)
            else:
                return self.getToken(ParserProjectParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProjectParser.SUB)
            else:
                return self.getToken(ParserProjectParser.SUB, i)

        def getRuleIndex(self):
            return ParserProjectParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ParserProjectParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.term()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==11:
                self.state = 51
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 52
                self.term()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProjectParser.FactorContext)
            else:
                return self.getTypedRuleContext(ParserProjectParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProjectParser.MUL)
            else:
                return self.getToken(ParserProjectParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProjectParser.DIV)
            else:
                return self.getToken(ParserProjectParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProjectParser.MOD)
            else:
                return self.getToken(ParserProjectParser.MOD, i)

        def getRuleIndex(self):
            return ParserProjectParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ParserProjectParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.factor()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0):
                self.state = 59
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 60
                self.factor()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ParserProjectParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ParserProjectParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ParserProjectParser.RPAREN, 0)

        def NUMBER(self):
            return self.getToken(ParserProjectParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ParserProjectParser.STRING, 0)

        def ID(self):
            return self.getToken(ParserProjectParser.ID, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(ParserProjectParser.ArrayLiteralContext,0)


        def getRuleIndex(self):
            return ParserProjectParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ParserProjectParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(ParserProjectParser.LPAREN)
                self.state = 67
                self.expr()
                self.state = 68
                self.match(ParserProjectParser.RPAREN)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(ParserProjectParser.NUMBER)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.match(ParserProjectParser.STRING)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(ParserProjectParser.ID)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 73
                self.arrayLiteral()
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


    class ConditionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProjectParser.ConditionTermContext)
            else:
                return self.getTypedRuleContext(ParserProjectParser.ConditionTermContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProjectParser.OR)
            else:
                return self.getToken(ParserProjectParser.OR, i)

        def getRuleIndex(self):
            return ParserProjectParser.RULE_conditionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionExpr" ):
                listener.enterConditionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionExpr" ):
                listener.exitConditionExpr(self)




    def conditionExpr(self):

        localctx = ParserProjectParser.ConditionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_conditionExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.conditionTerm()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 77
                self.match(ParserProjectParser.OR)
                self.state = 78
                self.conditionTerm()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionFactor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProjectParser.ConditionFactorContext)
            else:
                return self.getTypedRuleContext(ParserProjectParser.ConditionFactorContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProjectParser.AND)
            else:
                return self.getToken(ParserProjectParser.AND, i)

        def getRuleIndex(self):
            return ParserProjectParser.RULE_conditionTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionTerm" ):
                listener.enterConditionTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionTerm" ):
                listener.exitConditionTerm(self)




    def conditionTerm(self):

        localctx = ParserProjectParser.ConditionTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conditionTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.conditionFactor()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 85
                self.match(ParserProjectParser.AND)
                self.state = 86
                self.conditionFactor()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ParserProjectParser.NOT, 0)

        def conditionFactor(self):
            return self.getTypedRuleContext(ParserProjectParser.ConditionFactorContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProjectParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProjectParser.ExprContext,i)


        def comparisonOp(self):
            return self.getTypedRuleContext(ParserProjectParser.ComparisonOpContext,0)


        def LPAREN(self):
            return self.getToken(ParserProjectParser.LPAREN, 0)

        def conditionExpr(self):
            return self.getTypedRuleContext(ParserProjectParser.ConditionExprContext,0)


        def RPAREN(self):
            return self.getToken(ParserProjectParser.RPAREN, 0)

        def getRuleIndex(self):
            return ParserProjectParser.RULE_conditionFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionFactor" ):
                listener.enterConditionFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionFactor" ):
                listener.exitConditionFactor(self)




    def conditionFactor(self):

        localctx = ParserProjectParser.ConditionFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_conditionFactor)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(ParserProjectParser.NOT)
                self.state = 93
                self.conditionFactor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.expr()
                self.state = 95
                self.comparisonOp()
                self.state = 96
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.match(ParserProjectParser.LPAREN)
                self.state = 99
                self.conditionExpr()
                self.state = 100
                self.match(ParserProjectParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(ParserProjectParser.LT, 0)

        def LE(self):
            return self.getToken(ParserProjectParser.LE, 0)

        def GT(self):
            return self.getToken(ParserProjectParser.GT, 0)

        def GE(self):
            return self.getToken(ParserProjectParser.GE, 0)

        def EQ(self):
            return self.getToken(ParserProjectParser.EQ, 0)

        def NE(self):
            return self.getToken(ParserProjectParser.NE, 0)

        def getRuleIndex(self):
            return ParserProjectParser.RULE_comparisonOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOp" ):
                listener.enterComparisonOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOp" ):
                listener.exitComparisonOp(self)




    def comparisonOp(self):

        localctx = ParserProjectParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
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


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ParserProjectParser.IF, 0)

        def conditionExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProjectParser.ConditionExprContext)
            else:
                return self.getTypedRuleContext(ParserProjectParser.ConditionExprContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProjectParser.COLON)
            else:
                return self.getToken(ParserProjectParser.COLON, i)

        def statementBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProjectParser.StatementBlockContext)
            else:
                return self.getTypedRuleContext(ParserProjectParser.StatementBlockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProjectParser.ELIF)
            else:
                return self.getToken(ParserProjectParser.ELIF, i)

        def ELSE(self):
            return self.getToken(ParserProjectParser.ELSE, 0)

        def getRuleIndex(self):
            return ParserProjectParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = ParserProjectParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(ParserProjectParser.IF)
            self.state = 107
            self.conditionExpr()
            self.state = 108
            self.match(ParserProjectParser.COLON)
            self.state = 109
            self.statementBlock()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 110
                self.match(ParserProjectParser.ELIF)
                self.state = 111
                self.conditionExpr()
                self.state = 112
                self.match(ParserProjectParser.COLON)
                self.state = 113
                self.statementBlock()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 120
                self.match(ParserProjectParser.ELSE)
                self.state = 121
                self.match(ParserProjectParser.COLON)
                self.state = 122
                self.statementBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ParserProjectParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ParserProjectParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProjectParser.StatementContext)
            else:
                return self.getTypedRuleContext(ParserProjectParser.StatementContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProjectParser.SEMICOLON)
            else:
                return self.getToken(ParserProjectParser.SEMICOLON, i)

        def getRuleIndex(self):
            return ParserProjectParser.RULE_statementBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementBlock" ):
                listener.enterStatementBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementBlock" ):
                listener.exitStatementBlock(self)




    def statementBlock(self):

        localctx = ParserProjectParser.StatementBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statementBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(ParserProjectParser.LBRACE)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7551844356) != 0):
                self.state = 126
                self.statement()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 127
                    self.match(ParserProjectParser.SEMICOLON)


                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self.match(ParserProjectParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ParserProjectParser.LBRACKET, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProjectParser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProjectParser.ExprContext,i)


        def RBRACKET(self):
            return self.getToken(ParserProjectParser.RBRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProjectParser.COMMA)
            else:
                return self.getToken(ParserProjectParser.COMMA, i)

        def getRuleIndex(self):
            return ParserProjectParser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)




    def arrayLiteral(self):

        localctx = ParserProjectParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(ParserProjectParser.LBRACKET)
            self.state = 138
            self.expr()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 139
                self.match(ParserProjectParser.COMMA)
                self.state = 140
                self.expr()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(ParserProjectParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





