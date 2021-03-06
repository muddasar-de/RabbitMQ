from ast import arguments
import pika
from pika.exchange_type import ExchangeType
connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange="hashing_exchange", exchange_type="x-consistent-hash")

message = "Hello, I am passing through hashing exchange."

hashing_key = "Muddasar"

channel.basic_publish(
    exchange="hashing_exchange",
    routing_key= hashing_key,
    body=message )

print(f"Sent Message : {message}")

connection.close()