from app.schemas import UserCreate, UserUpdate
from app.repository.user_repository import UserRepository

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user_data: UserCreate):
        return self.user_repo.create_user(user_data)

    def get_user(self, user_id: int):
        return self.user_repo.get_user(user_id)

    def get_all_users(self):
        return self.user_repo.get_all_users()

    def update_user(self, user_id: int, user_data: UserUpdate):
        return self.user_repo.update_user(user_id, user_data)

    def delete_user(self, user_id: int):
        self.user_repo.delete_user(user_id)
