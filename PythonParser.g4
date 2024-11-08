grammar PythonParser;

expr
    : expr '**' expr         # Power
    | expr '*' expr          # Multiply
    | expr '/' expr          # Divide
    | expr '+' expr          # Add
    | expr '-' expr          # Subtract
    | '(' expr ')'           # Parentheses
    | NUMBER                 # Number
    | STRING                         # StringLiteral
    | expr '%' expr          # Mod
    | expr ASSIGN_OP  expr   # Assignment
    | array                  # Arrays
    | arrayLiteral           # ArrayLiterals
    ;

array 
    : ID '[' expr ']' # ArrayIndex
    | ID ASSIGN_OP '[' expr (',' expr)* ']' # ArrayAssign
    ; 

arrayLiteral
    : '[' expr (',' expr)* ']'       # ArrayLiteral2
    ;

ASSIGN_OP : '=' | '+=' | '-=' | '*=' | '/=';
ID        : [a-zA-Z_][a-zA-Z_0-9]* ;
STRING    : '\'' [a-zA-Z_0-9]+ '\'' ; 
NUMBER : [0-9]+ ('.' [0-9]+)? ;
WS : [ \t\r\n]+ -> skip ;