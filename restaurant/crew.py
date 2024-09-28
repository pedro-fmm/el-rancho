# imports do Python
<<<<<<< HEAD
from threading import Thread, Semaphore
from time import sleep
=======
from threading import Thread, Lock
>>>>>>> 34b973768eb1351a7ddf08b6171c6bd324cb088b

from .shared import (
    get_totem, 
    get_clientes,
    get_queue_totem_call_crew,
    get_queue_orders,
    get_chef
)

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Crew(Thread):
    
    """ Inicia o membro da equipe com um id (use se necessario)."""
    def __init__(self, id, totem):
        super().__init__()
        self._id = id
<<<<<<< HEAD
        self.ticket = None
        self.semaforo = Semaphore(0)
=======
        self.totem = totem
        # Insira o que achar necessario no construtor da classe.
>>>>>>> 34b973768eb1351a7ddf08b6171c6bd324cb088b

    """ O membro da equipe espera um cliente. """    
    def wait(self):
        get_totem().remaining_clients_lock.release()
        print("O membro da equipe {} está esperando um cliente.".format(self._id))
        get_totem().semaforo.acquire()

    """ O membro da equipe chama o cliente da senha ticket."""
    def call_client(self, ticket):
        self.ticket = ticket
        clientes = get_clientes()
        for cliente in clientes:
            if cliente.ticket == ticket:
                cliente.semaforo_wait_crew.acquire()
        print("[CALLING] - O membro da equipe {} está chamando o cliente da senha {}.".format(self._id, ticket))
        self.wait()

    def make_order(self, order):
        self.semaforo.release()
        print("[STORING] - O membro da equipe {} está anotando o pedido {} para o chef.".format(self._id, order))
<<<<<<< HEAD
        get_queue_orders().put(order)
        get_chef().semaforo.release()
        
=======
        self.wait()

>>>>>>> 34b973768eb1351a7ddf08b6171c6bd324cb088b
    """ Thread do membro da equipe."""
    def run(self):
        while True:
            get_totem().remaining_clients_lock.acquire()
            
            remaining_clients = get_totem().get_remaining_clients()
            
            get_totem().decrease_remaining_clients()
            
            if remaining_clients <= 0:
                get_totem().remaining_clients_lock.release()
                break          

            self.wait()

            ticket = get_queue_totem_call_crew().get()[0]
            self.call_client(ticket)
            self.make_order(ticket)