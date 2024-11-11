grammar PythonParser;

// Start rule to distinguish assignments and expressions
start: assign | expr;

// Rule for assignments with specific options
assign: ID ASSIGN_OP (expr | arrayLiteral | TRUE | FALSE);

// Rule for expressions with arithmetic and grouping
expr: expr ('*' | '/' | '%' | '+' | '-') expr  // Arithmetic operations
    | '(' expr ')'                             // Grouping with parentheses
    | NUMBER                                   // Number literal
    | STRING                                   // String literal
    | ID                                       // Variable identifier
    | arrayLiteral;                            // Array literal

// Array literal with recursive expressions
arrayLiteral: '[' expr (',' expr)* ']';

// Assignment operators
ASSIGN_OP: '=' | '+=' | '-=' | '*=' | '/=';

// Identifiers
ID: [a-zA-Z_][a-zA-Z_0-9]*;

// String literals
STRING: '\'' [a-zA-Z_0-9]+ '\'' | '"' [a-zA-Z_0-9]+ '"';

// Number literals
NUMBER: [0-9]+ ('.' [0-9]+)?;

// Boolean literals
TRUE: 'True';
FALSE: 'False';

// Whitespace
WS: [ \t\r\n]+ -> skip;
