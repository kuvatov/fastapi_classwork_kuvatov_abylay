import pydantic
import uvicorn
import fastapi as fa

from tortoise.contrib.fastapi import register_tortoise

from api.router import router
from app.core.exc.handlers import (
    query_params_validation_error_handler,
    request_exception_handler,
    internal_exception_handler
)
from app.core.exc.http import BaseHTTPException

from app.db.conf import TORTOISE_ORM


def setup():
    application = fa.FastAPI()

    application.include_router(router)

    register_tortoise(application, config=TORTOISE_ORM, generate_schemas=True, add_exception_handlers=True)

    application.exception_handler(pydantic.ValidationError) (query_params_validation_error_handler)
    application.exception_handler(BaseHTTPException) (request_exception_handler)
    application.exception_handler(500) (internal_exception_handler)

    return application


app = setup()


def run(**params):
    uvicorn.run(app='api.application:app', host='0.0.0.0', **params)
    