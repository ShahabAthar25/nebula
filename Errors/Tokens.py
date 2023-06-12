from Errors.Error import Error

class SyntaxError(Error):
    def __init__(self, value):
        super().__init__(value, "Syntax")