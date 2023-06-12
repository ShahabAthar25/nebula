from Errors.Error import Error

class DIVISION_BY_ZERO(Error):
    def __init__(self, value):
        super().__init__(value, "Division By Zero")