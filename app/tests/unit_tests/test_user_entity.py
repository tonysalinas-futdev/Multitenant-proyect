import pytest
from app.core.domain.entities.user import User
from app.infraestructure.database.models import UserRole

def test_valid_user_creation():
    user=User(1, user_name="Tony", password="Abcd1234#", email="email@example.com",role=UserRole.ADMIN, company_id=1)

    assert user.user_name=="Tony"
    assert user.email=="email@example.com"


@pytest.mark.parametrize("id,user_name, password, email, role, company_id",(
    [1, None,"Abcd1234#", "example@gmail.com",UserRole.MANAGER,2 ],
    [2, "Tony","12345678", "example@gmail.com",UserRole.ADMIN,3 ],
    [3, "Tony","Abcd1234#", "exampgmail.com",UserRole.VIEWER,3 ],
    [4, "Tony","Abcd1234#", "example@gmail.com","person",3 ]
    )
    
    )
def test_failed_user_creation(id, user_name, password, email, role, company_id):
    """
    Vamos a probar que nos tire un ValueError si mandamos campos incorrectos, primero user_name, luego password, después email y luego rol
    """
    if id==4:
        with pytest.raises(ValueError, match="El rol introducido no es válido"):
            User(id=id, user_name=user_name,password=password,email=email,role=role,company_id=company_id)


    with pytest.raises(ValueError):
        User(id=id, user_name=user_name,password=password,email=email,role=role,company_id=company_id)
