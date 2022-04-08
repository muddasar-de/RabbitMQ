import email
import json
import pika
from statistics import mode
import string 
from unicodedata import name
from numpy import busday_offset
from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup
import time
def consume():

    # Step 1: Build Connection.
            
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    # Step 2: Declaring queue.

    channel.queue_declare(queue="Emails")

    dict = {
    "from": [],
    "to": [],
    "subject":[],
    "body":[],
    "date":[]
    }

    # Step 3: declare method that will do processing on consumed message
    def get_email_data(ch,method,properties,body):
        data  = body
        print(type(data))
      
        msg = email.message_from_bytes(data)
        
        # body = msg.get_body(preferencelist=('plain')).get_content()
        # print(type(body))
        # soup = BeautifulSoup(body)
        dict["from"].append(msg['from'])
        dict["to"].append(msg['to'])
        dict["subject"].append(msg['Subject'])
        # dict["body"].append(soup)
        dict["date"].append(msg['date'])
        
        print(dict)
        ch.basic_ack(delivery_tag =method.delivery_tag)

    # Step 4: Get the actuall message from producer.
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="Emails",on_message_callback=get_email_data)

    # Step 5: Start Consuming.

    channel.start_consuming()
    print(dict)

consume()