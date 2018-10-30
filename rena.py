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
        # self.gerenciador.sem.acquire()

        # print('Rena {:2d} sendo laçada'.format(self.i))
        self.gerenciador.contadorRenas -= 1

        # self.gerenciador.sem.release()

    # Organiza a chegada de cada Rena
    def run(self):
        while(True):
            rand = random.random()
            sleep(random.uniform(1,7))
            # if(self.gerenciador.sem.acquire(blocking=False)):
            self.gerenciador.sem.acquire()

            print('Rena {:2d} chegou'.format(self.i), end='')

            if self.gerenciador.contadorRenas == 9:
                print('9 renas prontas: {}'.format(self.gerenciador.filaRenas))
            else:
                self.gerenciador.contadorRenas += 1
                self.gerenciador.filaRenas.append(self.i)

                if self.gerenciador.contadorRenas == 9:
                    print(' e é a última rena')
                    self.gerenciador.sem.release()
                    self.gerenciador.semDespertador.acquire()
                    self.gerenciador.eventoDespertador.set()
                else:
                    print()

            self.gerenciador.sem.release()
            self.eventoRenaTrabalhando.clear()
            self.eventoRenaTrabalhando.wait()
            