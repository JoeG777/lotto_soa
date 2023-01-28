from pydantic import BaseModel, Field, validator
from datetime import datetime
import uuid

from src.customer.common import constants


class LottoDraw(BaseModel):
    winning_numbers: list[int] = Field(
        ..., title="Winning Numbers", description="Normal drawn numbers"
    )
    super_number: list[int] = Field(
        ..., title="Super Number", description="", max_items=1, min_items=1
    )

    @validator("winning_numbers")
    def validate_winning_numbers(cls, values: list[int]) -> list[int]:
        if not list(filter(lambda x: x > 0 and x < 50, values)):
            raise ValueError(f"{values} invalid - Choose numbers between 1 and 49")
        return values

    @validator("super_number")
    def validate_super_number(cls, values: list[int]) -> list[int]:
        if not list(filter(lambda x: x >= 0 and x < 10, values)):
            raise ValueError(f"{values} invalid - Choose numbers between 0 and 9")
        return values


class Bet(LottoDraw):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user: str = Field(
        ...,
        title="Username",
        description="The name of the user the bet is registered with",
    )
    timestamp: datetime = Field(
        datetime.now().strftime(constants.TIMESTAMP_FORMAT),
        title="Timestamp",
        description="Timestamp of the event",
    )
    winning_class: int = Field(
        None,
        title="Winnging Class",
        description="The Winning Class this bet resides in after been matched with a LottoDraw",
    )
