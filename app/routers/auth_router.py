from app import app
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.auth_controller import AuthController


@app.route('/auth/login', methods=['POST'])
def authLogin():
    controller = AuthController()
    return controller.login(request.json)


@app.route('/auth/token/refresh', methods=['POST'])
@jwt_required(refresh=True)
def authTokenRefresh():
    identity = get_jwt_identity()
    controller = AuthController()
    return controller.tokenRefresh(identity)
