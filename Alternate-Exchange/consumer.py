
import pika
from pika.exchange_type import ExchangeType

def msg_from_main_queue(ch,mehod, properties, body):
    print("Main Queue: %r" %body)

def msg_from_alt_queue(ch,mehod, properties, body):
     print("Alt Queue: %r" %body)
connection_parameters = pika.ConnectionParameters("localhost")
 
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

main_queue = channel.queue_declare(queue="", exclusive=True)

alt_queue = channel.queue_declare(queue="", exclusive=True)

channel.exchange_declare(exchange="altexchange", exchange_type=ExchangeType.fanout)

channel.exchange_declare(exchange="mainexchange", exchange_type=ExchangeType.direct,arguments={"alternate-exchange":"altexchange"})

channel.queue_bind(
    exchange="mainexchange",
    queue=main_queue.method.queue,
    routing_key="tests")

channel.basic_consume(queue=main_queue.method.queue,auto_ack=True,on_message_callback=msg_from_main_queue)

channel.queue_bind(
    exchange="altexchange",
    queue=alt_queue.method.queue)

channel.basic_consume(queue=alt_queue.method.queue,auto_ack=True,on_message_callback=msg_from_alt_queue)

print("Start Consuming...")
channel.start_consuming()