from dotenv import load_dotenv
from prisma import Prisma
from fastapi import FastAPI
from ebd_planner.routers import church
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager   
from prisma import Prisma

prisma = Prisma()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Conectando ao banco de dados...")
    prisma.connect()  
    app.state.db = prisma
    yield  
    print("🛑 Desconectando do banco de dados...")
    prisma.disconnect() 

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(church.router)


 