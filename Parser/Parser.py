from Lexer.Tokens import TokenTypes
from Errors.Tokens import SyntaxError
from Errors.EOF import EOFError
from Utils.ErrorHandler import ErrorHandler
from Parser.Nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens

        self.pos = -1
        self.current_tok = None

        self.advance()

    def advance(self):
        self.pos += 1
        if len(self.tokens) > self.pos:
            self.current_tok = self.tokens[self.pos]

    def parse(self):
        res = self.expr()

        if not res.error and self.current_tok.type != TokenTypes.EOF:
            return res.failure(EOFError("Expected expr."))

        return res

    def atom(self):
        res = ErrorHandler()
        tok = self.current_tok

        if self.current_tok.type in (TokenTypes.INT, TokenTypes.FLOAT):
            self.advance()
            return res.success(NumberNode(tok))
        
        elif self.current_tok.type == TokenTypes.LPAREN:
            self.advance()
            expr = res.register(self.expr())

            if self.current_tok.type != TokenTypes.RPAREN:
                res.failure(SyntaxError("Expected ')' after expr."))

            self.advance()

            return res.success(expr)
        
        else:
            return res.failure(SyntaxError("Expected a expr."))
        
    def factor(self):
        res = ErrorHandler()

        if self.current_tok.type in (TokenTypes.MINUS, TokenTypes.PLUS):
            op = self.current_tok
            self.advance()

            value = res.register(self.factor())
            if res.error: return res

            return res.success(UnaryNode(op, value))
        
        return self.binop(self.atom, (TokenTypes.POWER), self.factor)

    def term(self):
        return self.binop(self.factor, (TokenTypes.DIVIDE, TokenTypes.MULTIPLY, TokenTypes.MODULO))

    def expr(self):
        return self.binop(self.term, (TokenTypes.PLUS, TokenTypes.MINUS))

        
    def binop(self, func_a, ops, func_b=None):
        if func_b == None:
            func_b = func_a

        res = ErrorHandler()

        left = res.register(func_a())
        if res.error: return res

        while self.current_tok.type in ops:
            tok = self.current_tok
            self.advance()

            right = res.register(func_b())
            if res.error: return res

            left = BinOpNode(left, tok, right)

        return res.success(left)