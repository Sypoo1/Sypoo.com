from pydantic import BaseModel
from pydantic import ConfigDict


class ProjectBase(BaseModel):
    name: str
    description: str
    github_url: str
    contributors: int


class ProjectCreate(ProjectBase):
    pass


class ProjectRead(ProjectBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
