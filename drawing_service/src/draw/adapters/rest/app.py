from fastapi import FastAPI

from src.draw.adapters.dto import LottoDrawResponse
from src.draw.domain.i_drawer import IDrawer
from src.draw.application.drawer import Drawer


api = FastAPI(
title="Drawing Service",
    description="",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


@api.get("/index")
def index():
    return "Hello World!"


@api.get("/trigger_draw")
def trigger_draw() -> LottoDrawResponse:
    lotto_draw: IDrawer = Drawer().draw()
    return lotto_draw