from datetime import datetime, timedelta

from app.utility.time_processor import get_local_time


class TodoItem:
    def __init__(self, id: int, user_id: int, title: str,  scheduled_time: datetime,
                 is_done: bool = False, should_alert: bool = False,
                 ):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.should_alert = should_alert
        self.scheduled_time = scheduled_time
        self.is_done = is_done
        self.updated_at = get_local_time()
        self.created_at = get_local_time()

    def to_dict(self, exclude_fields=None):
        result = {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'should_alert': self.should_alert,
            'scheduled_time': self.scheduled_time,
            'is_done': self.is_done,
            'updated_at': self.updated_at,
            'created_at': self.created_at,
        }
        if exclude_fields:
            for field in exclude_fields:
                result.pop(field)
        return result

    def is_belong_to_user(self, user_id: int):
        return self.user_id == user_id

