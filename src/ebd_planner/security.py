from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from jwt import decode, encode
from jwt.exceptions import PyJWTError
from fastapi import Depends, Request, HTTPException
from fastapi.security import OAuth2PasswordBearer
from prisma import Prisma
from http import HTTPStatus

SECRET_KEY = 'your-secret-key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token')
def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    
    to_encode.update({'exp': expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def get_current_user(
        request: Request,
        token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        db: Prisma = request.app.state.db
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')

        if not email:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception
    
    user_db = db.usuario.find_first(where={'email': email})

    if not user_db:
        raise credentials_exception
    
    return user_db