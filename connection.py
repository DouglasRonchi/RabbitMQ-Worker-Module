import pika

from config import RabbitConfig

class RabbitConnection:
    def __init__(self, config: RabbitConfig):
        self.config = config
        self.connection = None
        self.channel = None

    def connect(self):
        credentials = pika.PlainCredentials(self.config.user, self.config.password)
        parameters = pika.ConnectionParameters(
            host=self.config.host,
            port=self.config.port,
            virtual_host=self.config.virtual_host,
            credentials=credentials
        )
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def close(self):
        if self.connection:
            self.connection.close()
