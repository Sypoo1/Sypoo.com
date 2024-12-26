from fastapi import APIRouter

from core.config import settings


from.projects import router as projects_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    projects_router,
    prefix=settings.api.v1.projects,
)