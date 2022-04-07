import queue
import pika
import json
import time
import random
# Step 1: Build connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Step 2: Declare Queue

channel.queue_declare(queue= "queue1")

objectId = 1
while(True):
    processingTime = random.randint(1,3)
    # Step 3: Message and Launch Exchange
    object1 = {
        "name": "Muddasar",
        "age" : 25,
        "id": objectId
    }
    channel.basic_publish(exchange="",routing_key="queue1",body=json.dumps(object1))
 
    print("Sent Message ID: ",objectId)
    time.sleep(processingTime)
    objectId+=1

    # Step 4: Deliver message by closing connection

    # connection.close()
    # print("Sent Message")