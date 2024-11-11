grammar PythonParser;

// Start rule to handle multiple statements, each optionally ending with a semicolon
start: (statement ';'?)* EOF;

// Rule for statements, which can be an assignment or an expression
statement: assign | expr;

// Rule for assignments
assign: ID ASSIGN_OP (expr | arrayLiteral | TRUE | FALSE);

// Rule for arithmetic expressions and grouping
expr: expr ('*' | '/' | '%' | '+' | '-') expr    // Arithmetic operations
    | '(' expr ')'                               // Grouping with parentheses
    | NUMBER                                     // Number literal (including decimals)
    | STRING                                     // String literal
    | ID                                         // Variable identifier
    | arrayLiteral                               // Array literal
    ;

// Array literals with recursive expressions
arrayLiteral: '[' expr (',' expr)* ']';

// Assignment operators
ASSIGN_OP: '=' | '+=' | '-=' | '*=' | '/=';

// Identifiers
ID: [a-zA-Z_][a-zA-Z_0-9]*;

// String literals (supports both single and double quotes)
STRING: '\'' .*? '\'' | '"' .*? '"';

// Number literals (supports integers and floats)
NUMBER: [0-9]+ ('.' [0-9]+)?;

// Boolean literals
TRUE: 'True';
FALSE: 'False';

// Whitespace (ignored)
WS: [ \t\r\n]+ -> skip;
