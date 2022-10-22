import pytest
from testcontainers.mongodb import MongoDbContainer
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient

from src.customer.application.db_client import db_client
from src.customer.application.models import Bet

@pytest.fixture(scope="session")
def testcontainer():
    with MongoDbContainer("mongo:latest").with_bind_ports(27017, 27017) as mongo:
        print("MongoDB available")
        yield mongo
        print("MongoDB closed")

@pytest.fixture
def mock_config(monkeypatch) -> None:
    test_config = {
            'CONNECTION_STRING': 'mongodb://localhost:27017',
            'COLLECTION': 'user_bets',
            'DB_NAME': 'test'
        }
    monkeypatch.setattr(db_client, "config", test_config)

def insert_for_tests(to_insert: list[Bet]):
    db = MongoClient('mongodb://localhost:27017', username="test", password="test")
    for element in to_insert:
        _ = db.database['test'].insert_one(jsonable_encoder(element))
    db.close()
    return to_insert

def test_add_bet(mock_config, testcontainer):
    test_bet = Bet(user="123", winning_numbers=[1,2,3,4,5,6], super_number=[0])
    test_created_object = Bet(**db_client.add_bet(test_bet))

    assert test_created_object.user == test_bet.user
    assert test_created_object.winning_numbers == test_bet.winning_numbers
    assert test_created_object.super_number == test_bet.super_number

def test_get_bets(mock_config, testcontainer):
    test_data = {"user": "123", "winning_numbers": [1,2,3,4,5,6], "super_number":[0]}
    test_objects = [insert_for_tests([Bet(**test_data)]) for i in range(0,3)]

    test_result = [Bet(**result) for result in db_client.get_bets()]

    assert len(test_result) == len(test_objects)
