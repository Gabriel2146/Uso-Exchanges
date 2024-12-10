import pika

class RabbitMQBroker:
    def __init__(self):
        self.connection = None
        self.channel = None

    def connect(self):
        try:
            # Usar las credenciales personalizadas
            credentials = pika.PlainCredentials('GabrielP', '2146')  # Cambiado aquí
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    'localhost', 
                    5672,  # Puerto por defecto
                    '/',    # Vhost predeterminado
                    credentials  # Usar las nuevas credenciales
                )
            )
            self.channel = self.connection.channel()
            print("Conexión a RabbitMQ exitosa.")
        except Exception as e:
            print(f"Error al conectar a RabbitMQ: {e}")

    def publish(self, exchange, routing_key, message):
        try:
            # Asegurarse de que el exchange existe
            self.channel.exchange_declare(exchange=exchange, exchange_type='direct')

            # Publicar el mensaje en el exchange
            self.channel.basic_publish(
                exchange=exchange,
                routing_key=routing_key,
                body=message
            )
            print(f"Mensaje publicado en el exchange {exchange} con routing_key {routing_key}")
        except Exception as e:
            print(f"Error al publicar el mensaje: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")
