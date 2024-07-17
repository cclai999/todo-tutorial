from apiflask import APIBlueprint

todo_list_bp = APIBlueprint('api', __name__, tag='Todo List', url_prefix='/todo_list')
account_bp = APIBlueprint('account_api', __name__, tag='Account', url_prefix='/account')

blueprint_list = [todo_list_bp, account_bp]

from app.api import todo_list, account
