# lexer.py
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
        return self.source[self.pos:self.pos+length]

    def tokenize(self):
        while self.current_char() is not None:
            if self.current_char().isspace():
                self.advance()
                continue

            # Comments
            if self.peek(1) in ["📝", "/"]:
                self.tokenize_comment()
                continue

            # Strings
            if self.current_char() == '"':
                self.tokenize_string()
                continue

            # Numbers
            if self.current_char().isdigit():
                self.tokenize_number()
                continue

            # Multi-character token check (emoji combos or slang)
            matched = False
            for length in range(3, 0, -1):  # check up to 3-char tokens
                candidate = self.peek(length)
                if candidate in TOKEN_MAP:
                    self.add_token(TOKEN_MAP[candidate], candidate)
                    self.advance(length)
                    matched = True
                    break
            if matched:
                continue

            # Identifiers (variable names)
            if re.match(r'[A-Za-z_]', self.current_char()):
                self.tokenize_identifier()
                continue

            # Single-character symbols not in TOKEN_MAP
            self.add_token(TokenType.COMMENT, self.current_char())  # fallback
            self.advance()

        return self.tokens

    def add_token(self, type_, value):
        self.tokens.append(Token(type_, value, self.line, self.column))

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
        self.tokens.append(Token("NUMBER", num_str, self.line, start_col))

    def tokenize_string(self):
        start_col = self.column
        self.advance()  # skip opening "
        str_val = ""
        while self.current_char() is not None and self.current_char() != '"':
            str_val += self.current_char()
            self.advance()
        self.advance()  # skip closing "
        self.tokens.append(Token("STRING", str_val, self.line, start_col))

    def tokenize_identifier(self):
        start_col = self.column
        id_str = ""
        while self.current_char() is not None and re.match(r'[A-Za-z0-9_😀]', self.current_char()):
            id_str += self.current_char()
            self.advance()
        # Check if identifier is a keyword in TOKEN_MAP
        token_type = TOKEN_MAP.get(id_str, TokenType.VAR)
        self.tokens.append(Token(token_type, id_str, self.line, start_col))

    def tokenize_comment(self):
        start_col = self.column
        if self.peek(1) == "📝":
            while self.current_char() is not None and self.current_char() != "\n":
                self.advance()
        elif self.peek(2) == "//":
            while self.current_char() is not None and self.current_char() != "\n":
                self.advance()
        self.tokens.append(Token(TokenType.COMMENT, "comment", self.line, start_col))
