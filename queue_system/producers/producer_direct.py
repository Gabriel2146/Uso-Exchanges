from queue_system.brokers.rabbitmq_broker import RabbitMQBroker

def main():
    broker = RabbitMQBroker()
    broker.connect()

    message = "Este es un mensaje de prueba."
    broker.publish("direct_logs", "email", message)

    broker.close()

if __name__ == "__main__":
    main()
