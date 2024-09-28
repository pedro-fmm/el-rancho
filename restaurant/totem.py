# imports do Python
from random import randint
<<<<<<< HEAD
from threading import Semaphore, Lock
from .shared import get_queue_totem_call_crew
=======
from threading import Thread, Lock
>>>>>>> 34b973768eb1351a7ddf08b6171c6bd324cb088b

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Totem:

    def __init__(self, number_of_clients):
        super().__init__()
        self.already_sampled = list()
        self.maximum_ticket_number = number_of_clients * 5
        self.call = list()
<<<<<<< HEAD
        self.semaforo = Semaphore(0) # semaforo para o crew esperar um cliente pedir um ticket
        self.call_lock = Lock()
        self.remaining_clients = number_of_clients # usado para controlar o numero de clientes atendidos, evita que crew fique esperando apos todos clientes serem chamados
        self.remaining_clients_lock = Lock() # protege a variavel anterior
=======
        self.call_lock = Lock()
        # Insira o que achar necessario no construtor da classe.
>>>>>>> 34b973768eb1351a7ddf08b6171c6bd324cb088b

    """ 
        A função get_ticket não pode ser alterada. 
        Ela garante que um ticket aleatório (não repetido) seja criado e que a equipe seja chamada para atendê-lo.
    """
    def get_ticket(self):
        
        # Gera um ticket aleatório
        ticket_number = randint(1, self.maximum_ticket_number)   

        # Garante que o ticket não foi chamado anteriormente
        while ticket_number in self.already_sampled:
            ticket_number = randint(1, self.maximum_ticket_number)
        self.already_sampled.append(ticket_number)

        # Adiciona o ticket na lista de chamadas
        self.call.append(ticket_number)

        self.call_crew()

        return ticket_number    
    
    def get_remaining_clients(self):
        return self.remaining_clients
    
    def decrease_remaining_clients(self):
        self.remaining_clients -= 1

    """ Insira sua sincronização."""
<<<<<<< HEAD
    def call_crew(self): 
        self.call_lock.acquire()
        ticket = min(self.call)
        self.call.remove(ticket)
        get_queue_totem_call_crew().put((ticket, ticket, )) # insere uma tupla pois é uma priority queue, usando o numero de ticket como prioridade
        self.semaforo.release() # libera um acesso ao semaforo de totem
        self.call_lock.release() 
        # print("[CALLING] - O totem chamou a equipe para atender o pedido da senha {}.".format(self.already_sampled[-1]))
        print("[CALLING] - O totem chamou a equipe para atender o pedido da senha {}".format(self.already_sampled[-1]))

=======
    def call_crew(self):
        self.call_lock.acquire()
        ticket = min(self.call)
        self.call.pop(ticket)
        print("[CALLING] - O totem chamou a equipe para atender o pedido da senha {}.".format(self.already_sampled[-1]))
        self.call_lock.release()
        #crew->call_client
>>>>>>> 34b973768eb1351a7ddf08b6171c6bd324cb088b
