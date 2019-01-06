# Operators
PLUS = '+'
MINUS = '-'
MUL = '*'
DIV = '/'
FLOORDIV = '//'
MOD = '%'
POWER = '^'
ARITHMATIC_LEFT_SHIFT = '<<<'
ARITHMATIC_RIGHT_SHIFT = '>>>'
XOR = 'xor'
BINARY_ONES_COMPLIMENT = '~'
BINARY_LEFT_SHIFT = '<<'
BINARY_RIGHT_SHIFT = '>>'
AND = 'and'
OR = 'or'
NOT = 'not'
IN = 'in'  # TODO
NOT_IN = 'not in'  # TODO
IS = 'is'
IS_NOT = 'is not'
LPAREN = '('
RPAREN = ')'
LSQUAREBRACKET = '['
RSQUAREBRACKET = ']'
LCURLYBRACKET = '{'
RCURLYBRACKET = '}'
COMMA = ','
COLON = ':'
DOT = '.'
RANGE = '..'
ELLIPSIS = '...'  # TODO
ARROW = '->'
CAST = 'as'
ASSIGN = '='
PLUS_ASSIGN = '+='
MINUS_ASSIGN = '-='
MUL_ASSIGN = '*='
DIV_ASSIGN = '/='
FLOORDIV_ASSIGN = '//='
MOD_ASSIGN = '%='
POWER_ASSIGN = '^='
PLUS_PLUS = '++'
MINUS_MINUS = '--'
EQUALS = '=='
NOT_BANG = '!'
NOT_EQUALS = '!='
LESS_THAN = '<'
GREATER_THAN = '>'
LESS_THAN_OR_EQUAL_TO = '<='
GREATER_THAN_OR_EQUAL_TO = '>='
DECORATOR = '@'  # TODO

# Types
ANY = 'any'
INT = 'int'
INT8 = 'int8'
INT16 = 'int16'
INT32 = 'int32'
INT64 = 'int64'  # same as int but doesn't automatically promote to larger integer type upon overflow
INT128 = 'int128'
UINT = 'uint'
UINT8 = 'uint8'
UINT16 = 'uint16'
UINT32 = 'uint32'
UINT64 = 'uint64'
UINT128 = 'uint128'
DOUBLE = 'double'
FLOAT = 'float'
COMPLEX = 'complex'  # TODO
STR = 'str'
BOOL = 'bool'
LIST = 'list'
TUPLE = 'tuple'
SET = 'set'  # TODO
DICT = 'dict'
ENUM = 'enum'  # TODO
FUNC = 'func'
STRUCT = 'struct'
CLASS = 'class'

# Contstants
TRUE = 'true'
FALSE = 'false'
NULL = 'null'  # TODO

# Keywords
IF = 'if'
ELSE_IF = 'else if'
ELSE = 'else'
FOR = 'for'
WHILE = 'while'
SWITCH = 'switch'
CASE = 'case'
DEFAULT = 'default'
OPERATOR = 'operator'
EXTERN = 'extern'
DEF = 'def'
CONST = 'const'
NEW = 'new'  # TODO
SUPER = 'super'  # TODO
THIS = 'this'  # TODO
RETURN = 'return'
TRY = 'try'  # TODO
CATCH = 'catch'  # TODO
THROW = 'throw'  # TODO
FINALLY = 'finally'  # TODO
YIELD = 'yield'  # TODO
BREAK = 'break'
FALLTHROUGH = 'fallthrough'
DEFER = 'defer'
CONTINUE = 'continue'
DEL = 'del'  # TODO
FROM = 'from'  # TODO
IMPORT = 'import'  # TODO
WILDCARD = '*'  # TODO
WITH = 'with'  # TODO
PASS = 'pass'
VOID = 'void'
ALIAS = 'alias'
OVERRIDE = 'override'  # TODO
ABSTRACT = 'abstract'  # TODO
ASSERT = 'assert'  # TODO

