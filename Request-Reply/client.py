import pika
from pika.exchange_type import ExchangeType
import uuid

def on_response_received(ch,mehod, properties, body):
    print("Waiting for response...")
    print("Client received the response: %r" %body)

connection_parameters = pika.ConnectionParameters("localhost")
 
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

request = "Face Detection"

coreId = str(uuid.uuid4)

channel.queue_declare(queue="reply_queue", exclusive=True)

channel.basic_publish(exchange="",routing_key="request_queue",properties=pika.BasicProperties(
    reply_to="reply_queue",
    correlation_id= coreId
), body=request)

channel.basic_consume(queue="reply_queue",auto_ack=True,on_message_callback=on_response_received)

print("Request send is for: %r" %request)

channel.start_consuming()