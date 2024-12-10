import pika
import json
from queue_system.brokers.message_broker import MessageBroker

class RabbitMQBroker(MessageBroker):
    def __init__(self):
        self.connection = None
        self.channel = None

    def connect(self):
        """Conectar a RabbitMQ."""
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
            self.channel = self.connection.channel()
            print("Conexión establecida con RabbitMQ.")
        except Exception as e:
            print(f"Error al conectar a RabbitMQ: {e}")
            raise

    def publish(self, exchange, routing_key, message):
        """Publicar un mensaje a un exchange especificado."""
        try:
            self.channel.exchange_declare(exchange=exchange, exchange_type='direct' if routing_key else 'fanout')
            self.channel.basic_publish(
                exchange=exchange,
                routing_key=routing_key,
                body=json.dumps(message)
            )
            print(f"Mensaje publicado en {exchange} con routing_key {routing_key}.")
        except Exception as e:
            print(f"Error al publicar el mensaje: {e}")

    def consume(self, queue, callback):
        """Consumir mensajes de una cola."""
        try:
            # Asegurarse de que la cola esté declarada antes de consumir
            self.channel.queue_declare(queue=queue, durable=True)  # durable=True asegura que la cola sobreviva a reinicios
            print(f"Esperando mensajes de la cola: {queue}...")
            self.channel.basic_consume(
                queue=queue,
                on_message_callback=lambda ch, method, properties, body: callback(ch, method, properties, body),
                auto_ack=True  # Auto-confirmar recepción de los mensajes
            )
            self.channel.start_consuming()
        except Exception as e:
            print(f"Error al consumir mensajes: {e}")
            raise
