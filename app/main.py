from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from app.api.routers import main_router
from app.core.config import settings
from app.core.init_db import create_first_superuser


origins = [
    "http://frontend:3000",
]

app = FastAPI(title=settings.app_title)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(main_router)
add_pagination(app)

@app.on_event('startup')
async def startup():
    await create_first_superuser()
