#!/usr/bin/env python

import pika
import sys
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = conn.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello world"

channel.basic_publish(exchange='logs', routing_key='', body=message)

print ("[x] Sent  %r" % message)

conn.close()
