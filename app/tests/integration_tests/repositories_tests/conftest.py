import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.infraestructure.database.models import Base,Users,Company,Employee,EmployeePersonalInfo
from app.core.domain.constants.constants import UserRole
from app.infraestructure.repositories.sqlalchemy_user_repo import SqlalchemyUserRepo
from app.infraestructure.repositories.sqlalchemy_company_repo import SqlalchemyCompanyRepo
from app.infraestructure.repositories.sqlalchemy_employee_repo import SqlAlchemyEmployeeRepo
from app.infraestructure.database.models import RefreshToken
from app.infraestructure.repositories.sqlalchemy_refresh_token_repo import SqlAlchemyRefreshTokenRepo
import hashlib
from uuid import uuid4
from datetime import datetime , timedelta,timezone

DATABASE_URL="sqlite+aiosqlite:///:memory:"
engine=create_async_engine(DATABASE_URL)
AsyncLocalSession=sessionmaker(engine, autoflush=False,class_=AsyncSession)


#Fixture para crear los modelos y limpiarla luego de cada test
@pytest_asyncio.fixture
async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

#Fixture para obtener la sessión
@pytest_asyncio.fixture
async def get_test_session(create_db):
    async with AsyncLocalSession() as session:
        yield session

@pytest_asyncio.fixture
async def get_user_repo(get_test_session):
    return SqlalchemyUserRepo(get_test_session)

@pytest_asyncio.fixture
async def get_company_repo(get_test_session):
    return SqlalchemyCompanyRepo(get_test_session)

@pytest_asyncio.fixture
async def get_employee_repo(get_test_session):
    return SqlAlchemyEmployeeRepo(get_test_session)

@pytest_asyncio.fixture
async def get_refresh_token_repo(get_test_session):
    return SqlAlchemyRefreshTokenRepo(get_test_session)

@pytest_asyncio.fixture
async def save_two_users(get_user_repo:SqlalchemyUserRepo):
    user=Users(id=1,user_name="Tony",password="12345678", email="tony@example.com",role=UserRole.ADMIN)
    user2=Users(id=2,user_name="Pedro",password="12345678",email="tony222@gmail.com",role=UserRole.MANAGER)

    await get_user_repo.save(user)
    await get_user_repo.save(user2)

@pytest_asyncio.fixture
async def save_two_companys(get_company_repo:SqlalchemyCompanyRepo):
    company1=Company(id=1,company_name="Helados Cuba",country="Cuba",contact_email="heladoscuba@gmail.com")

    company2=Company(id=2,company_name="Carne Cuba",country="Cuba",contact_email="carnecuba@gmail.com")

    company3=Company(id=3,company_name="Ferrari",country="Italia",contact_email="ferrari@gmail.com")

    await get_company_repo.save(company1)
    await get_company_repo.save(company2)
    await get_company_repo.save(company3)

@pytest_asyncio.fixture
async def save_employees_in_db(get_employee_repo:SqlAlchemyEmployeeRepo):
    employee1=Employee(
        employee_name="Juan Carlos Chao Salinas",
        description="Empleado serio",
        email="carlos@gmail.com",
        charge="Software Engineer",
        department="DevOps dp",
        company_id=1,
        salary=2300.00,
        personal_info=EmployeePersonalInfo(
            country="Cuba",
            city="La Habana",
            current_address="Panchito Gómez",
        ))
    
    employee2=Employee(
        employee_name="Enrique Castillo",
        description="Empleado serio",
        email="enrique@gmail.com",
        charge="Software Engineer",
        department="DevOps dp",
        company_id=1,
        salary=1500.00,
        personal_info=EmployeePersonalInfo(
            country="Cuba",
            city="La Habana",
            current_address="Panchito Gómez",
        ))


    employee3=Employee(
        employee_name="Juan Antonio Gonzalez",
        description="Empleado serio",
        email="antonio@gmail.com",
        charge="Software Engineer",
        department="DevOps dp",
        company_id=1,
        salary=4000.00,
        personal_info=EmployeePersonalInfo(
            country="Cuba",
            city="La Habana",
            current_address="Panchito Gómez",
        ))
    
    lista_empleados=[employee1,employee2,employee3]
    for empl in lista_empleados:
        await get_employee_repo.save(empl)


@pytest_asyncio.fixture
async def save_two_tokens_in_bd(get_refresh_token_repo:SqlAlchemyRefreshTokenRepo):
    expires_time=datetime.now(timezone.utc)+timedelta(minutes=15)
    token1=RefreshToken(expires_at=expires_time,
                        token=hashlib.sha256("12345abcd".encode()).hexdigest(),
                        user_id=1
                        
                        )
    
    token2=RefreshToken(
        expires_at=expires_time,
        user_id=2,
        token=hashlib.sha256("54321opqr".encode()).hexdigest()
    )

    await get_refresh_token_repo.save(token1)
    await get_refresh_token_repo.save(token2)