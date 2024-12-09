from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    firstname: str
    lastname: str


class UserUpdate(BaseModel):
    firstname: str | None = None
    lastname: str | None = None


class UserOut(BaseModel):
    id: int
    email: EmailStr
    firstname: str
    lastname: str

    class Config:
        orm_mode = True


class EmailMessage(BaseModel):
    users: list[int]
    message: str
