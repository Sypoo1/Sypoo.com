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
    ProjectUpdate,
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

@router.get("/{project_id}", response_model=ProjectRead)
async def get_project_by_id(
    project_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    project = await project_crud.get_project_by_id(
        session=session,
        project_id=project_id,
    )
    return project


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


@router.put("/{project_id}", response_model=ProjectRead)
async def update_project(
    project_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    project_update: ProjectUpdate,
):
    project = await project_crud.update_project(
        session=session,
        project_id=project_id,
        project_update=project_update,
    )
    return project


@router.delete("/{project_id}", response_model=ProjectRead)
async def delete_project(
    project_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    project = await project_crud.delete_project(
        session=session,
        project_id=project_id,
    )
    return project