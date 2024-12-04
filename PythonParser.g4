grammar PythonParser;

// Start rule for multiple statements
start: (statement NEWLINE)* EOF;

// Rules for statements
statement: assignment
         | arithmetic
         | arrayAssignment
         | ifStatement
         | whileStatement
         | forStatement
         | VAR ASSIGN_OP expr; // Additional expressions for generality

// Rules for assignments
assignment: VAR ASSIGN_OP (STRING | NUM | BOOL | VAR | arithmetic | arrayAssignment);

// Rules for arithmetic operations
arithmetic: arithmetic ARITH_OP arithmetic
          | VAR
          | NUM;

// Rules for arrays
arrayAssignment: VAR ASSIGN_OP '[' (expr (',' expr)*)? ']';

// Rules for expressions
expr: STRING
    | NUM
    | BOOL
    | VAR;

// Rules for conditions
condition: condition ('and' | 'or') condition
         | 'not' condition
         | '(' condition ')'
         | VAR COND_OP VAR
         | VAR COND_OP NUM
         | VAR COND_OP BOOL
         | NUM COND_OP NUM
         | BOOL;

// Rules for if-elif-else statements
ifStatement: 'if' condition ':' block
           ('elif' condition ':' block)*
           ('else' ':' block)?;

// Rules for while statements
whileStatement: 'while' condition ':' block;

// Rules for for loops
forStatement: 'for' VAR 'in' (RANGE | VAR) ':' block;

// Rules for blocks
block: INDENT statement+ DEDENT;

// Operators
ARITH_OP: '+' | '-' | '*' | '/' | '%';
ASSIGN_OP: '=' | '+=' | '-=' | '*=' | '/=' | '%=';
COND_OP: '==' | '!=' | '<' | '<=' | '>' | '>=';

// Tokens
VAR: [a-zA-Z_] [a-zA-Z_0-9]*;
NUM: '-'? [0-9]+ ('.' [0-9]+)?;
STRING: '"' ('\\' . | ~["\\])* '"' | '\'' ('\\' . | ~['\\])* '\'';
BOOL: 'True' | 'False';
RANGE: 'range(' NUM ',' NUM ')';

// Handling newlines and indentation
NEWLINE: '\r'? '\n'; // Handles both Unix and Windows line endings
WS: [ \t]+ -> skip; // Skips spaces and tabs

INDENT: NEWLINE {indentLevel++}; // Track increased indentation
DEDENT: NEWLINE {indentLevel--}; // Track decreased indentation

// Ignore comments
COMMENT: '#' ~[\r\n]* -> skip;
MULTICOMMENT: '\'\'\'' .*? '\'\'\'' -> skip;
