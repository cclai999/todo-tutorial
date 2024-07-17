from datetime import datetime, timedelta

from app.repository.base_repo import BaseOrmRepository
from app.models import Todo
from app.utility.time_processor import get_local_time


class TodoRepository(BaseOrmRepository):
    model = Todo

    def get_todo_by_id(self, query_id: int) -> None | Todo:
        return self.model.query.filter(Todo.id == query_id).first()

    def create_new_todo(
            self, title: str, should_alert: bool, scheduled_time: datetime, user_id: int
    ) -> Todo:
        self.write_into_db(
            new_records=[
                (new_record := Todo(
                    title=title,
                    should_alert=should_alert,
                    scheduled_time=scheduled_time,
                    user_id=user_id
                ))
            ])
        return new_record

    def update_todo_by_id(self, todo_id: int, json_data: dict, user_id: int) -> bool | Todo:
        record = self.model.query.filter(Todo.id == todo_id, Todo.user_id == user_id).first()
        if not record:
            return False
        for key, value in json_data.items():
            setattr(record, key, value)
        self.write_into_db()
        return record

    def update_is_done_to_value(self, todo: Todo, value: bool) -> Todo:
        todo.is_done = value
        self.write_into_db()
        return todo

    def get_today_todo_list(self, user_id: int) -> list[Todo]:
        today_start = get_local_time().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)
        return Todo.query.filter(
            Todo.user_id == user_id,
            Todo.scheduled_time >= today_start,
            Todo.scheduled_time <= today_end
        ).all()

    def get_user_todo_list(self, user_id: int) -> list[Todo]:
        return Todo.query.filter(Todo.user_id == user_id).all()

    def delete_Todo_item(self, item: Todo) -> None:
        self.orm_db_session.delete(item)
        self.write_into_db()
