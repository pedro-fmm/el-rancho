# imports do Python
<<<<<<< HEAD
from threading import Thread, Semaphore
=======
from threading import Thread, Lock
>>>>>>> 34b973768eb1351a7ddf08b6171c6bd324cb088b
from time import sleep
from random import randint

# imports do projeto
from .shared import (
    get_table,
    get_totem,
    get_funcionarios
)

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Client(Thread):
    
    """ Inicializa o cliente."""
    def __init__(self, i, totem, table):
        self._id = i
<<<<<<< HEAD
        self.ticket = None
        self.semaforo_wait_crew = Semaphore(0)
        self.semaforo_wait_chef = Semaphore(0)
=======
        self.totem = totem
        self.ticket_lock = Lock()
        self.table = table
>>>>>>> 34b973768eb1351a7ddf08b6171c6bd324cb088b
        super().__init__()

    """ Pega o ticket do totem."""
    def get_my_ticket(self):
        self.ticket_lock.acquire()
        self.totem.get_ticket()
        self.ticket_lock.release()
        print("[TICKET] - O cliente {} pegou o ticket.".format(self._id))
        self.ticket = get_totem().get_ticket() 

    """ Espera ser atendido pela equipe. """
    def wait_crew(self):
        print("[WAIT] - O cliente {} esta aguardando atendimento.".format(self._id))
        self.semaforo_wait_crew.release()

    """ O cliente pensa no pedido."""
    def think_order(self):
        print("[THINK] - O cliente {} esta pensando no que pedir.".format(self._id))
        sleep(randint(1,5))

    """ O cliente faz o pedido."""
    def order(self):
        funcionarios = get_funcionarios()
        for funcionario in funcionarios:
            if funcionario.ticket == self.ticket:
                funcionario.semaforo.acquire()
        print("[ORDER] - O cliente {} pediu algo.".format(self._id))

    """ Espera pelo pedido ficar pronto. """
    def wait_chef(self):
        print("[WAIT MEAL] - O cliente {} esta aguardando o prato.".format(self._id))
        self.semaforo_wait_chef.acquire()
    
    """
        O cliente reserva o lugar e se senta.
        Lembre-se que antes de comer o cliente deve ser atendido pela equipe, 
        ter seu pedido pronto e possuir um lugar pronto pra sentar. 
    """
    def seat_and_eat(self):
        print("[WAIT SEAT] - O cliente {} esta aguardando um lugar ficar livre".format(self._id))
<<<<<<< HEAD
        table = get_table()
        table.seat(self)
=======
        self.table.seat()
>>>>>>> 34b973768eb1351a7ddf08b6171c6bd324cb088b
        print("[SEAT] - O cliente {} encontrou um lugar livre e sentou".format(self._id))
        sleep(randint(1,5))

    """ O cliente deixa o restaurante."""
    def leave(self):
<<<<<<< HEAD
        table = get_table()
        table.leave(self)
=======
        self.table.leave()
>>>>>>> 34b973768eb1351a7ddf08b6171c6bd324cb088b
        print("[LEAVE] - O cliente {} saiu do restaurante".format(self._id))
    
    """ Thread do cliente """
    def run(self):
        self.get_my_ticket()
        self.wait_crew()
        self.think_order()
        self.order()
        self.wait_chef()
        self.seat_and_eat()
        self.leave()