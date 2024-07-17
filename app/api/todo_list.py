from datetime import timedelta

from app.api import todo_list_bp
from app.models import Todo
from app.repository import TodoRepository


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
            for item in TodoRepository().get_user_todo_list(current_user()['id'])
        ]
    }
