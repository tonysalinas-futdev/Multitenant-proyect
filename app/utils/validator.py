import re
from pydantic import Field
email_pattern_validator=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

password_pattern_validator=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!#.%$@])[a-zA-Z0-9!#.%$@]{8,}$"

def password_field_validator():
    return Field(
        ...,
        description="La contraseña debe tener una longitud minima de 8 caractéres y ademas incluir un símbolo especial entre !#.%$@ , una mayúscula y una minúscula "
    )

def validate_password(password:str):
    if not re.fullmatch(password_pattern_validator,password) or not isinstance(password,str):
        raise ValueError("La contraseña debe contener al menos una letra mayúscula, una minúscula, un número y al menos un caracter especial entre !#.%$@")
    return password

def validate_email(email:str):
    if not isinstance(email, str) or not re.fullmatch(email_pattern_validator, email):
        raise ValueError("El email no cumple con los estándares necesarios")
    return True