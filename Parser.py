import sys
from antlr4 import *
from gen.PythonParserLexer import PythonParserLexer
from gen.PythonParserParser import PythonParserParser

def main(input_file):
    # Read the content of the input file
    with open(input_file, 'r') as file:
        input_text = file.read()
    
    # Convert input text into an ANTLR input stream
    input_stream = InputStream(input_text)
    
    # Create a lexer for the input
    lexer = PythonParserLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    # Create a parser for the token stream
    parser = PythonParserParser(token_stream)

    tree = parser.start()  # Parse the 'start' rule
    
    # Print the parse tree (or process it as needed)
    print(tree.toStringTree(recog=parser))  # Display the parse tree in text form

if __name__ == '__main__':
    # Path to the input file to parse
    input_file = sys.argv[1] if len(sys.argv) > 1 else "project_deliverable_2.py"
    main(input_file)
