grammar PythonParser;

start:
	assign
	| expr; // assignment which is x = expression or simple without assignment

assign: ID ASSIGN_OP (expr | 'True' | 'False');
// seperate assignment rule for var = expression or bool value

expr:
	expr ASSIGN_OP expr
	| expr ('*' | '/' | '%' | '+' | '-') expr //changed to handle all of the arethmic in one case
	| '(' expr ')'
	| (
		NUMBER
		| STRING
	) //Num or String case for simple or assign case
	| ID
	| arrayLiteral; //recursively calling this will build a list 

arrayLiteral: '[' expr (',' expr)* ']';
//Allows for one or more and expr can be recursive into NUM and String into list seperated by commas

ASSIGN_OP: '=' | '+=' | '-=' | '*=' | '/='; //Assign operators

ID:
	[a-zA-Z_][a-zA-Z_0-9]*; //Define ID must start with a letter or underscore 

STRING: '\'' [a-zA-Z_0-9]+ '\''; //Define String

NUMBER: [0-9]+ ('.' [0-9]+)*; //Define Number

WS: [ \t\r\n]+ -> skip; //Define whitespace to skip