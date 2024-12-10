import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the fanout exchange
    channel.exchange_declare(exchange='notifications_fanout', exchange_type='fanout')

    message = "General Notification: Hello to all consumers!"
    channel.basic_publish(exchange='notifications_fanout', routing_key='', body=message)
    print(f"Sent: {message}")

    connection.close()

if __name__ == "__main__":
    main()
