import pika
import logging
import os
from src.draw.common import constants
from src.draw.common.configuration import config
from src.draw.application.models import LottoDrawEvent


class Publisher:
    @staticmethod
    def publish_message(drawing_results: LottoDrawEvent) -> None:
        con_params = pika.ConnectionParameters(
            host=os.environ.get("TC_HOST")
            or config.config_map.get("message_broker_host"),
            port=config.config_map.get("message_broker_port"),
        )
        con = pika.BlockingConnection(con_params)
        try:
            channel = con.channel()
            channel.queue_declare(
                constants.DEFAULT_MESSAGE_QUEUE_DRAWING_EVENT, passive=False
            )
            channel.basic_publish(
                exchange="",
                routing_key=constants.DEFAULT_MESSAGE_QUEUE_DRAWING_EVENT,
                body=drawing_results.json(),
            )
            logging.info("Message sent")
        finally:
            con.close()
