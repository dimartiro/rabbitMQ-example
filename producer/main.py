#!/usr/bin/env python
import pika
import os

QUEUE_HOST = os.getenv('QUEUE_HOST', 'localhost')
QUEUE_NAME = os.getenv('QUEUE_NAME', 'test')

MESSAGES=[
    "TEST 1",
    "TEST 2",
    "TEST 3",
    "TEST 4",
    "TEST 5"
]

#Establecemos una conexion con el broker
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=QUEUE_HOST))
channel = connection.channel()

#Declaramos la cola que va a utiliar
channel.queue_declare(queue=QUEUE_NAME)

for message in MESSAGES:
    #Publico los mensajes en la cola
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=message)
    print("[x] Mensaje enviado: %s " % message)

#Cierro la conexion con la cola
connection.close()