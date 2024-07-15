from datetime import timedelta

from app.api import todo_list_bp
from app.models import TodoItem
from app.utility.time_processor import get_local_time

sample_todo_lists = [
    # create 3 sample todo items
    TodoItem(id=1, user_id=0, title="Buy milk", scheduled_time=get_local_time() + timedelta(days=1), is_done=False),
    TodoItem(id=2, user_id=0, title="Pay rent", scheduled_time=get_local_time() + timedelta(days=1), is_done=True),
    TodoItem(id=3, user_id=1, title="Call mom", scheduled_time=get_local_time() + timedelta(days=1), is_done=False)
]


def get_user_todolist_items(user_id: int) -> list[TodoItem]:
    # return [item for item in sample_todo_lists if item.user_id == user_id]
    return [item for item in sample_todo_lists if item.is_belong_to_user(user_id)]


def current_user() -> dict:
    return {'user_name': 'Max', 'id': 0}


@todo_list_bp.get("/all")
@todo_list_bp.doc()
def get_all_todo_list():
    """取得所有待辦事項清單"""
    return {
        "result": True,
        "data": [
            item.to_dict()
            for item in get_user_todolist_items(current_user()['id'])
        ]
    }
