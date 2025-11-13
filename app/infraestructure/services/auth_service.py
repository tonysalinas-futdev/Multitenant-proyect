from app.config.settings import settings
from datetime import datetime,timedelta,timezone
from jose import jwt , JWTError
from typing import Optional
from app.core.domain.implemented_exceptions.jwt_exceptions import InvalidTokenError
import hashlib
from app.infraestructure.database.models import RefreshToken,Users
from uuid import uuid4
from app.infraestructure.repositories.sqlalchemy_refresh_token_repo import SqlAlchemyRefreshTokenRepo


class AuthService():
    def __init__(self,repo:SqlAlchemyRefreshTokenRepo):
        self.algorithm=settings.algorithm
        self.jwt_secret_key=settings.jwt_secret_key
        self.access_token_duration=settings.access_token_expire_minutes
        self.refresh_token_duration=settings.refresh_token_expire_days
        self.refresh_token_repo=repo

    async def create_acces_token(self, data:dict, expires_time:Optional[timedelta]=None ):

        if expires_time:
            token_duration=datetime.now(timezone.utc)+expires_time
        else:
            token_duration=datetime.now(timezone.utc)+self.access_token_duration
        data.update({"exp":token_duration})
        access_token=jwt.encode(data,self.jwt_secret_key,algorithm=self.algorithm)
        return access_token

    async def create_refresh_token(self,user_id:int,expires_time:Optional[timedelta]=None):
        if expires_time:
            token_duration=datetime.now(timezone.utc)+expires_time
        else:
            token_duration=datetime.now(timezone.utc)+self.refresh_token_duration

        token_value=str(uuid4())

        payload=hashlib.sha256(token_value.encode()).hexdigest()

        token=RefreshToken(
        token=payload,
        user_id=user_id,
        expires_at=token_duration

        )
        await self.refresh_token_repo.save(token)
        return token_value

    async def verify_access_token(self,token:str):
        try:
            payload=jwt.decode(token,self.jwt_secret_key,algorithms=[self.algorithm])
            return payload
            
        except JWTError:
            return None
    
    async def verify_refresh_token(self, token_value:str):
        hash_token_value=hashlib.sha256(token_value.encode()).hexdigest()

        token=await self.refresh_token_repo.get_token_by_value(hash_token_value)
        if not token or token.expires_at<datetime.now(timezone.utc) or token.is_revoked==True :
            raise InvalidTokenError("Refresh token inválido")

        return token
    
    async def create_access_and_refresh_tokens(self,user_data:Users):
        access_token_data={
            "id":user_data.id,
            "username":user_data.user_name,
            "email":user_data.email,
            "role":user_data.role.value
        }

        access_token=await self.create_acces_token(access_token_data)
        refresh_token=await self.create_refresh_token(user_data.id)

        return {
            "access_token":access_token,
            "refresh_token":refresh_token,
            "token_type":"Bearer"
        }