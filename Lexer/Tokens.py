class TokenTypes:
    INT         = "INT"
    FLOAT       = "FLOAT"
    PLUS        = "PLUS"
    MINUS       = "MINUS"
    MULTIPLY    = "MULTIPLY"
    DIVIDE      = "DIVIDE"
    MODULO      = "MODULO"
    LPAREN      = "LPAREN"
    RPAREN      = "RPAREN"
    EOF         = "EOF"

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'