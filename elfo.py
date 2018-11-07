from threading import Thread, Semaphore, Event
from time import sleep
import random

class Elfo(Thread):
    # Construtor da thread Elfo
    def __init__(self, gerenciador, id):
        self.gerenciador = gerenciador
        self.eventoElfosEsperando = Event()
        self.id = id
        Thread.__init__(self)
    
    # É ajudado pelo papai noel quando ele acorda
    def serAjudado(self):
        self.gerenciador.contadorElfos -= 1

    # Organiza a chegada de cada Elfo
    def run(self):
        while(True):

            # cada elfo demora um tempo entre 1 e 20s para pedir ajuda ao papai noel
            sleep(random.uniform(1,20))

            self.gerenciador.porta.acquire()        # fecha a porta
            self.gerenciador.sem.acquire()          # fecha o semaforo

            print('Elfo {:2d} chegou'.format(self.id))

            if self.gerenciador.contadorElfos < 3:      # se ainda não há 3 elfos esperando
                # self.gerenciador.sem.acquire()
                self.gerenciador.contadorElfos += 1
                self.gerenciador.filaElfos.append(self.id)  # entra na fila

                if self.gerenciador.contadorElfos == 3:         # se for o terceiro elfo, acorda o papai noel
                    print('Ultimo elfo, acorda Papai Noel')
                    self.gerenciador.semDespertador.acquire()
                    self.gerenciador.eventoDespertador.set()
                else:
                    self.gerenciador.porta.release()        # libera a porta somente se a fila de elfos nao estiver cheia

            self.gerenciador.sem.release()      

            self.eventoElfosEsperando.clear()
            self.eventoElfosEsperando.wait()
            