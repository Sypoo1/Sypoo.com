from sqlalchemy.orm import Mapped
from sqlalchemy import Text
from sqlalchemy.orm import mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


class Project(IntIdPkMixin, Base):
    Name: Mapped[str] = mapped_column(unique=True)
    Disctiption: Mapped[str] = mapped_column(Text)
    Github_Url: Mapped[str]
    Contributors: Mapped[int]