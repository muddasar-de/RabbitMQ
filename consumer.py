import queue
import json
import pika , os, sys

def main():

# Step 1: Build connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Step 2: Declare Queue

    channel.queue_declare(queue= "queue1")

    # Step 3: Declare callback function to get message

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % json.loads(body))

    # Step 4: Get the actuall message from producer.

    channel.basic_consume(queue='queue1', auto_ack=True, on_message_callback=callback)

    # Step 5: Cosuming Message:

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)