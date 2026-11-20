from pydantic import BaseModel, Field



class UserRegister(BaseModel):

    username: str= Field(
        min_length=3,
        max_length=40,
    )
    email: str = Field(
        min_length=5,
        max_length=100,
    )
    password: str = Field(
        min_length=8,
        max_length=80,
    )

class UserLogin(BaseModel):

    username: str=Field(
        min_length=3,
        max_length=40,
    )

    password: str= Field(
        min_length=8,
        max_length=80,
    )