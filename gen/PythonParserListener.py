# Generated from PythonParser.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by PythonParserParser#indentStatement.
    def enterIndentStatement(self, ctx:PythonParserParser.IndentStatementContext):
        pass

    # Exit a parse tree produced by PythonParserParser#indentStatement.
    def exitIndentStatement(self, ctx:PythonParserParser.IndentStatementContext):
        pass


    # Enter a parse tree produced by PythonParserParser#ifStatement.
    def enterIfStatement(self, ctx:PythonParserParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PythonParserParser#ifStatement.
    def exitIfStatement(self, ctx:PythonParserParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PythonParserParser#elif.
    def enterElif(self, ctx:PythonParserParser.ElifContext):
        pass

    # Exit a parse tree produced by PythonParserParser#elif.
    def exitElif(self, ctx:PythonParserParser.ElifContext):
        pass


    # Enter a parse tree produced by PythonParserParser#else.
    def enterElse(self, ctx:PythonParserParser.ElseContext):
        pass

    # Exit a parse tree produced by PythonParserParser#else.
    def exitElse(self, ctx:PythonParserParser.ElseContext):
        pass


    # Enter a parse tree produced by PythonParserParser#forStatement.
    def enterForStatement(self, ctx:PythonParserParser.ForStatementContext):
        pass

    # Exit a parse tree produced by PythonParserParser#forStatement.
    def exitForStatement(self, ctx:PythonParserParser.ForStatementContext):
        pass


    # Enter a parse tree produced by PythonParserParser#whileStatement.
    def enterWhileStatement(self, ctx:PythonParserParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PythonParserParser#whileStatement.
    def exitWhileStatement(self, ctx:PythonParserParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PythonParserParser#expression.
    def enterExpression(self, ctx:PythonParserParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PythonParserParser#expression.
    def exitExpression(self, ctx:PythonParserParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PythonParserParser#arithmatic.
    def enterArithmatic(self, ctx:PythonParserParser.ArithmaticContext):
        pass

    # Exit a parse tree produced by PythonParserParser#arithmatic.
    def exitArithmatic(self, ctx:PythonParserParser.ArithmaticContext):
        pass



del PythonParserParser