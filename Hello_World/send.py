#!/usr/bin/env python

import pika
import sys
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = conn.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello world"

channel.basic_publish(exchange='', routing_key='task_queue', body=message, properties=pika.BasicProperties(delivery_mode = 2,))

print ("[x] Sent  %r" % message)

conn.close()
