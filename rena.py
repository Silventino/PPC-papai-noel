from threading import Thread, Semaphore, Event
from time import sleep
import random

class Rena(Thread):
    # Construtor da thread Rena
    def __init__(self, gerenciador, i):
        self.gerenciador = gerenciador
        self.eventoRenaTrabalhando = Event()
        
        self.i = i
        Thread.__init__(self)
    
    # Laça uma rena, quando o papai noel acordar
    def serLacada(self):
        self.gerenciador.contadorRenas -= 1

    # Organiza a chegada de cada Rena
    def run(self):
        while(True):
            sleep(random.uniform(1,7))                                          # cada rena demora entre 1 e 7s para chegar
            self.gerenciador.sem.acquire()                                      # fecha o semaforo    

            print('Rena {:2d} chegou'.format(self.i), end='')

            self.gerenciador.contadorRenas += 1
            self.gerenciador.filaRenas.append(self.i)                           # se coloca na fila

            if self.gerenciador.contadorRenas == 9:                             # se for a ultima rena, acorda o papai noel
                print(' e é a última rena')
                self.gerenciador.sem.release()
                self.gerenciador.semDespertador.acquire()
                self.gerenciador.eventoDespertador.set()
            else:
                print()

            self.gerenciador.sem.release()
            self.eventoRenaTrabalhando.clear()
            self.eventoRenaTrabalhando.wait()
            