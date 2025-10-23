
class User():
    def __init__(self, id, user_name, password, email, role, company_id ):
        self.id=id
        self.user_name=user_name
        self.password=password
        self.email=email
        self.role=role
        self.company_id=company_id
        
    def validate_username_and_email(self):
        if len(self.user_name)==0 and len(self.email)==0:
            raise ValueError("Estos camppos no pueden estar vacíos")
    
    def validate_password(self):
        if len(self.password)<8:
            raise ValueError("La contraseña debe tener mínimo 8 caracteres")
        
