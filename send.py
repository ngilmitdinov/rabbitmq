#!/usr/bin/env python

import pika
import sys
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = conn.channel()

channel.queue_declare(queue='first queue')

message = ' '.join(sys.argv[1:]) or "Hello world"

channel.basic_publish(exchange='', routing_key='first queue', body=message)

print ("[x] Sent  %r" % message)

conn.close()
