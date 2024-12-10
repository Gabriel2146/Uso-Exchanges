import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the direct exchange
    channel.exchange_declare(exchange='notifications_direct', exchange_type='direct')

    messages = [
        ("email", "Direct Notification: Email message content."),
        ("sms", "Direct Notification: SMS message content."),
    ]

    for routing_key, message in messages:
        channel.basic_publish(exchange='notifications_direct', routing_key=routing_key, body=message)
        print(f"Sent: {message} with routing key: {routing_key}")

    connection.close()

if __name__ == "__main__":
    main()
