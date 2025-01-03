from fastapi import APIRouter, Depends

from auth.auth_handler import get_current_active_user
from core.schemas.user import UserResponse
from core.models.user import User

router = APIRouter()

@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user