# RabbitMQ
## What is RabbitMQ?
RabbitMQ is a message queueing software/ queue manager or message broker. Simply it is a software in which queues are defined, to which applications it will connect in order to transfer messages.  

## When do we use RabbitMQ?
RabbitMQ is used when we want to communicate between two or more applications in order to transfer data or messages.
That is, Publisher and Consumers.	

RabbitMQ uses AMQP: https://www.amqp.org/
The Advanced Message Queuing Protocol (AMQP) is an open standard for passing business messages between applications or organizations.  It connects systems, feeds business processes with the information they need and reliably transmits onward the instructions that achieve their goals.

## Exchange: 
In previous parts of the tutorial we sent and received messages to and from a queue. Now it's time to introduce the full messaging model in Rabbit.
Let's quickly go over what we covered in the previous tutorials:

A producer is a user application that sends messages.

A queue is a buffer that stores messages.

A consumer is a user application that receives messages.


The core idea in the messaging model in RabbitMQ is that the producer never sends any messages directly to a queue. Actually, quite often the producer doesn't even know if a message will be delivered to any queue at all.

Instead, the producer can only send messages to an exchange. An exchange is a very simple thing. On one side it receives messages from producers and the other side it pushes them to queues. The exchange must know exactly what to do with a message it receives. Should it be appended to a particular queue? Should it be appended to many queues? Or should it get discarded. The rules for that are defined by the exchange type.

There are a few exchange types available: direct, topic, headers and fanout. We'll focus on the last one -- the fanout. Let's create an exchange of that type, and call it logs:

Exchange type


Default: pre-declared names

Direct exchange: (Empty string) and amq.direct

Fanout exchange: amq.fanout

Topic exchange: amq.topic

Headers exchange: amq.match (and amq.headers in RabbitMQ)


Besides the exchange type, exchanges are declared with a number of attributes, the most important of which are:

Name

Durability (exchanges survive broker restart)

Auto-delete (exchange is deleted when last queue is unbound from it)

Arguments (optional, used by plugins and broker-specific features)
