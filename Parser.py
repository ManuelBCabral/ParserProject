import sys
from antlr4 import *
from gen.PythonParserLexer import PythonParserLexer
from gen.PythonParserParser import PythonParserParser

def main(input_text):
    #Convert input text into an ANTLR input stream
    input_stream = InputStream(input_text)
    
    #Create a lexer for the input
    lexer = PythonParserLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    #Create a parser for the token stream
    parser = PythonParserParser(token_stream)

    tree = parser.expr()
    
    #Print the parse tree (or process it as needed)
    print(tree.toStringTree(recog=parser))  # Display the parse tree in text form

if __name__ == '__main__':
    # Sample input to parse
    input_text = sys.argv[1] if len(sys.argv) > 1 else "3 + 5 * (10 - 4)"
    main(input_text)
