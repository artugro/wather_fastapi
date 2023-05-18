import os
from fastapi import FastAPI

from api.routes.health import init_health_router
from api.routes.weather import init_weather_router


def init_api() -> FastAPI:
    """
    Constructor for FastAPI instance, here we can wire middleware and routes
    :return FastAPI:
    """

    version = os.environ.get("VERSION", "DEV-SNAPSHOT")
    app = FastAPI(title="ema-service", version=version)
    _init_middleware(app, version)
    _init_routes(app)

    # app.add_event_handler("startup", startup)
    # app.add_event_handler("shutdown", shutdown)

    return app


def _init_middleware(app: FastAPI, version: str) -> None:
    """
    This is for wiring middlewares
    :param app:
    :param version:
    :return None:
    """

    # app.add_middleware()


def _init_routes(app: FastAPI) -> None:
    """
    This is for connecting routes
    :param app:
    :return None:
    """
    app.include_router(init_health_router())
    app.include_router(init_weather_router())
