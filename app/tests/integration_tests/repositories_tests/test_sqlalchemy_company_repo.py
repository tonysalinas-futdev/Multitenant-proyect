import pytest
from app.infraestructure.repositories.sqlalchemy_company_repo import SqlalchemyCompanyRepo
from app.infraestructure.database.models import Company

@pytest.mark.asyncio
async def test_get_by_company_email(get_company_repo:SqlalchemyCompanyRepo,save_two_companys):

    """Vamos a obtener correctamente dos compañias por su email, luego vamos a intentar obtener una con un nombre inexistente, nos retornará None"""


    helados_company=await get_company_repo.get_by_email("heladoscuba@gmail.com")
    carne_company=await get_company_repo.get_by_email("carnecuba@gmail.com")
    nonexistent_company=await get_company_repo.get_by_email("nonexistent@gmail.com")

    assert helados_company.contact_email=="heladoscuba@gmail.com"
    assert carne_company.contact_email=="carnecuba@gmail.com"
    assert nonexistent_company is None

@pytest.mark.asyncio
async def test_get_company_by_country(get_company_repo:SqlalchemyCompanyRepo,save_two_companys):
    """
    Comprobaremos que efectivamente solo hay dos compañías que tienen Cuba como país y que no se coló ninguna de otro lugar en la lista
    """

    cuba_companys=await get_company_repo.get_by_country("Cuba")
    assert len(cuba_companys)==2
    assert all(company.country=="Cuba" for company in cuba_companys)