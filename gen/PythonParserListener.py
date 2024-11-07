# Generated from PythonParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonParserParser import PythonParserParser
else:
    from PythonParserParser import PythonParserParser

# This class defines a complete listener for a parse tree produced by PythonParserParser.
class PythonParserListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParserParser#Add.
    def enterAdd(self, ctx:PythonParserParser.AddContext):
        pass

    # Exit a parse tree produced by PythonParserParser#Add.
    def exitAdd(self, ctx:PythonParserParser.AddContext):
        pass


    # Enter a parse tree produced by PythonParserParser#Divide.
    def enterDivide(self, ctx:PythonParserParser.DivideContext):
        pass

    # Exit a parse tree produced by PythonParserParser#Divide.
    def exitDivide(self, ctx:PythonParserParser.DivideContext):
        pass


    # Enter a parse tree produced by PythonParserParser#Number.
    def enterNumber(self, ctx:PythonParserParser.NumberContext):
        pass

    # Exit a parse tree produced by PythonParserParser#Number.
    def exitNumber(self, ctx:PythonParserParser.NumberContext):
        pass


    # Enter a parse tree produced by PythonParserParser#Multiply.
    def enterMultiply(self, ctx:PythonParserParser.MultiplyContext):
        pass

    # Exit a parse tree produced by PythonParserParser#Multiply.
    def exitMultiply(self, ctx:PythonParserParser.MultiplyContext):
        pass


    # Enter a parse tree produced by PythonParserParser#Subtract.
    def enterSubtract(self, ctx:PythonParserParser.SubtractContext):
        pass

    # Exit a parse tree produced by PythonParserParser#Subtract.
    def exitSubtract(self, ctx:PythonParserParser.SubtractContext):
        pass


    # Enter a parse tree produced by PythonParserParser#Parentheses.
    def enterParentheses(self, ctx:PythonParserParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by PythonParserParser#Parentheses.
    def exitParentheses(self, ctx:PythonParserParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by PythonParserParser#Power.
    def enterPower(self, ctx:PythonParserParser.PowerContext):
        pass

    # Exit a parse tree produced by PythonParserParser#Power.
    def exitPower(self, ctx:PythonParserParser.PowerContext):
        pass



del PythonParserParser