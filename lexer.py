# lexer.py — CWE-Compiler Emoji-Slang Lexer
from tokens import Token, TokenType, TOKEN_MAP
import re

class Lexer:
    def __init__(self, source_code):
        self.source = source_code
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []

    def advance(self, steps=1):
        for _ in range(steps):
            if self.current_char() == "\n":
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.pos += 1

    def current_char(self):
        if self.pos >= len(self.source):
            return None
        return self.source[self.pos]

    def peek(self, length=1):
        return self.source[self.pos:self.pos + length]

    def add_token(self, type_, value, start_col=None):
        col = start_col if start_col is not None else self.column
        self.tokens.append(Token(type_, value, self.line, col))

    def tokenize(self):
        max_token_len = max(len(k) for k in TOKEN_MAP.keys())

        while self.current_char() is not None:
            char = self.current_char()

            # Whitespace / newline
            if char.isspace():
                if char == "\n":
                    self.add_token(TokenType.NEWLINE, "\\n", self.column)
                else:
                    self.add_token(TokenType.WHITESPACE, char, self.column)
                self.advance()
                continue

            # Comments
            if self.peek(1) == "📝" or self.peek(2) == "//":
                self.tokenize_comment()
                continue

            # Multiline comment (/* ... */)
            if self.peek(2) == "/*":
                self.tokenize_multiline_comment()
                continue

            # String literal
            if char == '"':
                self.tokenize_string()
                continue

            # Character literal
            if char == "'":
                self.tokenize_char()
                continue

            # Number (int / float)
            if char.isdigit():
                self.tokenize_number()
                continue

            # Multi-character token (emoji/slang) — longest match first
            matched = False
            for length in range(max_token_len, 0, -1):
                candidate = self.peek(length)
                if candidate in TOKEN_MAP:
                    start_col = self.column
                    self.add_token(TOKEN_MAP[candidate], candidate, start_col)
                    self.advance(length)
                    matched = True
                    break
            if matched:
                continue

            # Identifiers / hybrid emojis
            if re.match(r'[A-Za-z0-9_😀-🙏]', char):
                self.tokenize_identifier()
                continue

            # Unknown / trap token
            print(f"Unknown token: {char} at {self.line}:{self.column}")  # debug
            self.add_token(TokenType.UNKNOWN, char, self.column)
            self.advance()

        # EOF token
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens

    def tokenize_number(self):
        start_col = self.column
        num_str = ""
        dot_count = 0
        while self.current_char() is not None and (self.current_char().isdigit() or self.current_char() == '.'):
            if self.current_char() == '.':
                dot_count += 1
                if dot_count > 1:
                    break
            num_str += self.current_char()
            self.advance()
        token_type = TokenType.FLOAT if '.' in num_str else TokenType.NUMBER
        self.add_token(token_type, num_str, start_col)

    def tokenize_string(self):
        start_col = self.column
        self.advance()  # skip opening "
        str_val = ""
        escapes = {"n": "\n", "t": "\t", "\\": "\\", '"': '"'}
        while self.current_char() is not None and self.current_char() != '"':
            if self.current_char() == "\\" and self.peek(2)[1] in escapes:
                esc_char = self.peek(2)[1]
                str_val += escapes[esc_char]
                self.advance(2)
            else:
                str_val += self.current_char()
                self.advance()
        self.advance()  # skip closing "
        self.add_token(TokenType.STRING, str_val, start_col)

    def tokenize_char(self):
        start_col = self.column
        self.advance()  # skip opening '
        char_val = self.current_char()
        self.advance()
        if self.current_char() == "'":
            self.advance()
            self.add_token(TokenType.CHAR, char_val, start_col)
        else:
            self.add_token(TokenType.UNKNOWN, char_val, start_col)

    def tokenize_identifier(self):
        start_col = self.column
        id_str = ""
        while self.current_char() is not None and re.match(r'[A-Za-z0-9_😀-🙏]', self.current_char()):
            id_str += self.current_char()
            self.advance()
        token_type = TOKEN_MAP.get(id_str.lower(), TokenType.IDENTIFIER)
        self.add_token(token_type, id_str, start_col)

    def tokenize_comment(self):
        start_col = self.column
        comment_str = ""
        if self.peek(1) == "📝":
            self.advance()  # skip marker
            while self.current_char() is not None and self.current_char() != "\n":
                comment_str += self.current_char()
                self.advance()
        elif self.peek(2) == "//":
            self.advance(2)  # skip //
            while self.current_char() is not None and self.current_char() != "\n":
                comment_str += self.current_char()
                self.advance()
        self.add_token(TokenType.COMMENT, comment_str.strip(), start_col)

    def tokenize_multiline_comment(self):
        start_col = self.column
        self.advance(2)  # skip /*
        comment_str = ""
        while self.current_char() is not None and self.peek(2) != "*/":
            comment_str += self.current_char()
            self.advance()
        if self.peek(2) == "*/":
            self.advance(2)
        self.add_token(TokenType.COMMENT, comment_str.strip(), start_col)
