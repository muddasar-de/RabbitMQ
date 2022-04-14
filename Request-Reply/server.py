import pika
from pika.exchange_type import ExchangeType

def on_request_received(ch,method, properties, body):
    print("Client received the response: %r" %body)
    response = "There are two faces detected"
    ch.basic_publish(exchange="",routing_key=properties.reply_to, body=response)
    print(f"Sent response : {response}")

connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue="request_queue")

channel.basic_consume(queue="request_queue", auto_ack=True,on_message_callback=on_request_received)

channel.start_consuming()