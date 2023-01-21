from fastapi import FastAPI
from datetime import datetime

from src.draw.application.models import LottoDraw, LottoDrawEvent
from src.draw.application.drawer import Drawer
from src.draw.application.publisher import Publisher

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
def trigger_draw() -> LottoDraw:
    lotto_draw: LottoDraw = Drawer.draw()
    Publisher.publish_message(LottoDrawEvent(lotto_draw=lotto_draw, timestamp=datetime.now()))
    return lotto_draw