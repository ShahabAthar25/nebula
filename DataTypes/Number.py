from Errors.Arithmatics import DIVISION_BY_ZERO

class Number:
    def __init__(self, value):
        self.value = value

    def addition(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value), None

    def subtraction(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value), None

    def multiplication(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value), None

    def division(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, DIVISION_BY_ZERO(f"The number {self.value} cannot be divided by zero.")
            return Number(self.value / other.value), None
        
    def modulo(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, DIVISION_BY_ZERO(f"The number {self.value} cannot be divided by zero (Modulo '%').")
            return Number(self.value % other.value), None

    def power(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value), None

    def __repr__(self):
        return f"{self.value}"