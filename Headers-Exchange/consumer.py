
import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch,mehod, properties, body):
    print("I am first Consumer: %r" %body)

connection_parameters = pika.ConnectionParameters("localhost")
 
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

queue = channel.queue_declare(queue="", exclusive=True)

bind_args={
    'x-match' :"all",
    "name":"Muddasar",
    "age": 23
}

channel.queue_bind(
    exchange="headers_exchange",
    queue=queue.method.queue,
    arguments=bind_args)

channel.basic_consume(queue=queue.method.queue,auto_ack=True,on_message_callback=on_message_received)

print("Start Consuming...")
channel.start_consuming()