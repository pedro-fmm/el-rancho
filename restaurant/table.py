from threading import Semaphore

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Table:

    """ Inicia a mesa com um número de lugares """
    def __init__(self,number):
        self._number = number
        self.semaphore = Semaphore(number) # semaforo para controle de uso da mesa
        # Insira o que achar necessario no construtor da classe.
    
    """ O cliente se senta na mesa."""
    def seat(self, client):
        self.semaphore.acquire() # pega um lugar na mesa
    
    """ O cliente deixa a mesa."""
    def leave(self, client):
        self.semaphore.release() # libera um lugar na mesa para outra thread de Client
