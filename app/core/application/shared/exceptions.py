
class DomainError(Exception):
    def __init__(self, message:str, code:str=None):
        self.message=message
        self.code=code

class NotFoundError(DomainError):
    pass

class DomainRuleValidationError(DomainError):
    pass

class AlredyExistsError(DomainError):
    pass

class PermissionDeniedError(DomainError):
    pass

class InvalidCredentialsError(DomainError):
    pass