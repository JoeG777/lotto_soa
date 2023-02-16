import pika
from pydantic import BaseModel, Field, validator
from datetime import datetime

class LottoDraw(BaseModel):
    winning_numbers: list[int] = Field(
        ..., title="Winning Numbers", description="Normal drawn numbers"
    )
    super_number: list[int] = Field(
        ..., title="Super Number", description="", max_items=1, min_items=1
    )

    @validator("winning_numbers")
    def validate_winning_numbers(cls, values: list[int]) -> None:
        if not list(filter(lambda x: x > 0 and x < 50, values)):
            raise ValueError(f"{values} invalid - Choose numbers between 1 and 49")
        return values

    @validator("super_number")
    def validate_super_number(cls, values: list[int]) -> None:
        if not list(filter(lambda x: x >= 0 and x < 10, values)):
            raise ValueError(f"{values} invalid - Choose numbers between 0 and 9")
        return values

class LottoDrawEvent(BaseModel):
    lotto_draw: LottoDraw = Field(
        ..., title="Lotto Draw", description="The object holding the lotto numbers"
    )
    timestamp: datetime = Field(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S%z"),
        title="Timestamp",
        description="Timestamp of the event",
    )

def publish_message():
    con_params = pika.ConnectionParameters(
            host="localhost",
            port=5672
        )
    con = pika.BlockingConnection(con_params)
    channel = con.channel()
    channel.queue_declare(
        "lotto_drawing_event", passive=False
    )
    channel.basic_publish(
        exchange="",
        routing_key="lotto_drawing_event",
        body=LottoDrawEvent(lotto_draw=LottoDraw(winning_numbers=[1,2,3,4,5,6], super_number=[0]), timestamp=datetime(2022, 1, 1)).json()
    )

if __name__ == '__main__':
    print(publish_message())