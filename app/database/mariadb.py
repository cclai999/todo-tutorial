from math import ceil
from typing import Union, Tuple

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session, declarative_base

from app.exc.exceptions import DatabaseOperationError
# from app.utility.logger import app_logger

engine = None
db_session: Union[Session, scoped_session] = scoped_session(sessionmaker())
Base = declarative_base()
Base.query = db_session.query_property()


def init_engine(uri):
    global engine
    engine = create_engine(uri)
    db_session.configure(bind=engine)
    return engine


def init_db():
    # TODO: 視情況使用此段程式碼建立資料表
    import app.models  # noqa: F401
    Base.metadata.create_all(bind=engine)


def write_into_database(use_flush=False, new_records=None):
    if new_records:
        db_session.add_all(new_records)
    try:
        if use_flush:
            db_session.flush()
        else:
            db_session.commit()
    except Exception as e:
        # app_logger.critical(f"DB Error: {e}")
        print(f"DB Error: {e}")
        db_session.rollback()
        raise DatabaseOperationError(message="Database Error.", exc_val=e)


def pagination(query, page, per_page) -> Tuple[list, int, int]:
    total = query.count()
    return (
        query.limit(per_page).offset((page - 1) * per_page).all(),
        int(ceil(total / float(per_page))) if per_page > 0 else None,
        total
    )
