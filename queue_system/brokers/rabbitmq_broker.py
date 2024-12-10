import pika
from brokers.message_broker import MessageBroker

class RabbitMQBroker(MessageBroker):
    def __init__(self, host='localhost'):
        self.host = host

    def _connect(self):
        return pika.BlockingConnection(pika.ConnectionParameters(self.host))

    def publish(self, exchange: str, routing_key: str, message: str):
        connection = self._connect()
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='direct')
        channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)
        print(f"Sent: {message} to exchange: {exchange} with routing key: {routing_key}")
        connection.close()

    def consume(self, exchange: str, queue: str, routing_key: str, callback):
        connection = self._connect()
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='direct')
        channel.queue_declare(queue=queue)
        channel.queue_bind(exchange=exchange, queue=queue, routing_key=routing_key)
        channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
        print(f"Waiting for messages in queue: {queue}. To exit press CTRL+C")
        channel.start_consuming()
