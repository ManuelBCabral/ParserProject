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
    ;

NUMBER : [0-9]+ ('.' [0-9]+)? ;
WS : [ \t\r\n]+ -> skip ;