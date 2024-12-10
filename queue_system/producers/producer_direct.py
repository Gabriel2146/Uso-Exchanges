import sys
from pathlib import Path

# Agregar el directorio raíz al sys.path si no se reconoce automáticamente
root_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(root_dir))

from brokers.rabbitmq_broker import RabbitMQBroker

def main():
    broker = RabbitMQBroker()
    messages = [
        ("email", "Direct Notification: Email message content."),
        ("sms", "Direct Notification: SMS message content."),
    ]

    for routing_key, message in messages:
        broker.publish(exchange='notifications_direct', routing_key=routing_key, message=message)

if __name__ == "__main__":
    main()
