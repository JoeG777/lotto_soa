from pydantic import BaseModel, Field, validator


class LottoDrawResponse(BaseModel):
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
