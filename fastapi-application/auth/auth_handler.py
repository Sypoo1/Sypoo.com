from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from core.models import db_helper
from core.models.user import User
from core.schemas.token import TokenData
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

router = APIRouter()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)



async def get_user(session: AsyncSession, username: str):
    stmt = select(User).where(User.username == username)
    result = await session.execute(stmt)
    db_user = result.scalar_one_or_none()
    return db_user


async def authenticate_user(session: AsyncSession, username: str, password: str):
    user = await get_user(session, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.auth.secret_key, algorithm=settings.auth.algorithm)
    return encoded_jwt


async def get_current_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    token: str = Depends(oauth2_scheme),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.auth.secret_key, algorithms=[settings.auth.algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception

    stmt = select(User).where(User.username == token_data.username)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user
