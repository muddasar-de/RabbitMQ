from ast import arguments
import pika
from pika.exchange_type import ExchangeType
import time
connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange="headers_exchange", exchange_type=ExchangeType.headers)
count = 1
while(True):
    message = f"Hello, I am passing through headers exchange.{count}"

    channel.basic_publish(
        exchange="headers_exchange",
        routing_key="",
        body=message,
        properties=pika.BasicProperties(headers={"name":"Muddasr", "age":25}) )
    count = count+1
    time.sleep(2)
    print(f"Sent Message : {message}")

# connection.close()