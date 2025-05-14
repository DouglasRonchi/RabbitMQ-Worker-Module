class RabbitTopic:
    def __init__(self, channel):
        self.channel = channel

    def add_topic(self, exchange_name: str, exchange_type: str = 'direct'):
        self.channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

    def bind_queue_to_topic(self, queue_name: str, exchange_name: str, routing_key: str):
        self.channel.queue_bind(queue=queue_name, exchange=exchange_name, routing_key=routing_key)
