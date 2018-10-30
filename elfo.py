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
        # self.gerenciador.sem.acquire()

        # print('Elfo {:2d} sendo ajudado'.format(self.id))
        self.gerenciador.contadorElfos -= 1

        # self.gerenciador.sem.release()

    # Organiza a chegada de cada Elfo
    def run(self):
        while(True):
            # sleep(0.5)
            rand = random.random()
            # sleep(rand*5)
            sleep(random.uniform(1,7))


            # if(self.gerenciador.porta.acquire(blocking=False) and self.gerenciador.sem.acquire(blocking=False)):
            self.gerenciador.porta.acquire()
            self.gerenciador.sem.acquire()

            print('Elfo {:2d} chegou'.format(self.id))

            # print('Elfos esperando: {}'.format(self.gerenciador.contadorElfos))

            if self.gerenciador.contadorElfos < 3:
                # self.gerenciador.sem.acquire()
                self.gerenciador.contadorElfos += 1
                self.gerenciador.filaElfos.append(self.id)

                if self.gerenciador.contadorElfos == 3:
                    print('Ultimo elfo, acorda Papai Noel')
                    self.gerenciador.eventoDespertador.set()
                else:
                    self.gerenciador.porta.release()
            # else:
                # print('Fila cheia')

            # print('filaElfos: {}'.format(self.gerenciador.filaElfos))

            self.gerenciador.sem.release()

            # print()
            self.eventoElfosTrabalhando.clear()
            self.eventoElfosTrabalhando.wait()
            







            # if self.gerenciador.contadorElfos == 3:
            #     print("entreiiiii")
            #     print('3 elfos esperando: {}'.format(self.gerenciador.filaElfos))
            # else:
            #     self.gerenciador.contadorElfos += 1
            #     self.gerenciador.filaElfos.append(self.id)
            #     self.gerenciador.porta.release()

            #     if self.gerenciador.contadorElfos == 3:
            #         print(' terceiro elfo')
            #         self.gerenciador.eventoDespertador.set()
            #     else:
            #         print()
            
            # print(self.gerenciador.filaElfos)
                    
            # self.gerenciador.sem.release()

            # self.eventoElfosTrabalhando.clear()
            # self.eventoElfosTrabalhando.wait()
            