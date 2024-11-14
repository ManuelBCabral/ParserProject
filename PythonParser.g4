grammar PythonParser;

// Start rule to handle multiple statements
start: (statement)* EOF;

statement: ifStatement | assignment;

assignment: assignment ASSIGN_OP (assignment | arithmatic)
	| BOOL
	| VAR
	| NUM
	| CHAR
	| STRING
	| array;

arithmatic: arithmatic ARITH_OP arithmatic
	| VAR
	| NUM;

condition: condition ('and' | 'or') condition
	| condition COND_OP condition
	| 'not' condition
	| '(' condition ')'
	| VAR
	| NUM
	| BOOL;

ifStatement: 'if' '('? condition ')'? ':' (' ')* block+ ('elif' '('? condition ')'? ':' block+)* ('else' ':' block+)?;

block: TAB (statement)+;

array: '[' (expr (',' expr)*)? ']';

expr: (CHAR | NUM | STRING);

TAB: '\n    ';
VAR: (CHAR | '_') (CHAR | NUM | '_')*;
ARITH_OP: '+' | '-' | '*' | '/' | '%';
ASSIGN_OP: '=' | '+=' | '-=' | '*=' | '/=' | '%=' | '&=';
COND_OP: '==' | '!=' | '<' | '<=' | '>' | '>=';

CHAR: [a-zA-Z_];
NUM: [-]?[0-9]+ ('.' [0-9]+)?;
STRING: '"' ('\\' . | ~["\\])* '"' | '\'' ('\\' . | ~['\\])* '\'';
BOOL: 'True' | 'False';

// Whitespace (ignored)
WS: [\t\r\n]+ -> skip;