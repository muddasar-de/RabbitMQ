from ast import arguments
import pika
from pika.exchange_type import ExchangeType
connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange="headers_exchange", exchange_type=ExchangeType.headers)

message = "Hello, I am passing through headers exchange."

channel.basic_publish(
    exchange="headers_exchange",
    routing_key="",
    body=message,
    properties=pika.BasicProperties(headers={"name":"Muddasar"}) )

print(f"Sent Message : {message}")

connection.close()