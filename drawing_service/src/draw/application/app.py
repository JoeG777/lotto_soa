from fastapi import FastAPI
from src.draw.application.models import LottoDraw
from src.draw.application.drawer import Drawer
from src.draw.application.publisher import Publisher

api = FastAPI()

@api.get("/index")
def index():
    return "Hello World!"

@api.get("/trigger_draw")
def trigger_draw() -> LottoDraw:
    lotto_draw = Drawer.draw()
    Publisher.publish_message(lotto_draw)
    return lotto_draw