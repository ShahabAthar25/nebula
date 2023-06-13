class TokenTypes:
    INT         = "INT"
    FLOAT       = "FLOAT"
    PLUS        = "PLUS"
    MINUS       = "MINUS"
    MULTIPLY    = "MULTIPLY"
    DIVIDE      = "DIVIDE"
    MODULO      = "MODULO"
    POWER       = "POWER"
    EQ          = "EQ"
    LPAREN      = "LPAREN"
    RPAREN      = "RPAREN"
    KEYWORD     = "KEYWORD"
    IDENTIFIER  = "IDENTIFIER"
    EOF         = "EOF"


class KeywordTypes:
    VAR = "var"

    @classmethod
    def check_variable(cls, string):
        variables = [value for value in cls.__dict__.values() if isinstance(value, str)]
        return string in variables


class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def matches(self, type_, value):
        return self.type == type_ and self.value == value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'
