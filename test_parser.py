import sys
from antlr4 import *
from gen.PythonParserLexer import PythonParserLexer
from gen.PythonParserParser import PythonParserParser

def parse_expression(input_text):
    # Convert input text into an ANTLR input stream
    input_stream = InputStream(input_text)
    
    # Create a lexer and parser
    lexer = PythonParserLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PythonParserParser(token_stream)
    
    # Parse using the `start` rule
    tree = parser.start()
    
    # Print the parse tree
    print(f"Expression: {input_text.strip()}")
    print(tree.toStringTree(recog=parser))
    print("-" * 40)

def main():
    if len(sys.argv) > 1:
        # Check if the input is a filename
        filename = sys.argv[1]
        try:
            # Open the file and read each line as an expression
            with open(filename, 'r') as file:
                for line in file:
                    # Skip empty lines
                    if line.strip():
                        parse_expression(line.strip())
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
    else:
        # Default expression if no file is provided
        input_text = "3 + 5 * (10 - 4)"
        parse_expression(input_text)

if __name__ == '__main__':
    main()
