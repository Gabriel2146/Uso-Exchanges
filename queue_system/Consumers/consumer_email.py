import pika

def callback(ch, method, properties, body):
    print(f"Received email notification: {body.decode()}")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the direct exchange
    channel.exchange_declare(exchange='notifications_direct', exchange_type='direct')

    # Declare a queue and bind it to the exchange with the routing key 'email'
    queue_name = 'email_notifications'
    channel.queue_declare(queue=queue_name)
    channel.queue_bind(exchange='notifications_direct', queue=queue_name, routing_key='email')

    print("Waiting for email notifications. To exit press CTRL+C")
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == "__main__":
    main()
