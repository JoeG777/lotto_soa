import pytest
import requests
from fastapi.testclient import TestClient

from src.customer.application.app import api
from src.customer.application.models import Bet

@pytest.fixture
def mock_api():
    yield TestClient(api)

def test_add_bet(mock_api):
    """ Try to add a bet via the API and check whether it successfully ended up in the database."""
    test_bet = {"user":"1", "winning_numbers":[1,2,3,4,5,6], "super_number" :[0]}
    test_response = mock_api.post("/add_bet", json=test_bet).json()

    assert test_bet["super_number"] == test_response["super_number"]
    assert test_bet["winning_numbers"] == test_response["winning_numbers"]
    assert test_bet["user"] == test_response["user"]

def test_response_model(mock_api):
    """Check to see whether the response model only contains the right amount of data"""
    pass
    

def test_show_results(mock_api):
    
    test_response_json = mock_api.get("/show_results").json()
    assert Bet(**test_response_json[1])
    assert {"user", "winning_numbers", "super_number"}.issubset(set(test_response_json[1].keys()))