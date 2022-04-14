import pika
from pika.exchange_type import ExchangeType
connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange="first_exchange", exchange_type=ExchangeType.direct)
channel.exchange_declare(exchange="second_exchange", exchange_type=ExchangeType.fanout)

channel.exchange_bind("second_exchange","first_exchange")

message = "Hello, I am passing through first exchange."

channel.basic_publish(exchange="second_exchange",routing_key="",body=message )

print(f"Sent Message : {message}")

connection.close()