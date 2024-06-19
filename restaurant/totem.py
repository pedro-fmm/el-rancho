# imports do Python
from random import randint
from threading import Thread, Lock

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Totem:

    def __init__(self, number_of_clients):
        super().__init__()
        self.already_sampled = list()
        self.maximum_ticket_number = number_of_clients * 5
        self.call = list()
        self.call_lock = Lock()
        # Insira o que achar necessario no construtor da classe.

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

    """ Insira sua sincronização."""
    def call_crew(self):
        self.call_lock.acquire()
        ticket = min(self.call)
        self.call.pop(ticket)
        print("[CALLING] - O totem chamou a equipe para atender o pedido da senha {}.".format(self.already_sampled[-1]))
        self.call_lock.release()
        #crew->call_client
