import pika
import json

from src.customer.application.db_client import db_client
from src.customer.application.bets_matcher import match_bets
from src.customer.application.models import LottoDraw

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

result = channel.queue_declare(queue='lotto_drawing_event')
queue_name = result.method.queue

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body.decode('utf-8'))
    running_bets = db_client.get_bets()
    evaluated_bets = match_bets(LottoDraw(**json.loads(body)), running_bets)
    db_client.update_bets(evaluated_bets)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()