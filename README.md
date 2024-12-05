# Python Language Parser

Our project aims to create a parser for the Python programming language using ANTLR4 a parser generator.

Throughout the code, we use ANTLR4 to create CFG's (Context-Free-Grammars) that define the syntax rules for valid Python expressions.

We then use that ANTLR4 grammar to create a parse tree to visually represent the code structure it implements.

## Features Supported

### Statement Types

1. Assignment Statements
2. If Statements
3. While Loops
4. For Loops
5. Nested Statements

### Other

1. Artihmetic Expressions
2. Operators
3. Conditionals

## Team Members

- Johnathon Brumfield
- Manuel Belaustegui-Cabral
- Tin Duong
- Jake Morgan
- Joseph Mun

## Setup Instructions

### Prerequisites

Ensure you have Antlr4 downloaded according to Canvas instructions.

### Virtual Environment

If you are using a Python virtual environment:

1. Create the virtual environment:
   ```sh
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On macOS:
     ```sh
     source venv/bin/activate
     ```
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   Alternatively, manually install the Antlr4 runtime.

## Compilation and Execution

### Compile the ANTLR Parser and Lexer

```sh
antlr4 -Dlanguage=Python3 PythonParser.g4 -o gen
```

### Run the Parser

```sh
python3 Parser.py
```

This command runs the file given to the parser and creates the parse tree.

## Testing the Parser

### Prepare Test File

1. Create a file named `project_deliverable_x.py` containing the expressions you want to test.

### Run the Test

2. After compiling the `.g4` file, run:
   ```sh
   python3 Parser.py <insert file name>
   ```
   This command will display the parse tree for the expressions in the specified file. Alternatively, you can change the file being tested by modifying line 28 in `Parser.py`.
