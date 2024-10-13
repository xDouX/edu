from sqlalchemy import ForeignKey

from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class UserOrm(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str]
    age: Mapped[int]
    items: Mapped[list["ItemsOrm"]] = relationship(back_populates="user", cascade="all, delete")


class ItemsOrm(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    user: Mapped["UserOrm"] = relationship(back_populates="items")
