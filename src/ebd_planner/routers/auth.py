from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, Request, HTTPException
from ebd_planner.schemas import Token
from dotenv import load_dotenv
from prisma import Prisma
from ebd_planner.security import create_access_token, verify_password

load_dotenv()
router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/token', response_model=Token)
def login_user(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    db: Prisma = request.app.state.db
    user = db.usuario.find_first(where={'email': form_data.username})

    if not user or not verify_password(form_data.password, user.senha):
        raise HTTPException(
            status_code=400, detail='Email ou senha incorreto'
        )
    
    access_token = create_access_token(data={'sub': user.email })

    return {'access_token': access_token, 'token_type': 'Bearer'}