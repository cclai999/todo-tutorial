from app import guard
from app.repository.base_repo import BaseOrmRepository
from app.models import User
from app.utility.time_processor import get_local_time


class UserRepository(BaseOrmRepository):
    model = User

    def get_user_by_id(self, form_id: int) -> None | User:
        return self.model.query.filter(User.id == form_id).first()

    def update_last_login_time(self, user: User) -> None:
        user.last_login = get_local_time()
        self.write_into_db(use_flush=False)

    def create_user(self, username='test_user', fullname="test_user", password='1234'):
        user = self.model(
            username=username,
            password=guard.hash_password(password),
            fullname=fullname
        )
        self.write_into_db(use_flush=False, new_records=[user])
        return user
