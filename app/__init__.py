from apiflask import APIFlask


def create_app(config):
    app = APIFlask(
        __name__,
        version="0.1.0",
        docs_ui="redoc",
        title="Todo List Backend API",
    )
    app.config.from_object(config)
    from app.api import todo_list_bp
    app.register_blueprint(todo_list_bp)
    app.json.sort_keys = False
    return app



