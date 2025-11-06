from app.infraestructure.repositories.sqlalchemy_generic_crud import SqlAlchemyGenericCrud
from app.infraestructure.database.models import Company
from sqlalchemy import select
from app.core.application.repositories.company_interface import CompanyRepositoryInterface
from typing import List


class SqlalchemyCompanyRepo(CompanyRepositoryInterface,SqlAlchemyGenericCrud[Company]):
    def __init__(self, session):
        super().__init__(session, Company)

    async def get_by_company_name(self, company_name:str)->Company:
        stmt=select(Company).where(Company.company_name==company_name)
        result=await self.session.execute(stmt)
        company=result.scalar_one_or_none()
        return company
    

    async def get_by_country(self, country:str)->List[Company]:
        stmt=select(Company).where(Company.country==country)
        result=await self.session.execute(stmt)
        companys=result.scalars().all()
        return companys

    async def get_by_email(self, email:str):
        
        stmt=select(Company).where(Company.contact_email==email)
        result=await self.session.execute(stmt)
        company=result.scalar_one_or_none()
        return company
        
