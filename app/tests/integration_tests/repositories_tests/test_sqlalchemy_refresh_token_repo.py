from app.infraestructure.database.models import RefreshToken
from app.infraestructure.repositories.sqlalchemy_refresh_token_repo import SqlAlchemyRefreshTokenRepo
import hashlib
import pytest



@pytest.mark.asyncio
async def test_get_token_by_value_happy_path(get_refresh_token_repo:SqlAlchemyRefreshTokenRepo, save_two_tokens_in_bd):

    """
    En este test vamos a obtener correctamente los dos tokens, para eso vamos a pasar como valor la cadena definida en la fixture, para cada token
    """

    token1=await get_refresh_token_repo.get_token_by_value(hashlib.sha256("12345abcd".encode()).hexdigest())

    token2=await get_refresh_token_repo.get_token_by_value(hashlib.sha256("54321opqr".encode()).hexdigest())  

    assert token1.user_id==1 # Expected: 1
    assert token2.user_id==2 # Expected: 2



@pytest.mark.asyncio
async def test_get_token_by_value_failed(get_refresh_token_repo:SqlAlchemyRefreshTokenRepo, save_two_tokens_in_bd):

    """
    Obtendremos None ya que la cadena que pasamos a get_by_value no coincide con la definida en los conftest
    """

    token1=await get_refresh_token_repo.get_token_by_value(hashlib.sha256("12345".encode()).hexdigest())

    token2=await get_refresh_token_repo.get_token_by_value(hashlib.sha256("54321".encode()).hexdigest())  

    assert token1==None # Expected: None
    assert token2==None # Expected: None


@pytest.mark.asyncio
async def test_revoke_token(get_refresh_token_repo:SqlAlchemyRefreshTokenRepo, save_two_tokens_in_bd):
    token1=await get_refresh_token_repo.get_by_id(1)

    await get_refresh_token_repo.revoke_token(token1)


    assert token1.is_revoked==True # Expected: True