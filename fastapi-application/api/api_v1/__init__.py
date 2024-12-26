from fastapi import APIRouter

from core.config import settings


from .projects import router as projects_router
from .auth import router as auth_router
from .users import router as users_router


router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    projects_router,
    prefix=settings.api.v1.projects,
)
router.include_router(
    auth_router,
    prefix=settings.api.v1.auth,
)
router.include_router(
    users_router,
    prefix=settings.api.v1.users,
)