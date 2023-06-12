from Errors.Error import Error

class EOFError(Error):
    def __init__(self, value):
        super().__init__(value, "EOF")