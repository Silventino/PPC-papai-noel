from threading import Thread, Semaphore, Event
from time import sleep
import random

class Elfo(Thread):
    # Construtor da thread Rena
    def __init__(self, gerenciador, id):
        self.gerenciador = gerenciador
        self.eventoElfosTrabalhando = Event()
        self.id = id
        Thread.__init__(self)
    
    # Laça uma rena, quando o papai noel acordar
    def serAjudado(self):
        self.gerenciador.sem.acquire()

        print('Elfo {:2d} sendo ajudado'.format(self.id))
        self.gerenciador.contadorElfos -= 1

        self.gerenciador.sem.release()

    # Organiza a chegada de cada Rena
    def run(self):
        while(True):
            rand = random.random()
            sleep(rand*5)

            self.gerenciador.porta.acquire()
            self.gerenciador.sem.acquire()

            print('Elfo {:2d} chegou'.format(self.id), end='')

            if self.gerenciador.contadorElfos == 3:
                print('3 elfos esperando: {}'.format(self.gerenciador.filaElfos))
            else:
                self.gerenciador.contadorElfos += 1
                self.gerenciador.filaElfos.append(self.id)
                self.gerenciador.porta.release()

                if self.gerenciador.contadorElfos == 3:
                    print(' terceiro elfo')
                    self.gerenciador.eventoDespertador.set()
                else:
                    print()
                    
            self.gerenciador.sem.release()

            self.eventoElfosTrabalhando.clear()
            self.eventoElfosTrabalhando.wait()
            