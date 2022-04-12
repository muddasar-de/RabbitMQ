import imp
import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch,mehod, properties, body):
    print("I am first Consumer: {body}")

connection_parameters = pika.ConnectionParameters("localhost")
 
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)

queue = channel.queue_declare(queue="", exclusive=True)

channel.queue_bind(exchange="pubsub", queue=queue.method.queue)

channel.basic_consume(queue=queue.method.queue,auto_ack=True,on_message_callback=on_message_received)

channel.start_consuming()