import os
from pathlib import Path

from dotenv import dotenv_values

BASE_DIR = Path(__file__).parent.absolute()


def load_configs_from_env_file() -> dict:
    env_file = os.getenv("ENV_FILE", ".env")
    if env_file is None:
        print("找不到環境變數: ENV_FILE，程式將會自動退出。")
        exit(4)
    env_file_absolute_path = BASE_DIR / env_file
    if not env_file_absolute_path.exists():
        print(f"無法讀取指定的檔案於以下路徑: {env_file_absolute_path}。")
        exit(4)
    return dotenv_values(env_file_absolute_path)


envs = load_configs_from_env_file()


class BaseConfig:
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
#   SECRET_KEY = b"\xa1\xfbFx\x99S\x96\xb2e\xea~9G\x00\x8f\xaa7k\xef'\xcc\xff\xae\xf3\xda\x8fb@\xe7c"
    db_path = BASE_DIR / "todo.db"
    DATABASE_URI = f"sqlite:////{db_path}"
    ENGINE_OPTIONS = {}


class TestingConfig(BaseConfig):
    TESTING = True
#    SECRET_KEY = b'c\xee^\xee\x1e\x8b\xa7S\xb1R\xd6`\x12\xc7RU\x88$\xabc\xb7\xc5\xb9\xf7'


class ProductionConfig(BaseConfig):
    pass


CONFIG_MAPPER = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}


def get_config():
    global envs
    if (name := envs.get("APP_MODE", None)) not in CONFIG_MAPPER:
        raise Exception(f"無法找到指定的配置：{name}")
    return CONFIG_MAPPER[envs.get("APP_MODE")]
