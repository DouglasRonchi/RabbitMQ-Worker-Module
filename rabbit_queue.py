class RabbitQueue:
    def __init__(self, channel):
        self.channel = channel

    def add_queue(self, queue_name: str):
        self.channel.queue_declare(queue=queue_name, durable=True)

    def delete_queue(self, queue_name: str):
        self.channel.queue_delete(queue=queue_name)
