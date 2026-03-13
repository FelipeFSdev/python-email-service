from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.routes.email_sender import router as send_email_route

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initiating server.")
    yield
    print("Shutting down server.")


app = FastAPI(lifespan=lifespan)

