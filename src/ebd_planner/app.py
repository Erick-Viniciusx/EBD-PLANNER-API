from dotenv import load_dotenv
from prisma import Prisma
from fastapi import FastAPI
from ebd_planner.routers import church
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(church.router)


 