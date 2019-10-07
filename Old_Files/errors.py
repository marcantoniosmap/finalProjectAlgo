class Error:
    def __init__(self,error_name,details,position):
        self.error_name = error_name
        self.details=details
        self.position=position


    def as_string(self):
        return f'{self.error_name}: {self.details} \nat character :{self.position}'

class IllegalCharError(Error):
    def __init__(self,details,position):
        super().__init__('Illegal Character',details,position)

class InvalidSyntaxError(Error):
    def __init__(self,details,position):
        super().__init__('Invalid Syntax',details,position)