from queue_system.brokers.rabbitmq_broker import RabbitMQBroker
import json

def process_message(ch, method, properties, body):
    message = json.loads(body)
    print(f"Mensaje recibido en Consumer Email: {message}")

def main():
    broker = RabbitMQBroker()
    broker.connect()

    broker.consume("email_queue", process_message)

if __name__ == "__main__":
    main()
