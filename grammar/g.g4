grammar g;

// Parser rules
program: (line)* EOF;

line: assignment (COMMENT)? NL | expression (COMMENT)? NL | COMMENT NL | NL;

assignment
    : WORD '=:' expression        # assignmentLabel
    ;

expression
    // Atomic expressions (highest precedence)
    : atom                                                        # atomExpr
    | '_' atom                                                    # negativeExpr
    | '(' expression ')'                                          # parenExpr
    
    // Unary operations
    | ']' expression                                              # identityExpr
    | '#' expression                                              # sizeExpr
    | 'i.' expression                                             # seqExpr
    | op=('+' | '-' | '*' | '%' | '|' | '^' | '>' | '<' | '>=' | '<=' | '=' | '<>') ':' expression  # modifiedExpr
    | op=('+' | '-' | '*' | '%' | '|' | '^' | '>' | '<' | '>=' | '<=' | '=' | '<>') '/' expression  # foldlExpr

    // Binary operations
    | <assoc=right> expression op=('+' | '-' | '*' | '%' | '|' | '^') expression     # binaryExpr
    | expression op=('+' | '-' | '*' | '%' | '|' | '^') '~' expression               # flippedBinaryExpr
    | <assoc=right> expression op=(',' | '{' | '#') expression                       # specialBinaryExpr
    | <assoc=right> expression op=('>' | '<' | '>=' | '<=' | '=' | '<>') expression  # relationalExpr
    
    // Function application
    | WORD expression                                             # functionCallExpr
    
    // Composition (lowest precedence, but right-associative)
    | <assoc=right> expression '@:' expression                    # composeExpr
    ;

atom
    : (INT | NEG_INT)+                                            # listAtom
    | WORD                                                        # variableAtom
    | ']'                                                         # identityFuncExpr
    | '#'                                                         # sizeFuncExpr
    | 'i.'                                                        # seqFuncExpr
    | op=('+' | '-' | '*' | '%' | '|' | '^' | '>' | '<' | '>=' | '<=' | '=' | '<>') ':'        # modifiedFuncExpr
    | op=('+' | '-' | '*' | '%' | '|' | '^' | '>' | '<' | '>=' | '<=' | '=' | '<>') '/'        # foldlFuncExpr
    ;

// Lexer rules
INT: [0-9]+;
NEG_INT: '_' [0-9]+;
WORD : [a-zA-Z] [a-zA-Z0-9_]* ;
WS: [ \t]+ -> skip;
NL: '\r'? '\n';
COMMENT: 'NB.' ~[\r\n]* -> skip;