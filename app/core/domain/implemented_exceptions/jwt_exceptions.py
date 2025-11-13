from app.core.application.shared.exceptions import DomainError

class InvalidTokenError(DomainError):
    def __init__(self, message):
        super().__init__("Token inválido o modificado")