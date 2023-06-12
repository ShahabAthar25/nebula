from Utils.ErrorHandler import ErrorHandler
from DataTypes.Number import Number
from Lexer.Tokens import TokenTypes

class Interpreter:
    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        return Exception(f'No visit_{type(node).__name__} method defined')

    def visit_NumberNode(self, node):
        return ErrorHandler().success(
            Number(node.tok.value)
        )
    
    def visit_BinOpNode(self, node):
        res = ErrorHandler()

        left = res.register(self.visit(node.left))
        if res.error: return res

        right = res.register(self.visit(node.right))
        if res.error: return res

        if node.op.type == TokenTypes.PLUS:
            result, error = left.addition(right)
        elif node.op.type == TokenTypes.MINUS:
            result, error = left.subtraction(right)
        elif node.op.type == TokenTypes.MULTIPLY:
            result, error = left.multiplication(right)
        elif node.op.type == TokenTypes.DIVIDE:
            result, error = left.division(right)
        elif node.op.type == TokenTypes.MODULO:
            result, error = left.modulo(right)
        else:
            raise Exception("Operator Not Found")

        if error:
            return res.failure(error)

        return res.success(result)
    
    def visit_UnaryNode(self, node):
        res = ErrorHandler()

        if node.op.type == TokenTypes.PLUS:
            return res.success(node.value.tok.value)
        elif node.op.type == TokenTypes.MINUS:
            number = res.register(self.visit(node.value))
            if res.error: return res

            result, error = number.multiplication(Number(-1))
            if error: return res.failure(error)

            return res.success(result)
        else:
            raise Exception("Invalid sign for unary number")