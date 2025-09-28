# tokens.py — CWE-Compiler Token Definitions with metadata

class TokenType:
    # Program Entry
    MAIN = "MAIN"

    # Functions
    FUNC_DEF = "FUNC_DEF"
    RETURN = "RETURN"

    # Variables
    VAR = "VAR"
    IDENTIFIER = "IDENTIFIER"

    # Literals
    NUMBER = "NUMBER"
    FLOAT = "FLOAT"
    STRING = "STRING"
    CHAR = "CHAR"
    NULL = "NULL"

    # I/O
    PRINT = "PRINT"
    INPUT = "INPUT"

    # Conditionals
    IF = "IF"
    ELSE = "ELSE"
    ELSEIF = "ELSEIF"
    SWITCH = "SWITCH"
    CASE = "CASE"
    DEFAULT = "DEFAULT"

    # Loops
    WHILE = "WHILE"
    FOR = "FOR"
    BREAK = "BREAK"
    CONTINUE = "CONTINUE"

    # Operators
    PLUS = "PLUS"
    MINUS = "MINUS"
    TIMES = "TIMES"
    DIVIDE = "DIVIDE"
    MOD = "MOD"
    POW = "POW"
    ASSIGN = "ASSIGN"

    # Compound Assignments
    PLUS_ASSIGN = "PLUS_ASSIGN"
    MINUS_ASSIGN = "MINUS_ASSIGN"
    TIMES_ASSIGN = "TIMES_ASSIGN"
    DIV_ASSIGN = "DIV_ASSIGN"

    # Comparison
    EQ = "EQ"
    NEQ = "NEQ"
    GT = "GT"
    LT = "LT"
    GTE = "GTE"
    LTE = "LTE"

    # Boolean
    TRUE = "TRUE"
    FALSE = "FALSE"

    # Logical
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    XOR = "XOR"

    # Bitwise
    BIT_AND = "BIT_AND"
    BIT_OR = "BIT_OR"
    BIT_XOR = "BIT_XOR"
    SHIFT_LEFT = "SHIFT_LEFT"
    SHIFT_RIGHT = "SHIFT_RIGHT"

    # Unary
    INC = "INC"
    DEC = "DEC"

    # Arrays / Lists
    LIST_START = "LIST_START"
    LIST_END = "LIST_END"
    LIST_APPEND = "LIST_APPEND"
    INDEX = "INDEX"
    LENGTH = "LENGTH"

    # Built-ins
    RANGE = "RANGE"

    # Error / Exception
    THROW = "THROW"
    UNKNOWN = "UNKNOWN"  # For unmapped/invalid tokens
    EOF = "EOF"

    # Blocks
    END = "END"

    # Comments
    COMMENT = "COMMENT"

    # Symbols
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    SEMICOLON = "SEMICOLON"
    COMMA = "COMMA"
    QUESTION = "QUESTION"
    COLON = "COLON"
    DOT = "DOT"
    BACKSLASH = "BACKSLASH"

    # Formatting
    NEWLINE = "NEWLINE"
    WHITESPACE = "WHITESPACE"


class Token:
    def __init__(self, type_, value=None, line=None, column=None):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        if self.value is not None:
            return f"Token({self.type}, {self.value}, {self.line}:{self.column})"
        return f"Token({self.type})"


