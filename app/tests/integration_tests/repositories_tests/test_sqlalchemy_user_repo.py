from app.infraestructure.database.models import Users
from app.core.domain.constants.constants import UserRole
from app.infraestructure.repositories.sqlalchemy_user_repo import SqlalchemyUserRepo
from app.infraestructure.schemas.user_schemas import UpdateUser
import pytest

"""
Al heredar todos los repositorios de la clase genérica crud, solo testearemos los métodos comunes para todas las clases en esta implementación de usuario 
"""




@pytest.mark.asyncio
async def test_save_user_happy_path(get_user_repo:SqlalchemyUserRepo):
    """
    Usaremos la función save y comrobaremos luego que el usuario se guardó , intentando obtenerlo con get_by_id
    """
    user=Users(id=1,user_name="Tony",password="12345678", email="tony@example.com",role=UserRole.ADMIN)
    await get_user_repo.save(user)

    assert await get_user_repo.get_by_id(1)==user

@pytest.mark.asyncio
async def test_get_user_by_id(get_user_repo:SqlalchemyUserRepo,save_two_users):

    """
    Hay dos usuarios guardados en la bd , uno con id 1 , vamos a obtener a ese usuario exitosamente , y cuando intentemos obtener al de id 4 nos devolverá un None porque no existe
    """
    user1=await get_user_repo.get_by_id(1)
    user2=await get_user_repo.get_by_id(4)

    assert user1.id==1
    assert user2==None

@pytest.mark.asyncio
async def test_delete_user(get_user_repo:SqlalchemyUserRepo):

    """
    Para este test vamos a guardar a un usurioa , luego lo vamos a eliminar y posteriormente vamos a intentar obtenerlo, al hacerlo obtendremos un None porque ese usuario ya no va a existir
    """

    user=Users(id=1,user_name="Tony",password="12345678", email="tony@example.com",role=UserRole.ADMIN)
    await get_user_repo.save(user)
    await get_user_repo.delete_object(user)
    user=await get_user_repo.get_by_id(1) 
    assert user is None


@pytest.mark.asyncio
async def test_update_user(get_user_repo:SqlalchemyUserRepo,save_two_users):
    new_user_info=UpdateUser(user_name="Pedro Álvarez González", email="camavinga6@gmail.com")
    user=await get_user_repo.get_by_id(1)
    await get_user_repo.update(user,new_user_info)
    assert user.user_name=="Pedro Álvarez González"
    assert user.email=="camavinga6@gmail.com"

@pytest.mark.asyncio
async def test_get_all_users(get_user_repo:SqlalchemyUserRepo,save_two_users):
    list_of_users=await get_user_repo.get_all_objects()

    assert len(list_of_users)==2
    for obj in list_of_users:
        assert isinstance(obj,Users)


@pytest.mark.asyncio
async def test_get_by_email(get_user_repo:SqlalchemyUserRepo,save_two_users):
    user=await get_user_repo.get_by_email("tony@example.com")

    assert user.id==1
    assert user.email=="tony@example.com"

@pytest.mark.asyncio
async def test_get_by_username(get_user_repo:SqlalchemyUserRepo,save_two_users):
    user=await get_user_repo.get_by_user_name("Pedro")

    assert user.user_name=="Pedro"