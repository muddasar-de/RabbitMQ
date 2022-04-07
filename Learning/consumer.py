from itertools import count
import queue
import json
import pika , os, sys
import time
import random
def main():

# Step 1: Build connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Step 2: Declare Queue

    channel.queue_declare(queue= "queue1")

    # Step 3: Declare callback function to get message

    def callback(ch, method, properties, body):
        processingTime = random.randint(1,5)
        msg = json.loads(body)
        print(" Message : %r" % msg)
        time.sleep(processingTime)
        ch.basic_ack(delivery_tag =method.delivery_tag)
    # Step 4: Get the actuall message from producer.

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='queue1',  on_message_callback=callback)

    # Step 5: Cosuming Message:

    
    channel.start_consuming()
    print('Message recieved')
main()