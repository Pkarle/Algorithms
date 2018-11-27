import argparse
import simple_queue_publish
import simple_queue_read

parser = argparse.ArgumentParser(description='Read of publish')
parser.add_argument('--read', action='store_true', help='Read Mode')
parser.add_argument('--publish', action='store_true', help='Publish mode')

args = parser.parse_args()
print(args.read)
print(args.publish)

if args.read == True:
    simple_queue_read.launch_queue_read()
if args.publish == True:
    simple_queue_publish.launch_queue_publish('presentation', 'presentation', 'Hello world')