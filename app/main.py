
from fastapi import FastAPI

from core.config import settings
from fastapi.middleware.cors import CORSMiddleware

from api.main import api_router

import uvicorn

import os
from dotenv import load_dotenv
from logs.logging_middleware import LoggingMiddleware
from db.gibbrish_data import add_dummy_data

load_dotenv('.env')

print('Hello, World! Lets run our server')

DOMAIN = os.getenv("DOMAIN")
PORT = int(os.getenv("PORT", 8000))
WORKERS = int(os.getenv("WORKERS"))
DEBUG = os.getenv("DEBUG")
if DEBUG:
    print("Running in debug mode")
    print("adding dummy data")
    add_dummy_data()





app = FastAPI(
    title=settings.app_name,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.all_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LoggingMiddleware)


app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
  uvicorn.run('main:app', host=DOMAIN, port=PORT, reload=DEBUG, workers=WORKERS)
# app.include_router(api_router, prefex=settings.API_V1_STR)






