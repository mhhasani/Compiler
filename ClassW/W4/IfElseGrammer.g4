grammar IfElseGrammer;

// Define the structure of an if statement.
if_statement: 'if' '(' condition=expression ')' true_branch=statement ('else' false_branch=statement)?;

// Define the structure of a statement.
statement: assignment_statement | if_statement;

// Define the structure of an expression.
expression: additive_expression (comparison_operator additive_expression)?;

// Define the structure of an additive expression.
additive_expression: VARIABLE | NUMBER | additive_expression (ADDITIVEOPERATOR) additive_expression;

// Define the structure of an assignment statement.
assignment_statement: VARIABLE '=' additive_expression;

// Define the structure of a comparison operator.
comparison_operator: '<' | '<=' | '>' | '>=' | '==' | '!=';

// Define the structure of a variable.
VARIABLE: [a-zA-Z];

// Define the structure of a number.
NUMBER: [0-9]+;

// Define the structure of an additive operator.
ADDITIVEOPERATOR: '+' | '-' | '*';

// Define the structure of white space, which is skipped during parsing.
WS: [ \t\r\n]+ -> channel(HIDDEN);
