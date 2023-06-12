class Error:
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def asString(self):
        error = f"{self.type} Error: {self.value}"

        return error