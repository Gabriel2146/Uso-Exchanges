from queue_system.brokers.rabbitmq_broker import RabbitMQBroker
import json

def main():
    # Crear la instancia del broker y conectar
    broker = RabbitMQBroker()
    broker.connect()

    # El mensaje que se va a publicar
    message = {"text": "Este es un mensaje de prueba para Direct Exchange"}

    # Publicar el mensaje en el exchange 'direct_logs' con routing_key 'email'
    broker.publish("direct_logs", "email", message)

if __name__ == "__main__":
    main()
