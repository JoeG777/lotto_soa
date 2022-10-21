import pytest
from testcontainers.mongodb import MongoDbContainer

from src.customer.application.db_client import db_client
from src.customer.application.models import Bet

# docker run --rm -p 27017:27017 mongo:latest
@pytest.fixture
def mock_config(monkeypatch) -> None:
    test_config = {
            'CONNECTION_STRING': 'mongodb://localhost:27017',
            'COLLECTION': 'user_bets',
            'DB_NAME': 'test'
        }
    monkeypatch.setattr(db_client, "config", test_config)

def test_add_bet(mock_config):
    test_bet = Bet(user="123", winning_numbers=[1,2,3,4,5,6], super_number=[0])
    test_created_object = Bet(**db_client.add_bet(test_bet))
    import pdb; pdb.set_trace()
    assert test_created_object.user == test_bet.user
    assert test_created_object.winning_numbers == test_bet.winning_numbers
    assert test_created_object.super_number == test_bet.super_number

def test_get_bets(mock_config):
    # depends on own implementation
    # setup does not encompass clean up
    test_data = {"user": "123", "winning_numbers": [1,2,3,4,5,6], "super_number":[0]}
    test_objects = [Bet(**db_client.add_bet(Bet(**test_data))) for i in range(0,3)]

    test_result = [Bet(**result) for result in db_client.get_bets()]

    assert len(test_result) == len(test_objects)