#!/usr/bin/env python

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = conn.channel()

channel.queue_declare(queue='first queue')

def callback(ch, method, properties, body):
    print ("[x] Recieved %r" % body)

print '[*] Waiting for messages'

channel.basic_consume(callback, queue='first queue', no_ack=True)

channel.start_consuming()

