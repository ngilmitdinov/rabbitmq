#!/usr/bin/env python

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = conn.channel()

channel.queue_declare(queue='first queue')

channel.basic_publish(exchange='', routing_key='first queue', body='Hello World!')

print "[x] Sent  'Hello World!'"

conn.close()