# Dual Mapping: Emoji + Text → TokenType
TOKEN_MAP = {
    # Program Entry
    "🚀": TokenType.MAIN, "main": TokenType.MAIN, "👋": TokenType.MAIN,

    # Function Definition
    "🛠": TokenType.FUNC_DEF, "vibe": TokenType.FUNC_DEF,

    # Return
    "🎁": TokenType.RETURN, "back": TokenType.RETURN,

    # Variables
    "😀": TokenType.VAR, "let": TokenType.VAR, "🔤": TokenType.VAR,

    # I/O
    "🖨": TokenType.PRINT, "📢": TokenType.PRINT, "say": TokenType.PRINT, "shout": TokenType.PRINT,
    "📥": TokenType.INPUT, "gimme": TokenType.INPUT, "grab": TokenType.INPUT,

    # Conditionals
    "❓": TokenType.IF, "fr": TokenType.IF,
    "🤔": TokenType.ELSE, "elsee": TokenType.ELSE,
    "❓➕": TokenType.ELSEIF, "❔": TokenType.ELSEIF, "mid": TokenType.ELSEIF,
    "🎚": TokenType.SWITCH, "switchup": TokenType.SWITCH,
    "➡️": TokenType.CASE, "casez": TokenType.CASE,
    "🚪": TokenType.DEFAULT, "defaultz": TokenType.DEFAULT,

    # Loops
    "🔁": TokenType.WHILE, "bet": TokenType.WHILE,
    "🔂": TokenType.FOR, "loopin": TokenType.FOR,
    "🛑": TokenType.BREAK, "bruh-stop": TokenType.BREAK,
    "⏭": TokenType.CONTINUE, "keep-goin": TokenType.CONTINUE,

    # Operators
    "➕": TokenType.PLUS, "plus": TokenType.PLUS,
    "➖": TokenType.MINUS, "minus": TokenType.MINUS,
    "✖": TokenType.TIMES, "times": TokenType.TIMES,
    "➗": TokenType.DIVIDE, "div": TokenType.DIVIDE,
    "%": TokenType.MOD, "modz": TokenType.MOD,
    "^": TokenType.POW, "powah": TokenType.POW,   # keep ^ for power
    "=": TokenType.ASSIGN, "📌": TokenType.ASSIGN,

    # Compound Assignments
    "+=": TokenType.PLUS_ASSIGN, "-=": TokenType.MINUS_ASSIGN,
    "*=": TokenType.TIMES_ASSIGN, "/=": TokenType.DIV_ASSIGN,
    "➕=": TokenType.PLUS_ASSIGN, "➖=": TokenType.MINUS_ASSIGN,
    "✖=": TokenType.TIMES_ASSIGN, "➗=": TokenType.DIV_ASSIGN,

    # Comparison (emoji + raw)
    "⚖": TokenType.EQ, "same": TokenType.EQ, "==": TokenType.EQ,
    "🙅": TokenType.NEQ, "nah": TokenType.NEQ, "!=": TokenType.NEQ,
    "🔼": TokenType.GT, "big": TokenType.GT, ">": TokenType.GT,
    "🔽": TokenType.LT, "smol": TokenType.LT, "<": TokenType.LT,
    "🔼=": TokenType.GTE, "big-eq": TokenType.GTE, ">=": TokenType.GTE,
    "🔽=": TokenType.LTE, "smol-eq": TokenType.LTE, "<=": TokenType.LTE,

    # Boolean
    "✅": TokenType.TRUE, "yeet": TokenType.TRUE,
    "❌": TokenType.FALSE, "sus": TokenType.FALSE,
    "🚫": TokenType.NULL, "voidz": TokenType.NULL,

    # Logical (emoji + raw)
    "🟰": TokenType.AND, "fam": TokenType.AND, "&&": TokenType.AND,
    "⭕": TokenType.OR, "maybe": TokenType.OR, "||": TokenType.OR,
    "❎": TokenType.NOT, "nope": TokenType.NOT, "!": TokenType.NOT,
    "✖⭕": TokenType.XOR, "alt": TokenType.XOR, "^^": TokenType.XOR,

    # Bitwise
    "&": TokenType.BIT_AND,
    "|": TokenType.BIT_OR,
    "^^^": TokenType.BIT_XOR,  # distinct from power
    "<<": TokenType.SHIFT_LEFT,
    ">>": TokenType.SHIFT_RIGHT,

    # Unary
    "🔼+": TokenType.INC, "up-it": TokenType.INC, "++": TokenType.INC,
    "🔽-": TokenType.DEC, "down-it": TokenType.DEC, "--": TokenType.DEC,

    # Arrays / Lists
    "[": TokenType.LIST_START, "squad": TokenType.LIST_START,
    "]": TokenType.LIST_END, "squad-end": TokenType.LIST_END,
    "➕📦": TokenType.LIST_APPEND, "add2squad": TokenType.LIST_APPEND,
    "🔍": TokenType.INDEX, "peek": TokenType.INDEX,
    "📏": TokenType.LENGTH, "howlong": TokenType.LENGTH,

    # Built-ins
    "🔢": TokenType.RANGE, "looprange": TokenType.RANGE,

    # Error / Exception
    "⚠": TokenType.THROW, "oops": TokenType.THROW,

    # Blocks
    "🔚": TokenType.END, "donezo": TokenType.END,

    # Comments
    "📝": TokenType.COMMENT, "//": TokenType.COMMENT, "cap": TokenType.COMMENT,

    # Symbols
    "(": TokenType.LPAREN, ")": TokenType.RPAREN,
    "{": TokenType.LBRACE, "}": TokenType.RBRACE,
    ";": TokenType.SEMICOLON, ",": TokenType.COMMA,
    "?": TokenType.QUESTION, ":": TokenType.COLON,
    ".": TokenType.DOT, "\\": TokenType.BACKSLASH
}
