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
- pip(/3) install -r requirements.txt // or maually install the antlr4 runtime on windows / mac

To compile your antlr parser and lexer you must run

antlr4 -Dlanguage=Python3 PythonParser.g4 -o gen //to compile

You must then run

Python3 \Parser.py // this runs the file it is given into the parser and creates the parse tree

To test the parser with sample expressions:

1. \*\*Prepare project_deliverable_2.py () contains the expressions you want to test, with each expression starting on a new line.

2. Run python (or python3 on mac) Parser.py after compiling the .g4 file: This command will display the parse tree for the expressions in the project_deliverable_2.py, another file can be used just have to run it as an arguement for the Parser.py file eg. python3 Parse.py <insert file name>
