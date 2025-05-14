from config import RabbitConfig
from connection import RabbitConnection
from message import RabbitMessage
from rabbit_queue import RabbitQueue
from topic import RabbitTopic
from dead_letter import RabbitDeadLetter

class RabbitOrchestrator:
    def __init__(self, config: RabbitConfig):
        self.config = config
        self.connection = RabbitConnection(config)
        self.message = None
        self.queue = None
        self.topic = None
        self.dead_letter = None
        self.__connection_error_message = "RabbitMQ connection is not established. Please call connect() method first."

    def connect(self):
        self.connection.connect()
        self.message = RabbitMessage(self.connection.channel)
        self.queue = RabbitQueue(self.connection.channel)
        self.topic = RabbitTopic(self.connection.channel)
        self.dead_letter = RabbitDeadLetter(self.connection.channel)

    def send_message(self, message: str, queue_name: str = None, exchange: str = None, routing_key: str = None):
        if not self.connection.channel:
            raise Exception(self.__connection_error_message)
        self.message.send_message(queue_name, message, exchange, routing_key)

    def listen_queue(self, queue_name: str, callback):
        if not self.connection.channel:
            raise Exception(self.__connection_error_message)
        self.message.listen_queue(queue_name, callback)

    def add_queue(self, queue_name: str):
        if not self.connection.channel:
            raise Exception(self.__connection_error_message)
        self.queue.add_queue(queue_name)

    def delete_queue(self, queue_name: str):
        if not self.connection.channel:
            raise Exception(self.__connection_error_message)
        self.queue.delete_queue(queue_name)

    def add_topic(self, exchange_name: str, exchange_type: str = 'direct'):
        if not self.connection.channel:
            raise Exception(self.__connection_error_message)
        self.topic.add_topic(exchange_name, exchange_type)

    def bind_queue_to_topic(self, queue_name: str, exchange_name: str, routing_key: str):
        if not self.connection.channel:
            raise Exception(self.__connection_error_message)
        self.topic.bind_queue_to_topic(queue_name, exchange_name, routing_key)

    def re_send_dead_letter(self, dead_letter_queue: str, target_queue: str):
        if not self.connection.channel:
            raise Exception(self.__connection_error_message)
        self.dead_letter.re_send_dead_letter(dead_letter_queue, target_queue)

    def close(self):
        self.connection.close()
