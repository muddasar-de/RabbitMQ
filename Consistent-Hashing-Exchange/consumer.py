
import pika
from pika.exchange_type import ExchangeType

def on_message1_received(ch,mehod, properties, body):
    print("Message from  1st queue: %r" %body)

def on_message2_received(ch,mehod, properties, body):
    print("Message from  2nd queue: %r" %body)
connection_parameters = pika.ConnectionParameters("localhost")
 
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

queue1 = channel.queue_declare(queue="", exclusive=True)

queue2 = channel.queue_declare(queue="", exclusive=True)

channel.queue_bind(
    exchange="hashing_exchange",
    queue=queue1.method.queue,
    routing_key="4")

channel.basic_consume(queue=queue1.method.queue,auto_ack=True,on_message_callback=on_message1_received)

channel.queue_bind(
    exchange="hashing_exchange",
    queue=queue2.method.queue,
    routing_key="1")

channel.basic_consume(queue=queue2.method.queue,auto_ack=True,on_message_callback=on_message2_received)

print("Start Consuming...")
channel.start_consuming()