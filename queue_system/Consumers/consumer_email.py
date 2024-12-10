from brokers.rabbitmq_broker import RabbitMQBroker

def callback(ch, method, properties, body):
    print(f"Received email notification: {body.decode()}")

def main():
    broker = RabbitMQBroker()
    broker.consume(exchange='notifications_direct', queue='email_notifications', routing_key='email', callback=callback)

if __name__ == "__main__":
    main()
