from threading import Thread, Semaphore, Event
from noel import Noel
from rena import Rena
from elfo import Elfo

class Gerenciador:
    # Construtor
    def __init__(self):
        self.numRenas = 9
        self.numElfos = 10

        self.eventoDespertador = Event()        # Esse evento fará o papai noel acordar
        self.sem = Semaphore()                  # Semaforo para controlar os contadores de renas e elfos
        self.porta = Semaphore()                # Semaforo para controlar a entrada de elfos
        self.semDespertador = Semaphore()

        self.contadorRenas = 0
        self.contadorElfos = 0
        self.renas = []                         # Threads de renas
        self.elfos = []                         # Threads de elfos
        self.filaRenas = []                     # Fila de renas que estão prontas para serem laçadas
        self.filaElfos = []                     # Fila de Elfos que estão prontas para serem laçadas

        self.noel = Noel(self)
        self.noel.start()                       # Iniciou a thread do Papai Noel

        for i in range(self.numRenas):
            self.renas.append(Rena(self,i))     # Criou as renas
        
        for i in range(self.numElfos):
            self.elfos.append(Elfo(self,i))     # Criou as elfo
    
    def inspectElfo(self):
        s = 'elfo: ['
        for i in range(len(self.elfos)):
            if self.elfos[i].is_alive():
                b = 'V'
            else:
                b = 'X'
            s += ' {}'.format(b)
        
        s += ' ]'
        print(s)

    def startRenas(self):
        for i in range(self.numRenas):
            self.renas[i].start()

    def startElfos(self):
        for i in range(self.numElfos):
            self.elfos[i].start()
    
    # def joinRenas(self):
    #     for i in range(self.numRenas):
    #         self.renas[i].join()

    