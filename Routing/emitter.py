#!/usr/bin/env python

import pika
import sys
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = conn.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[1:]) or "info: Hello world"

channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)

print ("[x] Sent %r:%r" % (severity, message))

conn.close()
