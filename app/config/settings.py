from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")
    app_name:str="Aplicación Empresarial Multitenant"
    debug:bool=True
    postgres_password:str
    postgres_user:str
    postgres_db:str
    postgres_port:int=5432
    postgres_host:str="localhost"
    jwt_secret_key:str
    algorithm:str
    access_token_expire_minutes:int=40
    refresh_token_expire_days:int=7

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}/{self.postgres_db}"    



    
settings=Settings()

print(settings.database_url)