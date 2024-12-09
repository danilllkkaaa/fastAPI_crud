from fastapi import FastAPI, HTTPException, Depends
from .models import Base, engine
from .repository.user_repository import UserRepository
from app.schemas import UserCreate, UserUpdate, UserOut, EmailMessage
from app.services.user_service import UserService
from app.services.email_service import EmailService

app = FastAPI()

# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

# Репозитории и сервисы
user_repository = UserRepository()
user_service = UserService(user_repository)
email_service = EmailService()


@app.post("/user", response_model=UserOut)
def create_user(user: UserCreate):
    return user_service.create_user(user)


@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/users", response_model=list[UserOut])
def get_users():
    return user_service.get_all_users()


@app.put("/users/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserUpdate):
    return user_service.update_user(user_id, user)


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    user_service.delete_user(user_id)
    return {"message": "User deleted successfully"}


@app.post("/send_email")
def send_email(email_data: EmailMessage):
    email_service.send_email_task(email_data)
    return {"message": "Emails are being sent asynchronously"}

