import sqlite3

from fastapi import FastAPI, HTTPException, status


from app.models import UserRegister, UserLogin
from app.database import create_user, get_user_by_username
from app.security import hash_password, verify_password
app = FastAPI(title="SafeBank API",
              description='edukacyjny symulator bankowosci',
              version='0.1.0',)


@app.post(
    '/auth/register',
    status_code=status.HTTP_201_CREATED
)
def register(user: UserRegister):
    password_hash = hash_password(user.password)

    try:
        created_user = create_user(
            username=user.username,
            email=user.email,
            password_hash=password_hash,
        )
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='username lub email jest juz zajety'
        )
    return created_user

@app.post('/auth/login')
def user_login(data: UserLogin):

    user = get_user_by_username(data.username)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail='unathourised'
        )
    if not verify_password(data.password, user['password_hash']):
        raise HTTPException(
            status_code=401,
            detail='unathourised'
    )

    return user

