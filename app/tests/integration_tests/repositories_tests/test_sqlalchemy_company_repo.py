import pytest
from app.infraestructure.repositories.sqlalchemy_company_repo import SqlalchemyCompanyRepo
from app.infraestructure.database.models import Company
from app.core.domain.entities.company import Company as CompanyEntity

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


@pytest.mark.asyncio
async def test_company_entity_to_model(get_company_repo:SqlalchemyCompanyRepo):
    """
    Vamos a probar que al pasar de entidad a modelo los datos se mantienen y todo s ejecuta de forma correcta y que además al guardarlo en la base de datos obtiene los campos que le faltan(id, fecha de creación)
    
    """

    company=CompanyEntity(company_name="Helados Cuba", contact_email="helados@gmail.com",country="Cuba")
    
    company_model=await get_company_repo.entity_to_model(company)
    await get_company_repo.save(company_model)
    saved_company=await get_company_repo.get_by_id(1)
    
    
    assert company_model.contact_email=="helados@gmail.com"
    assert company_model.country=="Cuba"
    assert company_model.company_name=="Helados Cuba"
    assert saved_company.company_name=="Helados Cuba"
    assert saved_company.created_at is not None
    