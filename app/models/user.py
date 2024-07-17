from datetime import datetime

from sqlalchemy import String, Integer, Text, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utility.time_processor import get_local_time
from app.database.mariadb import Base


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False, comment="使用者名稱")
    password: Mapped[str] = mapped_column(String(512), nullable=False, comment="使用者密碼")
    fullname: Mapped[str] = mapped_column(String(100), nullable=False, comment="使用者全名")
    roles: Mapped[str] = mapped_column(Text, nullable=False, default='user', comment="使用者角色")
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, comment="是否有效")
    last_login: Mapped[None | datetime] = mapped_column(
        DateTime, nullable=True, default=get_local_time, comment="上次登入時間"
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=get_local_time, onupdate=get_local_time, comment="更新時間",
        server_default=func.now()
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=get_local_time, comment="創建時間", server_default=func.now()
    )

    todos = relationship('Todo', back_populates='user')

    @property
    def identity(self):
        return self.id

    # noinspection PyBroadException
    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id_):
        return cls.query.filter_by(id=id_).one_or_none()

    def is_valid(self):
        return self.is_active

    def to_dict(self):
        return {
            "username": self.username,
            "fullname": self.fullname,
            "roles": self.rolenames,
            "last_login": self.last_login,
        }
