from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from core.models import Project
from core.schemas.project import ProjectCreate, ProjectUpdate


async def get_all_projects(
    session: AsyncSession,
) -> Sequence[Project]:
    stmt = select(Project).order_by(Project.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_project(
    session: AsyncSession,
    project_create: ProjectCreate,
) -> Project:
    project = Project(**project_create.model_dump())
    session.add(project)
    await session.commit()
    await session.refresh(project)
    return project


async def update_project(
    session: AsyncSession,
    project_id: int,
    project_update: ProjectUpdate,
) -> Project:
    stmt = select(Project).where(Project.id == project_id)
    result = await session.execute(stmt)
    project = result.scalar_one_or_none()

    if project is None:
        raise ValueError(f"Project with id:{project_id} not found")

    for key, value in project_update.model_dump().items():
        setattr(project, key, value)

    await session.commit()
    await session.refresh(project)
    return project


async def delete_project(
    session: AsyncSession,
    project_id: int,
) -> Project:
    stmt = select(Project).where(Project.id == project_id)
    result = await session.execute(stmt)
    project = result.scalar_one_or_none()

    if project is None:
        raise ValueError(f"Project with id:{project_id} not found")

    await session.delete(project)
    await session.commit()
    return project