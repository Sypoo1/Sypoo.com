from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from core.models import Project
from core.schemas.project import ProjectCreate


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
    # await session.refresh(project)
    return project
