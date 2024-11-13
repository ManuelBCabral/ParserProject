grammar ParserProject;

// Start rule to handle multiple statements, each optionally ending with a semicolon
start: (statement SEMICOLON?)* EOF;

// Rule for statements, which can be an assignment, an expression, or an if/elif/else block
statement: assign | expr | ifStatement;

// Rule for assignments
assign: ID ASSIGN_OP (expr | arrayLiteral | TRUE | FALSE);

// Rule for arithmetic expressions and grouping, split from conditionExpr
expr: term ((ADD | SUB) term)*;

term: factor ((MUL | DIV | MOD) factor)*;

factor: LPAREN expr RPAREN  // Grouping with parentheses
    | NUMBER              // Number literal (including decimals)
    | STRING              // String literal
    | ID                  // Variable identifier
    | arrayLiteral;       // Array literal

// Rule for conditional expressions, allowing logical and comparison operations
conditionExpr: conditionTerm ((OR) conditionTerm)*;

conditionTerm: conditionFactor ((AND) conditionFactor)*;

conditionFactor: NOT conditionFactor                       // Unary 'not' operator
    | expr comparisonOp expr                    // Comparison expressions (e.g., a < b)
    | LPAREN conditionExpr RPAREN;              // Grouping for logical expressions

// Comparison operators
comparisonOp: LT | LE | GT | GE | EQ | NE;

// Rule for if/elif/else statements
ifStatement: IF conditionExpr COLON statementBlock         // Basic if statement
    ( ELIF conditionExpr COLON statementBlock )*    // Optional elif branches
    ( ELSE COLON statementBlock )?                  // Optional else branch
    ;

// Block of statements following a conditional (using braces for simplicity)
statementBlock: LBRACE (statement SEMICOLON?)* RBRACE;     // Using braces to define blocks

// Array literals with recursive expressions
arrayLiteral: LBRACKET expr (COMMA expr)* RBRACKET;

// Assignment operators
ASSIGN_OP: '=' | '+=' | '-=' | '*=' | '/=';

// Lexer rules for various symbols and keywords
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
TRUE: 'True';
FALSE: 'False';
NOT: '!';
AND: '&&';
OR: '||';

// Arithmetic operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

// Comparison operators
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';
EQ: '==';
NE: '!=';

// Punctuation
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';
COLON: ':';
COMMA: ',';
SEMICOLON: ';';

// Identifiers
ID: [a-zA-Z_][a-zA-Z_0-9]*;

// String literals (supports both single and double quotes)
STRING: '\'' .*? '\'' | '"' .*? '"';

// Number literals (supports integers and floats)
NUMBER: [0-9]+ ('.' [0-9]+)?;

// Whitespace (ignored)
WS: [ \t\r\n]+ -> skip;
