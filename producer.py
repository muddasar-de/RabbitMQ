import queue
import pika
import json

# Step 1: Build connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Step 2: Declare Queue

channel.queue_declare(queue= "queue1")

# Step 3: Launch Exchange
object1 = {
    "name": "Muddasar",
    "age" : 25
}
channel.basic_publish(exchange="",routing_key="queue1",body=json.dumps(object1))

# Step 4: Deliver message by closing connection

connection.close()