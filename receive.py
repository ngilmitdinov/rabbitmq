#!/usr/bin/env python

from math import log
import pika
import time

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = conn.channel()

channel.queue_declare(queue='first queue')

def callback(ch, method, properties, body):
    print ("[x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")

print '[*] Waiting for messages'

channel.basic_consume(callback, queue='first queue', no_ack=True)

channel.start_consuming()

