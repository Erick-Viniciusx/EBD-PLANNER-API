from prisma import Prisma
from http import HTTPStatus
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import APIRouter, Request, HTTPException
from ebd_planner.schemas import UserPublic, UserSchema
from ebd_planner.security import get_password_hash


load_dotenv()
router = APIRouter(prefix='/users', tags=['users'])

@router.post('/', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(request: Request , user: UserSchema):
    db: Prisma = request.app.state.db

    db_user = db.usuario.find_first(where={"email":user.email})

    if db_user:
        if db_user.nome == user.nome:
            raise HTTPException (
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email já existe'
            )
        
    db_user = db.usuario.create(
        data={
            "nome": user.nome,
            "email": user.email,
            "telefone": user.telefone,
            "senha": get_password_hash(user.senha),
            "roleTipo": user.roleTipo
        }
    )

    return db_user