ARITHMETIC_OP = (PLUS, MINUS, MUL, DIV, MOD, FLOORDIV, POWER, ARITHMATIC_LEFT_SHIFT, ARITHMATIC_RIGHT_SHIFT)

ASSIGNMENT_OP = (ASSIGN, PLUS_ASSIGN, MINUS_ASSIGN, MUL_ASSIGN, DIV_ASSIGN, FLOORDIV_ASSIGN, MOD_ASSIGN, POWER_ASSIGN, PLUS_PLUS, MINUS_MINUS)

ARITHMETIC_ASSIGNMENT_OP = (PLUS_ASSIGN, MINUS_ASSIGN, MUL_ASSIGN, DIV_ASSIGN, FLOORDIV_ASSIGN, MOD_ASSIGN, POWER_ASSIGN)

INCREMENTAL_ASSIGNMENT_OP = (PLUS_PLUS, MINUS_MINUS)

COMPARISON_OP = (EQUALS, NOT_BANG, NOT_EQUALS, LESS_THAN, GREATER_THAN, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO, IS, IS_NOT)

LOGICAL_OP = (AND, OR, NOT)

BINARY_OP = (XOR, BINARY_ONES_COMPLIMENT, BINARY_LEFT_SHIFT, BINARY_RIGHT_SHIFT)

MEMBERSHIP_OP = (IN, NOT_IN)

MULTI_WORD_OPERATORS = (IS, IS_NOT, IN, NOT_IN, NOT)

OPERATORS = (
    LPAREN, RPAREN, LSQUAREBRACKET, RSQUAREBRACKET, LCURLYBRACKET, RCURLYBRACKET,
    ARROW, COMMA, COLON, DOT, DECORATOR, CAST, RANGE, ELLIPSIS,
) + ARITHMETIC_OP + ASSIGNMENT_OP + COMPARISON_OP + LOGICAL_OP + BINARY_OP + MEMBERSHIP_OP

SINGLE_OPERATORS = (
    LPAREN, RPAREN, LSQUAREBRACKET, RSQUAREBRACKET, LCURLYBRACKET, RCURLYBRACKET,
    BINARY_ONES_COMPLIMENT, COMMA, DECORATOR
)

KEYWORDS = (
    IF, ELSE, WHILE, FOR, SWITCH, CASE, DEF, SUPER, THIS, RETURN, TRY, CATCH, THROW,
    FINALLY, YIELD, BREAK, CONTINUE, DEL, IMPORT, FROM, WITH, PASS, VOID,
    CONST, OVERRIDE, ABSTRACT, ASSERT, DEFAULT, NEW, ALIAS, FALLTHROUGH,
    DEFER
)

MULTI_WORD_KEYWORDS = (IF, ELSE, ELSE_IF)

TYPES = (ANY, INT, INT8, INT16, INT32, INT64, INT128, UINT, UINT8, UINT16, UINT32, UINT64, UINT128, DOUBLE, FLOAT, COMPLEX, STR, BOOL, LIST, TUPLE, DICT, ENUM, FUNC, STRUCT, CLASS)

CONSTANTS = (TRUE, FALSE, NULL)

PRINT = 'print'
INPUT = 'input'

BUILTIN_FUNCTIONS = (PRINT, INPUT)

# For Lexer
TYPE = 'TYPE'
NUMBER = 'NUMBER'
STRING = 'STRING'
OP = 'OP'
CONSTANT = 'CONSTANT'
NEWLINE = 'NEWLINE'
INDENT = 'INDENT'
KEYWORD = 'KEYWORD'
ANON = 'ANON'
NAME = 'NAME'
EOF = 'EOF'
ALPHANUMERIC = 'alphanumeric'
NUMERIC = 'numeric'
OPERATIC = 'operatic'
WHITESPACE = 'whitespace'
COMMENT = 'comment'
ESCAPE = 'escape'
