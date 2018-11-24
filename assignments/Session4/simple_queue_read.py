import pika, os, time, key

def read_message(msg):
    """
    brief: Allowing to print body content from incoming message binding to CLOUDamqp
    Args:
        msg: message comming from callback function
    Return: 
        return self
    """

    print(" [x] Received %r "% msg)
    print(" [x] Message Processed, aknowledging (to delete message from the queue)")
    time.sleep(5) # delays for 5 seconds
    print(" Reading process finished ");
    return;

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', key.ampqUrl)
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='presentation') # Declare a queue

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  read_message(body)

# set up subscription on the queue
channel.basic_consume(callback,
  queue='presentation',
  no_ack=True)

# start consuming (blocks)
channel.start_consuming()
connection.close()