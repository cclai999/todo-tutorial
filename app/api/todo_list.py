from datetime import timedelta
from flask_praetorian import auth_required, current_user

from app.api import todo_list_bp
from app.models import Todo
from app.repository import TodoRepository


@todo_list_bp.get("/all")
@todo_list_bp.doc()
@auth_required
def get_all_todo_list():
    """取得所有待辦事項清單"""
    return {
        "result": True,
        "data": [
            item.to_dict()
            for item in TodoRepository().get_user_todo_list(current_user().id)
        ]
    }
