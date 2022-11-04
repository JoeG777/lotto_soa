import pytest
from pymongo import MongoClient
import requests
from testcontainers.mongodb import MongoDbContainer
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder

from src.customer.application.app import api
from src.customer.application.db_client import db_client
from src.customer.application.models import Bet

@pytest.fixture
def mock_config(monkeypatch) -> None:
    test_config = {
            'CONNECTION_STRING': 'mongodb://localhost:27017',
            'COLLECTION': 'user_bets',
            'DB_NAME': 'test'
        }
    monkeypatch.setattr(db_client, "config", test_config)

@pytest.fixture
def test_client():
    yield TestClient(api)

@pytest.fixture(scope="session", autouse=True)
def testcontainer():
    with MongoDbContainer("mongo:latest").with_bind_ports(27017, 27017) as mongo:
        print("MongoDB available")
        yield mongo
        print("MongoDB closed")

def check_for_id_in_db(id):
    client = MongoClient(db_client.config["CONNECTION_STRING"], username="test", password="test")
    created_object = client.database[db_client.config["DB_NAME"]].find_one(
            {"_id": id}
        )
    return created_object

def insert_for_tests(to_insert: list[Bet]):
    db = MongoClient('mongodb://localhost:27017', username="test", password="test")
    for element in to_insert:
        _ = db.database['test'].insert_one(jsonable_encoder(element))
    db.close()
    return to_insert

#TODO: check for available infra
@pytest.mark.e2e_testing
def test_e2e_add_bet(mock_config, test_client):
    """Test the '/add_bet' endpoint end-to-end by inserting a bet via the endpoint and then checking if it is present in the database
    """
    test_bet = Bet(user="123", winning_numbers=[1,2,3,4,5,6], super_number=[0])
    test_created_object = test_client.post("/add_bet", json=jsonable_encoder(test_bet)).json()

    assert test_created_object['user'] == test_bet.user
    assert test_created_object['winning_numbers'] == test_bet.winning_numbers
    assert test_created_object['super_number'] == test_bet.super_number
    assert check_for_id_in_db(test_created_object['_id'])

@pytest.mark.e2e_testing
def test_e2e_show_results(mock_config, test_client):
    test_data = {"user": "123", "winning_numbers": [1,2,3,4,5,6], "super_number":[0]}
    test_objects = [insert_for_tests([Bet(**test_data)]) for i in range(0,3)]
    test_result = test_client.get("/show_results")
    import pdb; pdb.set_trace()
    test_result = [Bet(**result) for result in test_result.json()]

    assert len(test_result) == len(test_objects)+1 # TODO: dependent on previous test
