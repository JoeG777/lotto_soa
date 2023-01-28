from fastapi import FastAPI, status, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles

from src.customer.application.db_client import db_client
from src.customer.application.models import Bet
from src.customer.exceptions import CustomerServiceException

api = FastAPI(
    title="Customer Service",
    description="",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@api.exception_handler(CustomerServiceException)
async def generic_exception_handler(request: Request, exc: CustomerServiceException) -> JSONResponse:
    return JSONResponse(
        status_code=500, content={"message": f"Something went wrong! - {exc.args[0]}"}
    )


@api.get("/")
async def default_route() -> RedirectResponse:
    return RedirectResponse(
        url="/index", status_code=status.HTTP_307_TEMPORARY_REDIRECT
    )


@api.get("/index")
async def index() -> str:
    return "Hello World!"


@api.post("/add_bet")
async def add_bet(bet_to_add: Bet) -> JSONResponse:
    added_bet = db_client.add_bet(bet_to_add)
    return JSONResponse(
        content=jsonable_encoder(added_bet), status_code=status.HTTP_201_CREATED
    )


@api.get("/show_results")
async def show_results() -> JSONResponse:
    evaluated_bets = db_client.get_bets()
    return JSONResponse(content=jsonable_encoder(evaluated_bets))
