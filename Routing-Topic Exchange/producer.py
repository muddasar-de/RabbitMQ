import pika
from pika.exchange_type import ExchangeType
connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange="topicrouting", exchange_type=ExchangeType.topic)


message = "Hello, I am sending payment message"
message1 = "Hello, I am sending analytics message"

channel.basic_publish(exchange="topicrouting",routing_key="user.pk.payments",body=message )
channel.basic_publish(exchange="topicrouting",routing_key="user.pk.analytics",body=message1 )


print(f"Sent Message : {message}")

print(f"Sent Message : {message1}")

connection.close()