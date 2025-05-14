class RabbitConfig:
    def __init__(self, host: str, port: int, user: str, password: str, virtual_host: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.virtual_host = virtual_host
