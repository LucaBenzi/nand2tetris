class TokenizerException(BaseException):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

    def __init__(self, message, line_number):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.line_number = line_number

    def message(self):
        return self.args[0]

    def get_line(self):
        return self.line_number
