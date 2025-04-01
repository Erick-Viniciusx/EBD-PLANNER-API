from prisma import Prisma
from http import HTTPStatus
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import APIRouter, Request, HTTPException, Depends
from ebd_planner.schemas import UserPublic, UserSchema
from ebd_planner.security import get_password_hash, get_current_user



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

@router.put('/{user_id}', response_model=UserPublic)
def update_user(
    user_id: int,
    user: UserSchema,
    request: Request,
    current_user=Depends(get_current_user), 
):
    db: Prisma = request.app.state.db
    if current_user.id != user_id:
        raise HTTPException(status_code=400, detail='Not enough permissions')
    
    ...
