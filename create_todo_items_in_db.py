from datetime import timedelta

from app import create_app
from app.database.mariadb import init_db
from app.utility.time_processor import get_local_time
from config import get_config
from app.models import Todo
from app.database.mariadb import db_session


app = create_app(config=get_config())


def create_sample_todos():
    db_session.add(Todo(
                    title="Buy milk",
                    should_alert=False,
                    scheduled_time=get_local_time() + timedelta(days=1),
                    user_id=1
                    ))
    db_session.add_all([
        Todo(
            title="Pay rent",
            should_alert=True,
            scheduled_time=get_local_time() + timedelta(days=2),
            user_id=1,
            is_done=True
        ),
        Todo(
            title="Call mom",
            should_alert=False,
            scheduled_time=get_local_time() + timedelta(days=3),
            user_id=2
        )
    ])
    db_session.commit()


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
    need_to_create_sample_todos = input("Do you want to create sample todo items? (y/n): ")
    if need_to_create_sample_todos.lower() == "y":
        create_sample_todos()
        print("Todo items created successfully.")