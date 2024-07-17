import time
from flask import request, jsonify, current_app
from flask_praetorian import auth_required, current_user

from app import guard
from app.api import account_bp
from app.models import User
from app.repository import UserRepository


@account_bp.post('/login')
def login():
    """登入並設定 JWT"""
    json_data = request.json
    username = json_data.get('username')  # demo for refactor: inline
    password = json_data.get('password')  # demo for refactor: inline
    user: User = guard.authenticate(username, password)
    UserRepository().update_last_login_time(user)
    response = jsonify({
                "result": True,
                "data": user.to_dict()
                })
    response.set_cookie(
        current_app.config['JWT_COOKIE_NAME'],
        guard.encode_jwt_token(user),
        expires=time.time() + 86400,
        httponly=True,
        samesite='Lax'
    )
    return response


@account_bp.get('logout')
def logout():
    """登出並清除 JWT"""
    response = jsonify({"result": True, "data": {}})
    response.set_cookie(
        current_app.config['JWT_COOKIE_NAME'],
        '',
        expires=0,
        httponly=True,
        samesite='Lax'
    )
    return response


@account_bp.get("/whoami")
@auth_required
def info_about_current_user():
    """目前登入的使用者資訊"""
    user = current_user()
    return {
        "result": True,
        "data": current_user().to_dict()
    }
