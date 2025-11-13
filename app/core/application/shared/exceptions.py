
class DomainError(Exception):
    def __init__(self, message:str):
        self.message=message

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