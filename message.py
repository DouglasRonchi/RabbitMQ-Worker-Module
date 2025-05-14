class RabbitMessage:
    def __init__(self, channel):
        self.channel = channel

    def send_message(self, queue_name: str = '', message: str = '', exchange: str = '', routing_key: str = ''):
        if exchange != '':
            # Send message to a Topic
            self.channel.basic_publish(
                exchange=exchange,
                routing_key=routing_key,
                body=message
            )
        else:
            # Send message to a Queue
            self.channel.basic_publish(
                exchange='',
                routing_key=queue_name,
                body=message
            )

    def listen_queue(self, queue_name: str, callback):
        self.channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
            auto_ack=True
        )
        self.channel.start_consuming()
