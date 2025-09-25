# tokens.py
# CWE-Compiler Token Definitions with metadata

class TokenType:
    # Program Entry
    MAIN = "MAIN"

    # Variables
    VAR = "VAR"

    # I/O
    PRINT = "PRINT"
    INPUT = "INPUT"

    # Conditionals
    IF = "IF"
    ELSE = "ELSE"
    ELSEIF = "ELSEIF"

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
    ASSIGN = "ASSIGN"

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

    # Unary
    INC = "INC"
    DEC = "DEC"

    # Arrays / Lists
    LIST_START = "LIST_START"
    LIST_END = "LIST_END"
    LIST_APPEND = "LIST_APPEND"
    INDEX = "INDEX"
    LENGTH = "LENGTH"

    # Functions
    FUNC_DEF = "FUNC_DEF"
    RETURN = "RETURN"

    # Built-ins
    RANGE = "RANGE"

    # Error / Exception
    THROW = "THROW"

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


# Token class with metadata
class Token:
    def __init__(self, type_, value=None, line=None, column=None):
        self.type = type_       # TokenType string
        self.value = value      # Actual text or emoji
        self.line = line        # Line number in source
        self.column = column    # Column position

    def __repr__(self):
        if self.value is not None:
            return f"Token({self.type}, {self.value}, {self.line}:{self.column})"
        return f"Token({self.type})"


# Dual Mapping: Emoji + Gen Z Slang/Text → TokenType
TOKEN_MAP = {
    # Program Entry
    "🚀": TokenType.MAIN,
    "main": TokenType.MAIN,

    # Variables
    "😀": TokenType.VAR,
    "let": TokenType.VAR,

    # I/O
    "🖨": TokenType.PRINT,
    "say": TokenType.PRINT,
    "shout": TokenType.PRINT,
    "📥": TokenType.INPUT,
    "gimme": TokenType.INPUT,
    "grab": TokenType.INPUT,

    # Conditionals
    "❓": TokenType.IF,
    "fr": TokenType.IF,
    "🤔": TokenType.ELSE,
    "elsee": TokenType.ELSE,
    "❓➕": TokenType.ELSEIF,
    "mid": TokenType.ELSEIF,

    # Loops
    "🔁": TokenType.WHILE,
    "bet": TokenType.WHILE,
    "🔂": TokenType.FOR,
    "loopin": TokenType.FOR,
    "🛑": TokenType.BREAK,
    "bruh-stop": TokenType.BREAK,
    "⏭": TokenType.CONTINUE,
    "keep-goin": TokenType.CONTINUE,

    # Operators
    "➕": TokenType.PLUS,
    "plus": TokenType.PLUS,
    "➖": TokenType.MINUS,
    "minus": TokenType.MINUS,
    "✖": TokenType.TIMES,
    "times": TokenType.TIMES,
    "➗": TokenType.DIVIDE,
    "div": TokenType.DIVIDE,
    "=": TokenType.ASSIGN,

    # Comparison
    "⚖": TokenType.EQ,
    "same": TokenType.EQ,
    "🙅": TokenType.NEQ,
    "nah": TokenType.NEQ,
    "🔼": TokenType.GT,
    "big": TokenType.GT,
    "🔽": TokenType.LT,
    "smol": TokenType.LT,
    "🔼=": TokenType.GTE,
    "big-eq": TokenType.GTE,
    "🔽=": TokenType.LTE,
    "smol-eq": TokenType.LTE,

    # Boolean
    "✅": TokenType.TRUE,
    "yeet": TokenType.TRUE,
    "❌": TokenType.FALSE,
    "sus": TokenType.FALSE,

    # Logical
    "🟰": TokenType.AND,
    "fam": TokenType.AND,
    "⭕": TokenType.OR,
    "maybe": TokenType.OR,
    "❎": TokenType.NOT,
    "nope": TokenType.NOT,

    # Unary
    "🔼+": TokenType.INC,
    "up-it": TokenType.INC,
    "🔽-": TokenType.DEC,
    "down-it": TokenType.DEC,

    # Arrays / Lists
    "[": TokenType.LIST_START,
    "squad": TokenType.LIST_START,
    "]": TokenType.LIST_END,
    "squad-end": TokenType.LIST_END,
    "➕📦": TokenType.LIST_APPEND,
    "add2squad": TokenType.LIST_APPEND,
    "🔍": TokenType.INDEX,
    "peek": TokenType.INDEX,
    "📏": TokenType.LENGTH,
    "howlong": TokenType.LENGTH,

    # Functions
    "🛠": TokenType.FUNC_DEF,
    "vibe": TokenType.FUNC_DEF,
    "🎁": TokenType.RETURN,
    "back": TokenType.RETURN,

    # Built-ins
    "🔢": TokenType.RANGE,
    "looprange": TokenType.RANGE,

    # Error / Exception
    "⚠": TokenType.THROW,
    "oops": TokenType.THROW,

    # Blocks
    "🔚": TokenType.END,
    "donezo": TokenType.END,

    # Comments
    "📝": TokenType.COMMENT,
    "//": TokenType.COMMENT,
    "cap": TokenType.COMMENT,

    # Symbols
    "(": TokenType.LPAREN,
    ")": TokenType.RPAREN,
    "{": TokenType.LBRACE,
    "}": TokenType.RBRACE,
    ";": TokenType.SEMICOLON,
    ",": TokenType.COMMA,
}
