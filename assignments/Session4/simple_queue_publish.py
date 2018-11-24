import pika;
import os;
import key;

# Set an environement variable filled with the ampq url
url = os.environ.get('CLOUDAMQP_URL', key.ampqUrl)
# Set the AMPQurl to pika
params = pika.URLParameters(key.ampqUrl)
params.socket_timeout = 100
# Create a connection with AMPQ
connection = pika.BlockingConnection(params)

chanel = connection.channel()
#  Declare a queue
chanel.queue_declare(queue='presentation')
# Send a message to the queue
chanel.basic_publish(exchange='', routing_key='presentation', body="Damien", properties=pika.BasicProperties(
    delivery_mode = 2 # make message persistent
))