from sqlalchemy.orm import Mapped
from sqlalchemy import Text
from sqlalchemy.orm import mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


class Project(IntIdPkMixin, Base):
    name: Mapped[str] 
    description: Mapped[str] = mapped_column(Text)
    github_url: Mapped[str]
    contributors: Mapped[int]