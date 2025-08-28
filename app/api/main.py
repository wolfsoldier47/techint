from fastapi import APIRouter

from api.routes import notes


api_router = APIRouter()
api_router.include_router(notes.router)