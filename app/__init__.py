from apiflask import APIFlask
from flask_praetorian import Praetorian

from app.database.mariadb import init_engine, db_session

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

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app



