import pika
import logging
import os
from src.draw.application.models import LottoDrawEvent


class Publisher:
    @staticmethod
    def publish_message(drawing_results: LottoDrawEvent) -> None:
        con_params = pika.ConnectionParameters(
            host=os.environ.get("RABBIT_HOST"),
            port=os.environ.get("RABBIT_PORT")
        )
        con = pika.BlockingConnection(con_params)
        try:
            channel = con.channel()
            channel.queue_declare(
                os.environ.get("QUEUE_DRAWING_EVENT"), passive=False
            )
            channel.basic_publish(
                exchange="",
                routing_key=os.environ.get("QUEUE_DRAWING_EVENT"),
                body=drawing_results.json(),
            )
            logging.info("Message sent")
        finally:
            con.close()
