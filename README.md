# Python Language Parser

Our project is a parser for the Python Language using context-free grammars.

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
