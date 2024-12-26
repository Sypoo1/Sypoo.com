from datetime import timedelta
from typing import Annotated

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from auth.auth_handler import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_user, get_password_hash

from core.schemas.token import Token
from core.schemas.user import UserCreate, UserResponse
from core.models.user import User

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register_user(
    user: UserCreate, 
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter),
    ],
):
    try:
        db_user = await get_user(session, user.username)
        if db_user:
            raise HTTPException(status_code=400, detail="Username already registered.")
        

        hashed_password = get_password_hash(user.password)

        new_user = User(
            username=user.username, 
            hashed_password=hashed_password
        )

        session.add(new_user)

        await session.commit()
        await session.refresh(new_user)
        return new_user

    except HTTPException as http_ex:
        raise http_ex

    except Exception as e:

        print(f"Unexpected error during registration: {str(e)}")
        await session.rollback()
        raise HTTPException(
            status_code=500, 
            detail="Internal Server Error"
        )


@router.post("/token")
async def login_for_access_token(
        session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
        form_data: OAuth2PasswordRequestForm = Depends(),
) -> Token:
    user = await authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")