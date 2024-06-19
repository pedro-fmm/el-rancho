# imports do Python
from threading import Thread, Lock
from time import sleep
from random import randint

# imports do projeto

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Client(Thread):
    
    """ Inicializa o cliente."""
    def __init__(self, i, totem, table):
        self._id = i
        self.totem = totem
        self.ticket_lock = Lock()
        self.table = table
        super().__init__()
        # Insira o que achar necessario no construtor da classe.

    """ Pega o ticket do totem."""
    def get_my_ticket(self):
        self.ticket_lock.acquire()
        self.totem.get_ticket()
        self.ticket_lock.release()
        print("[TICKET] - O cliente {} pegou o ticket.".format(self._id))

    """ Espera ser atendido pela equipe. """
    def wait_crew(self):
        print("[WAIT] - O cliente {} esta aguardando atendimento.".format(self._id))

    
    """ O cliente pensa no pedido."""
    def think_order(self):
        print("[THINK] - O cliente {} esta pensando no que pedir.".format(self._id))
        sleep(randint(1,5))

    """ O cliente faz o pedido."""
    def order(self):
        print("[ORDER] - O cliente {} pediu algo.".format(self._id))

    """ Espera pelo pedido ficar pronto. """
    def wait_chef(self):
        print("[WAIT MEAL] - O cliente {} esta aguardando o prato.".format(self._id))
    
    """
        O cliente reserva o lugar e se senta.
        Lembre-se que antes de comer o cliente deve ser atendido pela equipe, 
        ter seu pedido pronto e possuir um lugar pronto pra sentar. 
    """
    def seat_and_eat(self):
        print("[WAIT SEAT] - O cliente {} esta aguardando um lugar ficar livre".format(self._id))
        self.table.seat()
        print("[SEAT] - O cliente {} encontrou um lugar livre e sentou".format(self._id))
        sleep(randint(1,5))

    """ O cliente deixa o restaurante."""
    def leave(self):
        self.table.leave()
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