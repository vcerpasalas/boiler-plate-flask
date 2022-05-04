from app import db
from flask_jwt_extended import create_access_token, create_refresh_token
from flask import jsonify
from app.models.user_model import UserModel


class AuthController:
    def login(self, data):
        try:
            user = UserModel.where(username=data['username']).first()
            if user:
                if user.checkPassword(data['password']):
                    user_data = user.to_dict()
                    access_token = create_access_token(
                        identity=user_data['id'],
                        fresh=True
                    )
                    refresh_token = create_refresh_token(
                        identity=user_data['id']
                    )
                    return jsonify(
                        access_token=access_token,
                        refresh_token=refresh_token
                    ), 200
                else:
                    raise Exception('La contraseña ingresada es incorrecta')
            
            raise Exception('No se encontro al usuario')
        except Exception as e:
            return self.__error_transaction(e)
        
    def tokenRefresh(self, identity):
        try:
            access_token = create_access_token(
                identity=identity,
                fresh=True
            )
            return jsonify(
                access_token=access_token
            )
        except Exception as e:
            return self.__error_transaction(e)
        
    def __error_transaction(self, error):
        db.session.rollback()
        return {
            'message': str(error)
        }, 500

