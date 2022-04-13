import pika
from pika.exchange_type import ExchangeType
connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)

channel.exchange_declare(exchange="pubsub1", exchange_type=ExchangeType.fanout)

message = "Hello, I am Producer"

channel.basic_publish(exchange="pubsub",routing_key="",body=message)

print(f"Sent Message : {message}")
 
connection.close()