import pytest
import os
from dotenv import load_dotenv
from testcontainers.mongodb import MongoDbContainer
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient

load_dotenv("../.env")

from src.customer.application.db_client import db_client
from src.customer.application.models import Bet

TEST_CONNECTION_STRING = f"mongodb://localhost:{os.environ.get('MONGO_PORT')}"

@pytest.fixture(scope="session")
def testcontainer():
    with MongoDbContainer("mongo:6.0.3").with_bind_ports(os.environ.get("MONGO_PORT"), os.environ.get("MONGO_PORT")) as mongo:
        print("MongoDB available")
        yield mongo
        print("MongoDB closed")

def insert_for_tests(to_insert: list[Bet]):
    db = MongoClient(TEST_CONNECTION_STRING, username=os.environ.get('MONGO_INITDB_ROOT_USERNAME'), password=os.environ.get('MONGO_INITDB_ROOT_PASSWORD'))
    for element in to_insert:
        _ = db[os.environ.get("CUSTOMER_DATABASE_NAME")][os.environ.get('CUSTOMER_COLLECTION_NAME')].insert_one(jsonable_encoder(element))
    db.close()
    return to_insert

def test_add_bet(testcontainer):
    test_bet = Bet(user="123", winning_numbers=[1,2,3,4,5,6], super_number=[0])
    test_created_object = Bet(**db_client.add_bet(test_bet))

    assert test_created_object.user == test_bet.user
    assert test_created_object.winning_numbers == test_bet.winning_numbers
    assert test_created_object.super_number == test_bet.super_number

def test_get_bets(testcontainer):
    test_data = {"user": "123", "winning_numbers": [1,2,3,4,5,6], "super_number":[0]}
    test_objects = [insert_for_tests([Bet(**test_data)]) for i in range(0,3)]

    test_result = db_client.get_bets()

    assert len(test_result) == len(test_objects)+1 # TODO: dependent on previous test

def test_update_bet():
    pass