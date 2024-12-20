from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper

from core.schemas.project import (
    ProjectRead,
    ProjectCreate,
)
from crud import project as project_crud

router = APIRouter(tags=["Projects"])


@router.get("", response_model=list[ProjectRead])
async def get_projects(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    projects = await project_crud.get_all_projects(session=session)
    return projects


@router.post("", response_model=ProjectRead)
async def create_project(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    project_create: ProjectCreate,
):
    project = await project_crud.create_project(
        session=session,
        project_create=project_create,
    )
    return project
