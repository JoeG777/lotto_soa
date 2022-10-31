from fastapi import FastAPI
from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
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
async def add_bet(bet: Bet) -> JSONResponse: 
    bet_to_add = bet
    # added_bet = db_client.add_bet(bet_to_add)
    return JSONResponse(content=jsonable_encoder(bet_to_add))

@api.get("/show_results")
async def show_results() -> JSONResponse:
    evaluated_bets = [Bet(**{"user":"1", "winning_numbers":[1,2,3,4,5,6], "super_number" :[0]}) for i in range(3)]
    # evaluated_bets = db_client.get_bets()
    return JSONResponse(content=jsonable_encoder(evaluated_bets))