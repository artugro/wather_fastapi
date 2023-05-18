from fastapi import FastAPI

from api.api import init_api

app: FastAPI = init_api()
