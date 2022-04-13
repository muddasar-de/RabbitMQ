import pika
from pika.exchange_type import ExchangeType
connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange="routing", exchange_type=ExchangeType.direct)


message = "Hello, I am sending payment message"
message1 = "Hello, I am sending analytics message"

channel.basic_publish(exchange="routing",routing_key="paymentsonly",body=message )
channel.basic_publish(exchange="routing",routing_key="analyticsonly",body=message1 )


print(f"Sent Message : {message}")

print(f"Sent Message : {message1}")

connection.close()