from dotenv import load_dotenv
from prisma import Prisma
from fastapi import FastAPI
from ebd_planner.routers import church


app = FastAPI()

app.include_router(church.router)


 