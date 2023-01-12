import asyncio
import json
import os

import aiormq
from src.customer.application.bets_matcher import match_bets
from src.customer.application.db_client import db_client
from src.customer.application.models import LottoDraw


class AsyncRabbitConsumer:

    @classmethod
    async def on_message(cls, message):
        """
        on_message doesn't necessarily have to be defined as async.
        Here it is to show that it's possible.
        """
        print(f" [x] Received message {message!r}")
        print(f"Message body is: {message.body.decode('utf-8')}")
        running_bets = db_client.get_bets()
        evaluated_bets = match_bets(LottoDraw(**json.loads(message.body.decode('utf-8'))['lotto_draw']), running_bets)
        db_client.update_bets(evaluated_bets)
        print("Comparison done")


    @classmethod
    async def async_consume(cls):
        # Perform connection
        connection = await aiormq.connect(f"amqp://{os.environ.get('RABBIT_INIT_ROOT_USERNAME')}:{os.environ.get('RABBIT_INIT_ROOT_PASSWORD')}@{os.environ.get('RABBIT_HOST')}/")
        # Creating a channel
        channel = await connection.channel()

        # Declaring queue
        declare_ok = await channel.queue_declare(os.environ.get("QUEUE_DRAWING_EVENT"))
        consume_ok = await channel.basic_consume(
            declare_ok.queue, cls.on_message, no_ack=True
        )
    
    @classmethod
    def run(cls):
        print("Start Forever loop")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(cls.async_consume())
        loop.run_forever()

if __name__ == '__main__':
    AsyncRabbitConsumer.run()
