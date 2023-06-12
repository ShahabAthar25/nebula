class NumberNode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f"{self.tok}"

class UnaryNode:
    def __init__(self, op, value):
        self.op = op
        self.value = value

    def __repr__(self):
        return f"({self.op}, {self.value})"
    
class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"({self.left}, {self.op}, {self.right})"