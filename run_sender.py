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

n = 0
while n < 10:
    rabbit_main.send_message(message=f'Mensagem teste {n}', routing_key='my_routing_key', exchange='exemplo_topico_1')
    n += 1

