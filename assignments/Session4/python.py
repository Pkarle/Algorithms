import pika;
import os;
import key;

# Set an environement variable filled with the ampq url
url = os.environ.get('CLOUDAMQP_URL', key.ampqUrl)

credentials = pika.credentials.PlainCredentials(key.user, key.password, erase_on_connect=False)

params = pika.URLParameters(key.ampqUrl)
params.socket_timeout = 100

connection = pika.BlockingConnection(params)

chanel = connection.channel()
chanel.queue_declare(queue='hello')
chanel.basic_publish(exchange='', routing_key='hello', body="Hello world")

print('[*] Waiting for messages. to exit press CTRL + C')

connection.close()
