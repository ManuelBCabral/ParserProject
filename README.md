Our project here is a parser for the Python Language, using context free grammars.

Our group consists of 5 members:
Johnathon Brumfield
Manuel Belaustegui-Cabral
Tin Duong
Jake Morgan
Joseph Mun

To run this project, you need to make sure to have Antlr4 downloaded according to canvas instructions.

If you are using python virtual enviorement:

- python or python3 -m venv venv
- source venv/bin/activate (on mac) or venv\Scripts\activate (on windows) // Activates virtual enviorement
- pip(/3) install -r requirements.txt // or maually install the antlr4 runtime on windows

To compile your antlr parser and lexer you must run

antlr4 -Dlanguage=Python3 PythonParser.g4 -o gen //to compile

You must then run

Python3 .\parser.py "input" // This is to test the input and tree of parser, it will print out the parse tree output

To test the parser with sample expressions:

1. **Prepare `expressions.txt`**: Ensure `expressions.txt` contains the expressions you want to test, with each expression on a new line.

2. Run test_parser.py: Use the following command to parse each expression in expressions.txt and print the corresponding parse tree
python3 test_parser.py expressions.txt
