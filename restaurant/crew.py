# imports do Python
from threading import Thread, Lock


"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Crew(Thread):
    
    """ Inicia o membro da equipe com um id (use se necessario)."""
    def __init__(self, id, totem):
        super().__init__()
        self._id = id
        self.totem = totem
        # Insira o que achar necessario no construtor da classe.

    """ O membro da equipe espera um cliente. """    
    def wait(self):
        print("O membro da equipe {} está esperando um cliente.".format(self._id))

    """ O membro da equipe chama o cliente da senha ticket."""
    def call_client(self, ticket):
        print("[CALLING] - O membro da equipe {} está chamando o cliente da senha {}.".format(self._id, ticket))
        self.wait()

    def make_order(self, order):
        print("[STORING] - O membro da equipe {} está anotando o pedido {} para o chef.".format(self._id, order))
        self.wait()

    """ Thread do membro da equipe."""
    def run(self):
        self.wait()
        self.call_client(0)
        self.make_order(0)