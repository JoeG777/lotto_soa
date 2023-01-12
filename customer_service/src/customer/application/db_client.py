from dotenv import dotenv_values
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder

from src.customer.exceptions import CustomerServiceException
from src.customer.application.models import Bet

# TODO: make async
#TODO: depend on config
# TODO: make not "databse" but from config
# TODO: databasemodels and api facings
class DBClient:
    client: MongoClient
    config = dotenv_values(".env")

    def __init__(self):
        self.client = MongoClient(self.config["CONNECTION_STRING"], username="test", password="test")

    def add_bet(self, test_object: Bet):
        new_object = self.client.database[self.config["DB_NAME"]].insert_one(jsonable_encoder(test_object))
        created_object = self.client.database[self.config["DB_NAME"]].find_one(
            {"_id": new_object.inserted_id}
        )
        return created_object

    def get_bets(self) -> list[Bet]:
        bets = list(self.client.database[self.config["DB_NAME"]].find(limit=10))
        if len(bets) == 0:
            raise CustomerServiceException("No entries available")
        return [Bet(**bet) for bet in bets]
    
    def update_bets(self, bets: list[Bet]) -> list[Bet]:
        updated_records: list[Bet] = []
        for bet in bets:
            book_values_to_update = {k:v for k, v in bet.dict().items() if v is not None}
            if len(book_values_to_update) >=1:
                result_update = self.client.database[self.config["DB_NAME"]].update_one(
                    {"_id":bet.id}, {"$set": book_values_to_update}
                )
                if result_update.modified_count == 0:
                    raise Exception(f"No record has been updated on id: {bet._id}")
            if (updated_bet := self.client.database[self.config["DB_NAME"]].find_one({"_id": bet._id})):
                updated_records.append(updated_bet)
        return updated_records
    
    def __del__(self):
        if self.client:
            self.client.close()

db_client = DBClient()
