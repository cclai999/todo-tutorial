from app.database.mariadb import write_into_database, db_session


class BaseOrmRepository:
    _instance = None
    model = None
    orm_db_session = db_session

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def write_into_db(use_flush=False, new_records=None):
        return write_into_database(use_flush, new_records)
