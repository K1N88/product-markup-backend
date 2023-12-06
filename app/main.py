from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from app.api.routers import main_router
from app.core.config import settings
from app.core.init_db import create_first_superuser

import sentry_sdk


sentry_sdk.init(
    dsn="https://cda08122e16ff6d3f6ad7042d07f1a87@o4504084224933888.ingest.sentry.io/4506337137852416",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

origins = ["*"]

app = FastAPI(title=settings.app_title)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(main_router, prefix='/api/v1')
add_pagination(app)


@app.on_event('startup')
async def startup():
    await create_first_superuser()
