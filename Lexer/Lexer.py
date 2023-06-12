from Lexer.Tokens import Token, TokenTypes
from Errors.Tokens import SyntaxError

DIGITS = "1234567890"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None

        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if len(self.text) > self.pos else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in " \t":
                self.advance()
            elif self.current_char == "+":
                tokens.append(Token(TokenTypes.PLUS))
                self.advance()
            elif self.current_char == "-":
                tokens.append(Token(TokenTypes.MINUS))
                self.advance()
            elif self.current_char == "*":
                tokens.append(Token(TokenTypes.MULTIPLY))
                self.advance()
            elif self.current_char == "/":
                tokens.append(Token(TokenTypes.DIVIDE))
                self.advance()
            elif self.current_char == "%":
                tokens.append(Token(TokenTypes.MODULO))
                self.advance()
            elif self.current_char == "^":
                tokens.append(Token(TokenTypes.POWER))
                self.advance()
            elif self.current_char == "(":
                tokens.append(Token(TokenTypes.LPAREN))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token(TokenTypes.RPAREN))
                self.advance()
            elif self.current_char in DIGITS:
                token, error = self.make_number()
                if error: return [], error
                tokens.append(token)
            else:
                return [], SyntaxError(f"Token '{self.current_char}' was not recognized by nebula.")
            
        tokens.append(Token(TokenTypes.EOF))

        return tokens, None

    def make_number(self):
        num_string = ""
        dots = 0

        while self.current_char != None and self.current_char in DIGITS + ".":
            if self.current_char == ".":
                if dots > 1:
                    break
                dots += 1
            
            num_string += self.current_char
            self.advance()

        if dots == 1:
            return Token(TokenTypes.FLOAT, float(num_string)), None
        elif dots == 0:
            return Token(TokenTypes.INT, int(num_string)), None
        else:
            return None, SyntaxError("Float number can only have one decimal point '.'")