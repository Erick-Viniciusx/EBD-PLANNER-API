from dotenv import load_dotenv
from http import HTTPStatus
from fastapi import APIRouter, Request
from ebd_planner.schemas import ChurchPublic, ChurchSchema, ChurchList


load_dotenv()


router = APIRouter(prefix='/Igreja', tags=['Igreja'])
    
@router.post('/', response_model=ChurchPublic, status_code=HTTPStatus.CREATED)
def create_user(request: Request,church: ChurchSchema):
    db = request.app.state.db
    db_igreja = db.igreja.create(
        data={
            "nome": church.nome,
            "numeroDaArea": church.numero_area,
            "endereco": church.endereco,
            "pastor": church.pastor,
            "superintendente": church.superintendente,
            "tipo": church.tipo
        }
    )

    return db_igreja

@router.get('/', response_model=ChurchList)
def read_users(request: Request):
    db = request.app.state.db
    church = db.igreja.find_many()

    return {'churchs': church}

