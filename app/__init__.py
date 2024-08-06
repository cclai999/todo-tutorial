from apiflask import APIFlask, HTTPError
from flask_praetorian import Praetorian

from app.database.mariadb import init_engine, db_session
from app.exc.exceptions import AppException

guard = Praetorian()


def create_app(config):
    app = APIFlask(
        __name__,
        version="0.1.0",
        docs_ui="redoc",
        title="Todo List Backend API",
    )
    app.config.from_object(config)
    init_engine(config.DATABASE_URI)

    from app.models import User
    guard.init_app(app, User)

    from app.api import blueprint_list
    for bp in blueprint_list:
        app.register_blueprint(bp)

    app.json.sort_keys = False
    register_page_and_handlers(app)
    return app


def register_page_and_handlers(this_app):
    @this_app.get("/")
    def index_page():
        """後端首頁"""
        return "Welcome to Todo List Backend API"

    @this_app.get('/name/<name>')
    def hello(name):
        """"demo code for HHTPError"""
        if name == 'Foo':
            raise HTTPError(404, 'This man is missing.')
        return f'Hello, {name}!'
    @this_app.errorhandler(AppException)
    def app_exception_handler(e: AppException):
        return e.to_dict(), e.status_code

    @this_app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    @this_app.error_processor
    def my_error_processor(error):
        return {
            'result': False,
            'status_code': error.status_code,
            'error_description': error.message,
            'message': error.detail
        }, error.status_code, error.headers
