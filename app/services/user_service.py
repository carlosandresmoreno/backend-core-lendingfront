from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.schemas.user_schema import UserSchema

class UserService:
    @staticmethod
    def create_user(data):
        user = User(**data)
        UserRepository.save(user)
        return UserSchema.dump(user)

    @staticmethod
    def get_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if user:
            return UserSchema.dump(user)
        return None
