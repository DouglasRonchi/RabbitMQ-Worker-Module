from config import RabbitConfig
from main import RabbitOrchestrator


config = RabbitConfig(
    host='localhost',
    port=5672,
    user='guest',
    password='guest',
    virtual_host='/'
)

rabbit_main = RabbitOrchestrator(config)

rabbit_main.connect()

rabbit_main.add_queue('exemplo_fila_1')
rabbit_main.add_topic('exemplo_topico_1')

rabbit_main.bind_queue_to_topic('exemplo_fila_1', 'exemplo_topico_1', 'my_routing_key')

def callback(ch, method, properties, body):
    print(f"Mensagem recebida: {body.decode()}")

print("Esperando mensagens...")
rabbit_main.listen_queue('exemplo_fila_1', callback)
