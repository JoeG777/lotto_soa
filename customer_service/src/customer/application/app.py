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

@api.get("/add_bet")
async def add_bet(bet: Bet) -> JSONResponse:
    #TODO: 
    bet_to_add = Bet(**{"winning_numbers":[1,2,3,4,5,6], "super_number" :[0]})
    return JSONResponse(content=jsonable_encoder(bet_to_add))

@api.post("/show_results")
async def show_results() -> JSONResponse:
    #TODO:
    return JSONResponse(content=jsonable_encoder("Results"))