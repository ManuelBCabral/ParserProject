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


    # Enter a parse tree produced by PythonParserParser#assign.
    def enterAssign(self, ctx:PythonParserParser.AssignContext):
        pass

    # Exit a parse tree produced by PythonParserParser#assign.
    def exitAssign(self, ctx:PythonParserParser.AssignContext):
        pass


    # Enter a parse tree produced by PythonParserParser#expr.
    def enterExpr(self, ctx:PythonParserParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonParserParser#expr.
    def exitExpr(self, ctx:PythonParserParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonParserParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:PythonParserParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by PythonParserParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:PythonParserParser.ArrayLiteralContext):
        pass



del PythonParserParser