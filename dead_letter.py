class RabbitDeadLetter:
    def __init__(self, channel):
        self.channel = channel

    def re_send_dead_letter(self, dead_letter_queue: str, target_queue: str):
        self.channel.basic_get(queue=dead_letter_queue, auto_ack=True)
        message = self.channel.basic_get(queue=dead_letter_queue, auto_ack=True)
        if message:
            self.channel.basic_publish(
                exchange='',
                routing_key=target_queue,
                body=message.body
            )
