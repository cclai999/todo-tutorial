from app import create_app
from config import get_config, load_configs_from_env_file

app = create_app(config=get_config())


@app.get("/")
def index_page():
    """後端首頁"""
    return "Welcome to Todo List Backend API"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)
