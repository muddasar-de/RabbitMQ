
import pika
from pika.exchange_type import ExchangeType

def msg_from_main_queue(ch,mehod, properties, body):
    print("Main Queue: %r" %body)

def msg_from_alt_queue(ch,mehod, properties, body):
     print("DL Queue: %r" %body)
connection_parameters = pika.ConnectionParameters("localhost")
 
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange="dlx", exchange_type=ExchangeType.fanout)

channel.exchange_declare(exchange="main_exchange", exchange_type=ExchangeType.direct)

channel.queue_declare(queue="main_queue",arguments={"x-dead-letter-exchange":"dlx","x-message-ttl":1000 })

channel.queue_bind(
    exchange="main_exchange",
    queue="main_queue",
    routing_key="test")

# channel.basic_consume(queue="main_queue",auto_ack=True,on_message_callback=msg_from_main_queue)

channel.queue_declare(queue="dlq")

channel.queue_bind(
    exchange="dlx",
    queue="dlq")

channel.basic_consume(queue="dlq",auto_ack=True,on_message_callback=msg_from_alt_queue)

print("Start Consuming...")
channel.start_consuming()
