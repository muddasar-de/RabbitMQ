from glob import glob
from numpy import meshgrid
import pika
import glob
from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup
import json
import time
# Task: Passing email message from the producer to consumer and handle it by extracting the email header and body.

# Step 1: Build Connection.
            
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

# Step 2: Declaring queue.

channel.queue_declare(queue="Emails")

def produce():
    # Step 1: Loading emails from the local folder.
    list_of_files= glob.glob("./Emails/*.eml")
    print(len(list_of_files))
    for file in list_of_files:
        with open(file, "rb") as fp:
            msg = BytesParser(policy=policy.default).parse(fp)
            # print(type(str(msg)))
            print(msg)
            
            channel.basic_publish(exchange="",routing_key="Emails",body=str(msg))
            # print(str(msg))
            time.sleep(10)
            

produce()