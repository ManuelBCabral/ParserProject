grammar PythonParser;

expr
    : expr '**' expr         # Power
    | expr '*' expr          # Multiply
    | expr '/' expr          # Divide
    | expr '+' expr          # Add
    | expr '-' expr          # Subtract
    | '(' expr ')'           # Parentheses
    | NUMBER                 # Number
    | expr '%' expr          # Mod
    | expr ASSIGN_OP  expr   # Assignment
    ;

ASSIGN_OP : '=' | '+=' | '-=' | '*=' | '/=';
NUMBER : [0-9]+ ('.' [0-9]+)? ;
WS : [ \t\r\n]+ -> skip ;