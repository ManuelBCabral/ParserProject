grammar PythonParser;


// Start rule for the parser //
start
		: (statement)* EOF;

// Statement rules //
statement
		:	expression
		|	indentedStatement
		;

indentedStatement: INDENT* (ifStatement | whileStatement | forStatement);

// If statement and elif/else helpers //
ifStatement
		:	'if' expression (COND_OP expression)* ':'
			(INDENT* statement)+ 
			(elif)* (else)?
		;

elif
		:	INDENT* 'elif' expression (COND_OP expression)* ':' 
			(INDENT* statement)+ 
		;

else
		:	INDENT* 'else' ':' (INDENT* statement)+
		;


// For and while loop //	
forStatement
		:	'for' VAR 'in' (
			VAR 
			| ('range(' NUMBER ',' NUMBER ')')
			) ':' (INDENT* statement)+
		;

whileStatement
		:	'while' expression (COND_OP expression)* ':' 
			(INDENT* statement)+
		;

// Expression rules //
expression
		:   (arithmatic | VAR) (ASSGN_OP | COND_OP) (arithmatic | VAR)          
		|   COND_OP VAR   
		|   BOOL        
		|   '(' expression ')'                               
		;

// Arithmatic operation rules //
arithmatic
		:	arithmatic ARITH_OP arithmatic
		|   (NUMBER | STRING | ARRAY | BOOL | VAR)
		;


// Operators //
ARITH_OP: '*'| '/'| '%'| '+'| '-' ;
ASSGN_OP: '=' | '+=' | '-=' | '*=' | '/=' ;
COND_OP : '<'| '<=' | '>' | '>=' | '==' | '!=' | 'and'  | 'or'  | 'not';


// Token rules //
BOOL    : ('True' | 'False');
VAR     : [a-zA-Z_] [a-zA-Z_0-9]* ;
NUMBER  : '-'? [0-9]+ ('.' [0-9]+)? ;
STRING  : (('"') ( ~["\r\n] )* ('"')) | (('\'') (~['\r\n])* ('\''));
ARRAY   : '[' (NUMBER | STRING) (', ' (NUMBER | STRING))* ']';

// Comment rules //
COMMENT : (('#' ~[\r\n]*) | '\'\'\'' VAR*.*? '\'\'\'') -> skip;

// Whitespace rules //
INDENT  : '\t'; 
NEWLINE : '\r' ? '\n' -> skip;
WS      : [ \t]+ -> skip;