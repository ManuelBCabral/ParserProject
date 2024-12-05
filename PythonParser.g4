grammar PythonParser;

// Start rule to handle multiple statements
start: (statement)* EOF;

// Rules for different types of statements
statement:
	ifStatement
	| assignment
	| whileStatement
	| forStatement;

// Rules for different types of assignments
assignment:
	assignment ASSIGN_OP (assignment | arithmetic)
	| BOOL
	| VAR
	| NUM
	| CHAR
	| STRING
	| array;

// Rules for different types of arithmetic operations
arithmetic: arithmetic ARITH_OP arithmetic | VAR | NUM;

// Rules for different types of conditions
condition:
	condition ('and' | 'or') condition
	| condition COND_OP condition
	| 'not' condition
	| '(' condition ')'
	| VAR
	| NUM
	| BOOL;

// Rules for different types of if statements
ifStatement:
	'if' '('? condition ')'? ':' block+ (
		'elif' '('? condition ')'? ':' block+
	)* ('else' ':' block+)?;

whileStatement: 'while' '('? condition ')'? ':' block+;

forStatement:
	'for' VAR 'in' (
		loopStructure
		| ('range' '(' NUM (',' NUM)? ')')
	) ':' block+;

loopStructure: array | VAR;

block: statement;

// Rules for array literals
array: '[' (expr (',' expr)*)? ']';
expr: (CHAR | NUM | STRING);

// Operators
ARITH_OP: '+' | '-' | '*' | '/' | '%';
ASSIGN_OP: '=' | '+=' | '-=' | '*=' | '/=' | '%=' | '&=';
COND_OP: '==' | '!=' | '<' | '<=' | '>' | '>=';

// Tokens
NEWLINE: '/r'? '\n';

VAR: (CHAR | '_') (CHAR | NUM | '_')*;
CHAR: [a-zA-Z_];
NUM: [-]? [0-9]+ ('.' [0-9]+)?;
STRING:
	'"' ('\\' . | ~["\\])* '"'
	| '\'' ('\\' . | ~['\\])* '\'';
BOOL: 'True' | 'False';

// Whitespace (ignored)
WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
MULTICOMMENT: '"""' .*? '"""' -> skip;