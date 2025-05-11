// Файл: BasicCompiler/grammar/Basic.g4 (Без REM_MODE)
grammar Basic;

// --- Лексер ---

// Определяем WS и комментарии в начале, чтобы они обрабатывались первыми
NEWLINE: ('\r'? '\n');       // Одиночный перевод строки
WS: [ \t]+ -> skip;           // Пробелы и табы (пропускаем)
REM_COMMENT: 'REM' (~[\r\n])* NEWLINE -> skip; // Комментарии REM пропускаем
APOSTROPHE_COMMENT: '\'' (~[\r\n])* -> skip;   // Комментарии с апострофом (') пропускаем

// Ключевые слова (без строгого требования пробелов)
IF: 'IF';
THEN: 'THEN';
ELSE: 'ELSE';

// Остальные ключевые слова
PRINT: 'PRINT';
LET: 'LET';
END: 'END';
GOTO: 'GOTO';
FOR: 'FOR';
TO: 'TO';
STEP: 'STEP';
NEXT: 'NEXT';
GOSUB: 'GOSUB';
RETURN: 'RETURN';
WHILE: 'WHILE';
WEND: 'WEND';
INPUT: 'INPUT';

// Идентификаторы и литералы
ID: [a-zA-Z_] [a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;  // Целые и дробные числа
STRING: '"' (~["\r\n"])*? '"'; // Строка не может содержать " или перевод строки

// Операторы и специальные символы
ASSIGN: '='; // Используется для LET
EQ: '=';     // Используется для сравнения. Парсер решает по контексту.
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
NEQ: '<>';    // Не равно

PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';

LPAREN: '(';
RPAREN: ')';

COLON: ':';     // Для меток типа MYLABEL:
COMMA: ',';     // Для списка выражений в PRINT, переменных в INPUT/NEXT
SEMICOLON: ';'; // Для списка выражений в PRINT (печать вплотную)

TYPE_SUFFIX: '$' | '!' | '%'; // Суффиксы типов

// --- Парсер ---
program
    : (lineContent? NEWLINE)* (lineContent? EOF) // Позволяет пустые строки и необязательный NEWLINE в конце
    ;

lineContent
    : (labelDef | (NUMBER? statement?)) // Строка: метка ИЛИ (необязательный номер + необязательная инструкция)
    ;

labelDef: ID COLON; // Метка в виде ИМЯ: (например, MYLOOP:)

statement:
    printStmt
    | letStmt
    | ifStmt
    | gotoStmt
    | forStmt
    | nextStmt
    | gosubStmt
    | returnStmt
    | whileStmt
    | inputStmt
    | endStmt
    ;

printStmt: PRINT expressionList?;
expressionList: expression ( (COMMA | SEMICOLON) expression )*;

letStmt: LET variable ASSIGN expression;
ifStmt: IF WS? condition WS? THEN WS? statement (ELSE WS? statement)?;
gotoStmt: GOTO targetLabel;
forStmt: FOR variable ASSIGN expression TO expression (STEP expression)?; // ASSIGN для начального значения
nextStmt: NEXT variable (COMMA variable)*;
gosubStmt: GOSUB targetLabel;
returnStmt: RETURN;
// Тело цикла WHILE - ноль или больше строк (lineContent NEWLINE) до WEND
whileStmt: WHILE condition (lineContent? NEWLINE)* WEND;
inputStmt: INPUT (STRING COMMA)? variable (COMMA variable)*;

targetLabel: ID | NUMBER; // Метка, на которую переходим, может быть именем или числом

endStmt: END;

variable: ID TYPE_SUFFIX?; // Переменная с необязательным суффиксом типа

condition: expression; // Условие - это просто выражение

expression
    : comparisonExpr
    ;

comparisonExpr
    : left=additiveExpr (op=(EQ|LT|GT|LTE|GTE|NEQ) right=additiveExpr)?
    ;

additiveExpr
    : left=multiplicativeExpr (op=(PLUS | MINUS) right=multiplicativeExpr )*
    ;

multiplicativeExpr
    : left=unaryExpr (op=(MUL | DIV) right=unaryExpr )*
    ;

unaryExpr
    : MINUS atom  // Унарный минус
    | atom
    ;

atom
    : NUMBER
    | STRING
    | variable
    | LPAREN expression RPAREN
    ;