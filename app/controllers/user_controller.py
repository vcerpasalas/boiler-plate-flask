from app import db
from app.models.user_model import UserModel
from flask import jsonify


class UserController:
    def all(self, page, per_page, query):
        filters = {}
        
        if query:
            filters['name__ilike'] = f'%{query}%'
        
        records = UserModel.where(**filters).paginate(
            per_page=per_page, page=page
        ) # SELECT * FROM users WHERE name ilike '%na%'
        return jsonify(
            results=[
                row.to_dict(
                    nested=True,
                    exclude=['rol_id']
                ) 
                for row in records.items
            ],
            pagination={
                'totalRecords': records.total,
                'totalPages': records.pages,
                'perPage': records.per_page,
                'currentPage': records.page 
            }
        ), 200 # records.fetchall()
        
    def getById(self, user_id):
        # UserModel.query.get(id) # SELECT * FROM users WHERE id = id
        # UserModel.query.filter_by(id=id).first() # fetchone()
        record = UserModel.where(id=user_id).first()
        if record:
            return jsonify(
                result=record.to_dict(
                    nested=True,
                    exclude=['rol_id']
                )
            ), 200
        return {}, 404 
    
    def create(self, data):
        try:
            new_record = UserModel.create(**data) #key=value, key2=value2
            new_record.hashPassword()
            return self.__result_response(new_record, 201)
        except Exception as e:
            return self.__error_transaction(e)
            
    def update(self, user_id, data):
        try:
            record = UserModel.where(id=user_id).first()
            if record:
                record.update(**data)
                if 'password' in data:
                    record.hashPassword()
                return self.__result_response(record, 200)
            raise Exception('Usuario no encontrado')
        except Exception as e:
            return self.__error_transaction(e)
        
    
    def delete(self, user_id):
        try:
            record = UserModel.where(id=user_id).first()
            if record:
                record.delete()
                db.session.commit()
                return jsonify(
                    result={
                        'message': f'Usuario {user_id} eliminado'
                    }
                )
            raise Exception('Usuario no encontrado')
        except Exception as e:
            return self.__error_transaction(e)
            
            
    def __result_response(self, object_data, status_code):
        db.session.add(object_data)
        db.session.commit()
        return jsonify(
            result=object_data.to_dict(
                nested=True,
                exclude=['rol_id']
            )
        ), status_code
        
    def __error_transaction(self, error):
        db.session.rollback()
        return {
            'message': str(error)
        }, 500
