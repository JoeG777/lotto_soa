from fastapi import FastAPI, Depends
from dataclasses import asdict

from src.draw.domain.models import LottoDraw
from src.draw.domain.i_drawer import IDrawer
from src.draw.adapters.dto import LottoDrawResponse
from src.draw.common.autowire import Autowire


api = FastAPI(
title="Drawing Service",
    description="",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@api.get("/index")
def index() -> str:
    return "Hello World!"


@api.get("/trigger_draw")
def trigger_draw(drawer: IDrawer = Depends(Autowire(IDrawer))) -> LottoDrawResponse:
    lotto_draw: LottoDraw = drawer.draw()
    return LottoDrawResponse(**asdict(lotto_draw))
