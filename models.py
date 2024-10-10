from database import Base
from sqlalchemy.orm import Mapped, mapped_column


class UserOrm(Base):
    __tablename__ = "info"

#    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(primary_key=True)
    surname: Mapped[str]
    age: Mapped[int]

