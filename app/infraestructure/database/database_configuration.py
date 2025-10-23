
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config.settings import settings
from fastapi import Depends

engine=create_async_engine(url=settings.database_url, echo=settings.debug, connect_args={"check_same_thread":False})
Base=declarative_base()
Async_Session=sessionmaker(bind=engine, class_=AsyncSession, autoflush=False, autocommit=False)

async def get_database():
    async with Async_Session as session:
        yield session

async def get_session(session:AsyncSession=Depends(get_database))->AsyncSession:
    return session