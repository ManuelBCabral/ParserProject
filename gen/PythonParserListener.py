# Generated from PythonParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .PythonParserParser import PythonParserParser
else:
    from PythonParserParser import PythonParserParser

# This class defines a complete listener for a parse tree produced by PythonParserParser.
class PythonParserListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParserParser#start.
    def enterStart(self, ctx:PythonParserParser.StartContext):
        pass

    # Exit a parse tree produced by PythonParserParser#start.
    def exitStart(self, ctx:PythonParserParser.StartContext):
        pass


    # Enter a parse tree produced by PythonParserParser#statement.
    def enterStatement(self, ctx:PythonParserParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonParserParser#statement.
    def exitStatement(self, ctx:PythonParserParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonParserParser#assignment.
    def enterAssignment(self, ctx:PythonParserParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PythonParserParser#assignment.
    def exitAssignment(self, ctx:PythonParserParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PythonParserParser#arithmetic.
    def enterArithmetic(self, ctx:PythonParserParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by PythonParserParser#arithmetic.
    def exitArithmetic(self, ctx:PythonParserParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by PythonParserParser#condition.
    def enterCondition(self, ctx:PythonParserParser.ConditionContext):
        pass

    # Exit a parse tree produced by PythonParserParser#condition.
    def exitCondition(self, ctx:PythonParserParser.ConditionContext):
        pass


    # Enter a parse tree produced by PythonParserParser#ifStatement.
    def enterIfStatement(self, ctx:PythonParserParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PythonParserParser#ifStatement.
    def exitIfStatement(self, ctx:PythonParserParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PythonParserParser#block.
    def enterBlock(self, ctx:PythonParserParser.BlockContext):
        pass

    # Exit a parse tree produced by PythonParserParser#block.
    def exitBlock(self, ctx:PythonParserParser.BlockContext):
        pass


    # Enter a parse tree produced by PythonParserParser#array.
    def enterArray(self, ctx:PythonParserParser.ArrayContext):
        pass

    # Exit a parse tree produced by PythonParserParser#array.
    def exitArray(self, ctx:PythonParserParser.ArrayContext):
        pass


    # Enter a parse tree produced by PythonParserParser#expr.
    def enterExpr(self, ctx:PythonParserParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonParserParser#expr.
    def exitExpr(self, ctx:PythonParserParser.ExprContext):
        pass



del PythonParserParser