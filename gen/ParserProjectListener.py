# Generated from ParserProject.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ParserProjectParser import ParserProjectParser
else:
    from ParserProjectParser import ParserProjectParser

# This class defines a complete listener for a parse tree produced by ParserProjectParser.
class ParserProjectListener(ParseTreeListener):

    # Enter a parse tree produced by ParserProjectParser#start.
    def enterStart(self, ctx:ParserProjectParser.StartContext):
        pass

    # Exit a parse tree produced by ParserProjectParser#start.
    def exitStart(self, ctx:ParserProjectParser.StartContext):
        pass


    # Enter a parse tree produced by ParserProjectParser#statement.
    def enterStatement(self, ctx:ParserProjectParser.StatementContext):
        pass

    # Exit a parse tree produced by ParserProjectParser#statement.
    def exitStatement(self, ctx:ParserProjectParser.StatementContext):
        pass


    # Enter a parse tree produced by ParserProjectParser#assign.
    def enterAssign(self, ctx:ParserProjectParser.AssignContext):
        pass

    # Exit a parse tree produced by ParserProjectParser#assign.
    def exitAssign(self, ctx:ParserProjectParser.AssignContext):
        pass


    # Enter a parse tree produced by ParserProjectParser#expr.
    def enterExpr(self, ctx:ParserProjectParser.ExprContext):
        pass

    # Exit a parse tree produced by ParserProjectParser#expr.
    def exitExpr(self, ctx:ParserProjectParser.ExprContext):
        pass


    # Enter a parse tree produced by ParserProjectParser#term.
    def enterTerm(self, ctx:ParserProjectParser.TermContext):
        pass

    # Exit a parse tree produced by ParserProjectParser#term.
    def exitTerm(self, ctx:ParserProjectParser.TermContext):
        pass


    # Enter a parse tree produced by ParserProjectParser#factor.
    def enterFactor(self, ctx:ParserProjectParser.FactorContext):
        pass

    # Exit a parse tree produced by ParserProjectParser#factor.
    def exitFactor(self, ctx:ParserProjectParser.FactorContext):
        pass


    # Enter a parse tree produced by ParserProjectParser#conditionExpr.
    def enterConditionExpr(self, ctx:ParserProjectParser.ConditionExprContext):
        pass

    # Exit a parse tree produced by ParserProjectParser#conditionExpr.
    def exitConditionExpr(self, ctx:ParserProjectParser.ConditionExprContext):
        pass


    # Enter a parse tree produced by ParserProjectParser#conditionTerm.
    def enterConditionTerm(self, ctx:ParserProjectParser.ConditionTermContext):
        pass

    # Exit a parse tree produced by ParserProjectParser#conditionTerm.
    def exitConditionTerm(self, ctx:ParserProjectParser.ConditionTermContext):
        pass


    # Enter a parse tree produced by ParserProjectParser#conditionFactor.
    def enterConditionFactor(self, ctx:ParserProjectParser.ConditionFactorContext):
        pass

    # Exit a parse tree produced by ParserProjectParser#conditionFactor.
    def exitConditionFactor(self, ctx:ParserProjectParser.ConditionFactorContext):
        pass


    # Enter a parse tree produced by ParserProjectParser#comparisonOp.
    def enterComparisonOp(self, ctx:ParserProjectParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by ParserProjectParser#comparisonOp.
    def exitComparisonOp(self, ctx:ParserProjectParser.ComparisonOpContext):
        pass


    # Enter a parse tree produced by ParserProjectParser#ifStatement.
    def enterIfStatement(self, ctx:ParserProjectParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ParserProjectParser#ifStatement.
    def exitIfStatement(self, ctx:ParserProjectParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ParserProjectParser#statementBlock.
    def enterStatementBlock(self, ctx:ParserProjectParser.StatementBlockContext):
        pass

    # Exit a parse tree produced by ParserProjectParser#statementBlock.
    def exitStatementBlock(self, ctx:ParserProjectParser.StatementBlockContext):
        pass


    # Enter a parse tree produced by ParserProjectParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:ParserProjectParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by ParserProjectParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:ParserProjectParser.ArrayLiteralContext):
        pass



del ParserProjectParser