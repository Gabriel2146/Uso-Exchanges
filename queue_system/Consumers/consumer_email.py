# consumer_email.py

from queue_system.brokers.rabbitmq_broker import RabbitMQBroker

def process_message(ch, method, properties, body):
    print(f"Recibido mensaje: {body.decode()}")

def main():
    broker = RabbitMQBroker()
    broker.connect()

    # Declarar la cola desde la que vamos a consumir mensajes
    broker.channel.queue_declare(queue="email_queue")

    # Consumir los mensajes de la cola
    broker.channel.basic_consume(queue="email_queue", on_message_callback=process_message, auto_ack=True)

    print("Esperando mensajes...")

    # Iniciar el consumo de los mensajes
    broker.channel.start_consuming()

if __name__ == "__main__":
    main()
