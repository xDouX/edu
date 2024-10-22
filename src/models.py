from sqlalchemy import ForeignKey
from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class WorkGroup(Base):
    __tablename__ = "work_groups"

    name: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    users: Mapped[list["UserOrm"]] = relationship(back_populates="group")


class UserOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    user_group: Mapped[str] = mapped_column(ForeignKey("work_groups.name", ondelete="CASCADE"))
    group: Mapped["WorkGroup"] = relationship("WorkGroup", back_populates="users")
    items: Mapped[list["ItemsOrm"]] = relationship(back_populates="users", cascade="all, delete")


class ItemsOrm(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    weight: Mapped[float] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    users_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    users: Mapped["UserOrm"] = relationship(back_populates="items")
