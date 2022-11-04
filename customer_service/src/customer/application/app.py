from fastapi import FastAPI
from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles

from src.customer.application.db_client import db_client
from src.customer.application.models import Bet

api = FastAPI()

api.mount("/static", StaticFiles(directory="src/customer/templates"))

@api.get("/")
async def default_route():
    return RedirectResponse(url="/index", status_code=status.HTTP_307_TEMPORARY_REDIRECT)

@api.get("/index")
async def index():
    return "Hello World!"

@api.post("/add_bet")
async def add_bet(bet_to_add: Bet) -> JSONResponse: 
    added_bet = db_client.add_bet(bet_to_add)
    return JSONResponse(content=jsonable_encoder(added_bet), status_code=status.HTTP_201_CREATED)

@api.get("/show_results")
async def show_results() -> JSONResponse:
    evaluated_bets = db_client.get_bets()
    return JSONResponse(content=jsonable_encoder(evaluated_bets))