import pytest
from app.core.domain.entities.user import User
from app.infraestructure.database.models import UserRole
import re

def test_valid_user_creation():
    user=User(user_name="Tony", password="Abcd1234#", email="email@example.com",role=UserRole.ADMIN, company_id=1)

    assert user.user_name=="Tony"
    assert user.email=="email@example.com"


@pytest.mark.parametrize("user_name, password, email, role, company_id",(
    [None,"Abcd1234#", "example@gmail.com",UserRole.MANAGER,2 ],
    ["Tony","12345678", "example@gmail.com",UserRole.ADMIN,3 ],
    ["Tony","Abcd1234#", "exampgmail.com",UserRole.VIEWER,3 ],
    ["Tonys","Abcd1234#", "example@gmail.com","person",3 ]
    )
    
    )
def test_failed_user_creation(user_name, password, email, role, company_id):
    """
    Vamos a probar que nos tire un ValueError si mandamos campos incorrectos, primero user_name, luego password, después email y luego rol
    """
    if user_name=="Tonys":
        with pytest.raises(ValueError, match="El rol introducido no es válido"):
            User(user_name=user_name,password=password,email=email,role=role,company_id=company_id)


    with pytest.raises(ValueError):
        User( user_name=user_name,password=password,email=email,role=role,company_id=company_id)


def test_update_profile(return_test_user:User):
    return_test_user.update_profile("Carlos Gonzalez","example222@gmail.com")
    assert return_test_user.user_name=="Carlos Gonzalez"
    assert return_test_user.email=="example222@gmail.com"

@pytest.mark.parametrize("current_password, new_password",(
        ["aS1234567657#","Abcd12345#"],
        ["Abcd1234#","abcd12345#"],

))
def test_change_password_failed(new_password:str,current_password:str,return_test_user:User):
    """En el primer caso vamos a probar a  ingresar mal la contraseña actual y en el segundo vamos a pasar una nueva contraseña que no cumple con los requisitos exigidios"""

    if current_password=="aS1234567657#":
        with pytest.raises(ValueError,match="Contraseña incorrecta"):
            return_test_user.change_password(current_password,new_password)
    else:
        with pytest.raises(ValueError,match=re.escape("La contraseña debe contener al menos una letra mayúscula, una minúscula, un número y al menos un caracter especial entre !#.%$@")):
            return_test_user.change_password(current_password,new_password)

def test_change_password_succes(return_test_user:User):
    return_test_user.change_password("Abcd1234#","Abcd123456789#")
    assert return_test_user.password=="Abcd123456789#"

