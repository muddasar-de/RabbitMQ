
import pika
from pika.exchange_type import ExchangeType
 
def on_message_received(ch,mehod, properties, body):
    print(f"I am second Consumer: {body}")

connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange="routing", exchange_type=ExchangeType.direct)

queue2 = channel.queue_declare(queue="", exclusive=True)

channel.queue_bind(exchange="routing", queue=queue2.method.queue, routing_key="analyticsonly")

channel.basic_consume(queue=queue2.method.queue,auto_ack=True,on_message_callback=on_message_received)

print("Start Consuming...")
channel.start_consuming()