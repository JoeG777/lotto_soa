import pytest
import pika
import os
import logging
from datetime import datetime
from testcontainers.rabbitmq import RabbitMqContainer
from src.draw.application.models import LottoDraw, LottoDrawEvent

from src.draw.application.publisher import Publisher
from src.draw.common import constants

class TestPublisher:
    
    @pytest.fixture(scope="session")
    def rabbitmq_instance(self):
        os.environ["TC_HOST"] = "192.168.0.33"

        with RabbitMqContainer('rabbitmq:3.9', port=constants.DEFAULT_MESSAGE_BROKER_PORT) as rabbitmq:
            connection = pika.BlockingConnection(rabbitmq.get_connection_params())
            os.environ["DRAW_MESSAGE_BROKER_PORT"] = str(rabbitmq.get_connection_params().port)
            channel = connection.channel()
            yield channel
            connection.close()
            logging.debug("Connection closed")
    
    @pytest.fixture
    def check_for_message(self, rabbitmq_instance):
        def inner():
            rabbitmq_instance.queue_declare(constants.DEFAULT_MESSAGE_QUEUE_DRAWING_EVENT, passive=True)
            method_frame, header_frame, body = rabbitmq_instance.basic_get(constants.DEFAULT_MESSAGE_QUEUE_DRAWING_EVENT)
            if method_frame:
                print(method_frame, header_frame, body)
            else:
                print('No message returned')
            return body
        return inner

    #@pytest.xfail
    def test_connection(self, check_for_message):
        test_message = LottoDrawEvent(lotto_draw=LottoDraw(winning_numbers=[1,2,3,4,5,6], super_number=[0]), timestamp=datetime(2022, 1, 1))
        try:
            Publisher.publish_message(test_message)
        except Exception as exc:
            assert False, f"Exception raised although not expected: {exc}"

        #assert test_message == test_result
        assert True
    