from app import app
from flask import request
from flask_jwt_extended import jwt_required
from app.controllers.user_controller import UserController

# /users - GET : Traer a todos los usuarios
# /users/id - GET : Trae el usuario que le pertenece dicho id
# /users - POST (Body Request) : Crear un usuario
# /users/id - PUT (Body Request) : Actualizar un usuario
# /users/id - DELETE : Eliminar un usuario

@app.route('/users', methods=['GET'])
@jwt_required(fresh=True)
def usersAll():
    controller = UserController()
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))
    query = request.args.get('q')
    return controller.all(page, per_page, query)


@app.route('/users/<id>', methods=['GET'])
def userById(id):
    controller = UserController()
    return controller.getById(id)


@app.route('/users', methods=['POST'])
def userCreate():
    controller = UserController()
    return controller.create(request.json)


@app.route('/users/<id>', methods=['PUT'])
def userUpdate(id):
    controller = UserController()
    return controller.update(id, request.json)


@app.route('/users/<id>', methods=['DELETE'])
def userDelete(id):
    controller = UserController()
    return controller.delete(id)
