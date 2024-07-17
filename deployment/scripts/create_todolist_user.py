from app import guard, create_app
from app.database.mariadb import db_session
import app.models as models
from config import get_config


def main():
    create_app(get_config())
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username and password:
        user = models.User(
            username=username,
            password=guard.hash_password(password),
            fullname=username,
            roles="admin"
        )
        db_session.add(user)
        db_session.commit()
        print("User created successfully.")
        return True
    print("Username and password are required.")
    return False


if __name__ == "__main__":
    main()
