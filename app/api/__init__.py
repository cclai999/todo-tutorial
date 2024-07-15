from apiflask import APIBlueprint

todo_list_bp = APIBlueprint('api', __name__, tag='Todo List', url_prefix='/todo_list')

from app.api import todo_list
