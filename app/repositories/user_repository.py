from app.extensions import db
from app.models.user import User

class UserRepository:
    @staticmethod
    def save(user):
        """Guarda un nuevo usuario en la base de datos"""
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()  # Si ocurre un error, hace rollback
            raise Exception(f"Error al guardar el usuario: {str(e)}")

    @staticmethod
    def get_by_id(user_id):
        """Obtiene un usuario por su ID"""
        try:
            return User.query.get(user_id)
        except Exception as e:
            raise Exception(f"Error al obtener el usuario con ID {user_id}: {str(e)}")

    @staticmethod
    def get_all():
        """Obtiene todos los usuarios"""
        try:
            return User.query.all()
        except Exception as e:
            raise Exception(f"Error al obtener todos los usuarios: {str(e)}")

    @staticmethod
    def delete(user):
        """Elimina un usuario de la base de datos"""
        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error al eliminar el usuario: {str(e)}")

    @staticmethod
    def update(user):
        """Actualiza un usuario en la base de datos"""
        try:
            db.session.commit()  # Suponiendo que los cambios ya se han realizado en el objeto `user`
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error al actualizar el usuario: {str(e)}")
