from datetime import datetime

from sqlalchemy import String, Integer, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.mariadb import Base
from app.utility.time_processor import get_local_time


class Todo(Base):
    __tablename__ = 'todo'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False, comment="使用者ID")
    user_id: Mapped[int] = mapped_column(Integer, nullable=False, comment="使用者ID")
    title: Mapped[str] = mapped_column(String(512), nullable=False, comment="待辦事項標題")
    should_alert: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, comment="是否需要提醒")
    scheduled_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, comment="預定時間")
    is_done: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment="是否已完成")

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=get_local_time, onupdate=get_local_time, comment="更新時間",
        server_default=func.now()
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=get_local_time, comment="創建時間", server_default=func.now()
    )

    # user = relationship('User', back_populates='todo_lists', uselist=False)

    def to_dict(self, exclude_fields=None):
        result = {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'should_alert': self.should_alert,
            'scheduled_time': self.scheduled_time,
            'is_done': self.is_done,
            'updated_at': self.updated_at,
            'created_at': self.created_at,
        }
        if exclude_fields:
            for field in exclude_fields:
                result.pop(field)
        return result

    def is_belong_to_user(self, user_id: int):
        return self.user_id == user_id


