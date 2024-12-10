import pika

def callback(ch, method, properties, body):
    print(f"Received general notification: {body.decode()}")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the fanout exchange
    channel.exchange_declare(exchange='notifications_fanout', exchange_type='fanout')

    # Create a temporary queue and bind it to the exchange
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='notifications_fanout', queue=queue_name)

    print("Waiting for general notifications. To exit press CTRL+C")
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == "__main__":
    main()
