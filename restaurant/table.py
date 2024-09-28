from threading import Semaphore
<<<<<<< HEAD
=======

>>>>>>> 34b973768eb1351a7ddf08b6171c6bd324cb088b

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Table:

    """ Inicia a mesa com um número de lugares """
    def __init__(self,number):
        self._number = number
<<<<<<< HEAD
        self.semaphore = Semaphore(number) # semaforo para controle de uso da mesa
=======
        self.seats = Semaphore(value = number)
>>>>>>> 34b973768eb1351a7ddf08b6171c6bd324cb088b
        # Insira o que achar necessario no construtor da classe.
    
    """ O cliente se senta na mesa."""
    def seat(self, client):
<<<<<<< HEAD
        self.semaphore.acquire() # pega um lugar na mesa
    
    """ O cliente deixa a mesa."""
    def leave(self, client):
        self.semaphore.release() # libera um lugar na mesa para outra thread de Client
=======
        self.seats.acquire()
        pass
    
    """ O cliente deixa a mesa."""
    def leave(self, client):
        self.seats.release()
        pass
>>>>>>> 34b973768eb1351a7ddf08b6171c6bd324cb088b
