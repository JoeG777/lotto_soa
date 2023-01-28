import os
from pymongo import MongoClient
from typing import Any
from fastapi.encoders import jsonable_encoder

from src.customer.exceptions import CustomerServiceException
from src.customer.application.models import Bet


class DBClient:
    client: MongoClient
    database_name: str
    collection_name: str

    def __init__(self) -> None:
        self.client = MongoClient(
            f"mongodb://{os.environ.get('MONGO_HOST')}:{os.environ.get('MONGO_PORT')}",
            username=os.environ.get("MONGO_INITDB_ROOT_USERNAME"),
            password=os.environ.get("MONGO_INITDB_ROOT_PASSWORD"),
        )
        self.database_name = os.environ.get("CUSTOMER_DATABASE_NAME") or "lotto"
        self.collection_name = os.environ.get("CUSTOMER_COLLECTION_NAME") or "bets"

    def add_bet(self, test_object: Bet) -> dict[str, Any]:
        new_object = self.client[self.database_name][
            self.collection_name
        ].insert_one(jsonable_encoder(test_object))
        created_object = self.client[self.database_name][
            self.collection_name
        ].find_one({"_id": new_object.inserted_id})
        return created_object

    def get_bets(self) -> list[Bet]:
        bets = list(
            self.client[self.database_name][
                self.collection_name
            ].find(limit=10)
        )
        if len(bets) == 0:
            raise CustomerServiceException("No entries available")
        return [Bet(**bet) for bet in bets]

    def update_bets(self, bets: list[Bet]) -> list[Bet]:
        updated_records: list[Bet] = []
        for bet in bets:
            book_values_to_update = {
                k: v for k, v in bet.dict().items() if v is not None
            }
            if len(book_values_to_update) >= 1:
                result_update = self.client[self.database_name][
                    self.collection_name
                ].update_one({"_id": bet.id}, {"$set": book_values_to_update})
                if result_update.modified_count == 0:
                    # TODO: fails if some records are still in the database
                    print(f"No record has been updated on id: {bet.id}")
                    # raise Exception(f"No record has been updated on id: {bet.id}")
            if updated_bet := self.client[self.database_name][
                self.collection_name
            ].find_one({"_id": bet.id}):
                updated_records.append(updated_bet)
        return updated_records

    def __del__(self) -> None:
        try:
            if self.client:
                self.client.close()
        except AttributeError:
            print("No client to close")


db_client = DBClient()
