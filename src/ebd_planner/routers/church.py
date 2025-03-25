from dotenv import load_dotenv
from http import HTTPStatus
from prisma import Prisma
from fastapi import APIRouter
from ebd_planner.schemas import ChurchPublic, ChurchSchema, ChurchList


load_dotenv()
db = Prisma()


router = APIRouter(prefix='/Igreja', tags=['Igreja'])
    
@router.post('/', response_model=ChurchPublic, status_code=HTTPStatus.CREATED)
def create_user(church: ChurchSchema):
    db.connect()
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

    db.disconnect()
    return db_igreja


@router.get('/', response_model=ChurchList)
def read_users():
    db.connect()
    church = db.igreja.find_many()

    db.disconnect()
    return {'churchs': church}

