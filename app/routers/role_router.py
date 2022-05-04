from app import app
from flask import request
from app.controllers.role_controller import RoleController


@app.route('/roles', methods=['GET'])
def rolesAll():
    controller = RoleController()
    return controller.all()


@app.route('/roles/<id>', methods=['GET'])
def roleById(id):
    controller = RoleController()
    return controller.getById(id)


@app.route('/roles', methods=['POST'])
def roleCreate():
    controller = RoleController()
    return controller.create(request.json)


@app.route('/roles/<id>', methods=['PUT'])
def roleUpdate(id):
    controller = RoleController()
    return controller.update(id, request.json)


@app.route('/roles/<id>', methods=['DELETE'])
def roleDelete(id):
    controller = RoleController()
    return controller.delete(id)
