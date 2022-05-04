from app import db
from app.models.role_model import RoleModel
from flask import jsonify


class RoleController:
    def all(self):
        records = RoleModel.all()
        return jsonify(
            results=[
                role.to_dict()
                for role in records
            ]
        ), 200
        
    def getById(self, role_id):
        record = RoleModel.where(id=role_id).first()
        if record:
            return jsonify(
                result=record.to_dict()
            ), 200
        return {}, 404 
    
    def create(self, data):
        try:
            new_record = RoleModel.create(**data)
            return self.__result_response(new_record, 201)
        except Exception as e:
            return self.__error_transaction(e)
            
    def update(self, role_id, data):
        try:
            record = RoleModel.where(id=role_id).first()
            if record:
                record.update(**data)
                return self.__result_response(record, 200)
            raise Exception('Rol no encontrado')
        except Exception as e:
            return self.__error_transaction(e)
        
    
    def delete(self, role_id):
        try:
            record = RoleModel.where(id=role_id).first()
            if record:
                record.delete()
                db.session.commit()
                return jsonify(
                    result={
                        'message': f'Rol {role_id} eliminado'
                    }
                )
            raise Exception('Rol no encontrado')
        except Exception as e:
            return self.__error_transaction(e)
            
            
    def __result_response(self, object_data, status_code):
        db.session.add(object_data)
        db.session.commit()
        return jsonify(
            result=object_data.to_dict()
        ), status_code
        
    def __error_transaction(self, error):
        db.session.rollback()
        return {
            'message': str(error)
        }, 500
