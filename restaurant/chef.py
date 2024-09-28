# imports do Python
from threading import Thread, Semaphore
from time import sleep
from random import randint
from .shared import (
    get_queue_orders,
    get_clientes
)

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Chef(Thread):
    
    def __init__(self):
        super().__init__()
        self.current_order = None
        self.remaining_orders = None
        self.semaforo = Semaphore(0)

    """ Chef prepara um dos pedido que recebeu do membro da equipe."""
    def cook(self):
        print("[COOKING] - O chefe esta preparando o pedido para a senha {}.".format(self.current_order)) # Modifique para o numero do ticket
        sleep(randint(1,5))

    """ Chef serve o pedido preparado."""
    def serve(self):
        clientes = get_clientes()
        for cliente in clientes:
            if cliente.ticket == self.current_order:
                cliente.semaforo_wait_chef.release()
        print("[READY] - O chefe está servindo o pedido para a senha {}.".format(self.current_order)) # Modificar para o numero do ticket

    """ O chefe espera algum pedido vindo da equipe."""
    def wait_order(self):
        print("O chefe está esperando algum pedido.")
        self.semaforo.acquire()
        self.current_order = get_queue_orders().get()

    """ Thread do chefe."""
    def run(self):
        self.remaining_orders = len(get_clientes())
        while self.remaining_orders > 0:
            self.wait_order()
            self.cook()
            self.serve()
            self.remaining_orders -= 1