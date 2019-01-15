#!/usr/bin/env python

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = conn.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(exclusive=True)

queue_name=result.method.queue
print(queue_name)

channel.queue_bind(exchange='logs', queue=queue_name)

print ('[*] Waiting for logs')

def callback(ch, method, properties, body):
    print ("[x] %r" % body)

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
