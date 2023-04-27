#!/usr/bin/env python
import pika
import os

QUEUE_HOST = os.getenv('QUEUE_HOST', 'localhost')
QUEUE_NAME = os.getenv('QUEUE_NAME', 'test')

#Creo la conexion con el broker
connection = pika.BlockingConnection(pika.ConnectionParameters(host=QUEUE_HOST))
channel = connection.channel()

#Declaramos la cola que va a utiliar
channel.queue_declare(queue=QUEUE_NAME)

#Creo la función que va a ejecutarse al recibir un mensaje
def callback(ch, method, properties, body):
    print(" [x] Mensaje recibido %s" % body)

#Configuro la suscripción
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

#Quedo a la escucha de nuevos mensajes
channel.start_consuming()