import pika;
import os;
import key;

def launch_queue_publish(queue, routing_key, message):
    # Set an environement variable filled with the ampq url
    url = os.environ.get('CLOUDAMQP_URL', key.ampqUrl)
    # Set the AMPQurl to pika
    params = pika.URLParameters(key.ampqUrl)
    params.socket_timeout = 100
    # Create a connection with AMPQ
    connection = pika.BlockingConnection(params)

    chanel = connection.channel()
    #  Declare a queue
    chanel.queue_declare(queue=queue)
    # Send a message to the queue
    chanel.basic_publish(exchange='', routing_key=routing_key, body=message, properties=pika.BasicProperties(
        delivery_mode = 2 # make message persistent
    ))

def publishing_routine(number, exchange, routing_key, body):
    for i in range(number):
        chanel.basic_publish(exchange=exchange, routing_key=routing_key, body=body, properties=pika.BasicProperties(
            delivery_mode = 2 # make message persistent
        ))

