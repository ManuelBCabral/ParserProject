grammar PythonParser;

// Start rule to handle multiple statements, each optionally ending with a semicolon
start: (statement COLON?)* EOF;

// Rule for statements, which can be an assignment or an expression or if statement
statement: assign | expr | ifStatement;

// Rule for assignments
assign: ID ASSIGN_OP (expr | arrayLiteral | TRUE | FALSE);

//Rule for if/elif/else statements
ifStatement:
	IF conditionBlock block COLON (
		ELIF conditionBlock COLON block
	)* (ELSE COLON* block)?;

//Condition block for if/elif statements
conditionBlock: expr;

//Code block, allows multiple statements within braces block: statement | '{' (statement ';'?)* '}';
block: '{' statement* '}' | statement+;

// Rule for arithmetic expressions and grouping
expr:
	expr ('*' | '/' | '%' | '+' | '-') expr // Arithmetic operations
	| expr ('<' | '<=' | '>' | '>=' | '==' | '!=') expr // Comparison operations
	| expr (AND | OR) expr // Logical and/or operations
	| NOT expr // Logical not
	| '(' expr ')' // Grouping with parentheses
	| NUMBER // Number literal (including decimals)
	| STRING // String literal
	| ID // Variable identifier
	| arrayLiteral; // Array literal

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

// Keywords
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
AND: 'and';
OR: 'or';
NOT: 'not';
COLON: ':';

// Whitespace (ignored)
WS: [ \t\r\n]+ -> skip;