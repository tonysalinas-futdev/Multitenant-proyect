from app.utils.validator import validate_password, validate_email
from app.core.domain.constants.constants import  UserRole
class User():
    def __init__(self, id, user_name:str, password:str, email:str, role:UserRole, company_id ):
        if not user_name or  id is None or not email or password is None:
            raise ValueError("Estos campos son obligatorios")
        if not isinstance(role, UserRole):
            raise ValueError("El rol introducido no es válido")
            
        validate_email(email)
        validate_password(password)
        self.id=id
        self.user_name=user_name
        self.password=password
        self.email=email
        self.role=role
        self.company_id=company_id

    def __eq__(self, another_instance):
        return(
                isinstance(another_instance, User)
                and self.id==another_instance.id
                and self.user_name==another_instance.user_name
                and self.password==another_instance.password
                and self.email==another_instance.email
                and self.role==another_instance.role
                and self.company_id==another_instance.company_id)
    
    def update_profile(self,new_username:str, new_email:str):
        self.user_name=new_username
        self.email=new_email
        
    
    def change_password(self,current_password:str, new_password:str):
        if current_password!=self.password:
            raise ValueError("Contraseña incorrecta")
        validate_password(new_password)
        self.password=new_password