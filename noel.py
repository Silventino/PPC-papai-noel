from threading import Thread, Semaphore, Event
from time import sleep

class Noel(Thread):
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador
        Thread.__init__(self)
    
    # Funcao chamada quando 9 renas estao prontas
    def ajudaRenas(self):
        print('\tAjudando renas')
        for j in self.gerenciador.filaRenas:
            self.gerenciador.renas[j].serLacada()                       # Lançando cada rena
            sleep(0.273)
        # print('\tRenas laças')

        print("\tFoi entregar os brinquedo")
        sleep(3)
        print("\tVoltou da entrega de brinquedos")

        for j in self.gerenciador.filaRenas:
            self.gerenciador.renas[j].eventoRenaTrabalhando.set()       # Soltando cada rena
        
        self.gerenciador.filaRenas.clear()                              # Limpa a fila de renas

    def ajudaElfos(self):
        print('\tAjudando elfos')
        for j in self.gerenciador.filaElfos:
            self.gerenciador.elfos[j].serAjudado()                       # Lançando cada rena
            sleep(0.273)
        # print('\tElfos ajudados')

        print("\tSe reunindo com os Elfos")
        sleep(1)
        print("\tVoltou da reunião")

        for j in self.gerenciador.filaElfos:
            self.gerenciador.elfos[j].eventoElfosTrabalhando.set()       # Soltando cada elfo
        
        self.gerenciador.porta.release()
        self.gerenciador.filaElfos.clear()                              # Limpa a fila de renas

    def run(self):
        while True:
            print('\tNoel está dormindo')
            self.gerenciador.eventoDespertador.wait()                   # Papai Noel espera até alguém acordar ele
            print('\tNoel acordou')

            self.gerenciador.sem.acquire()
            numRenas = self.gerenciador.contadorRenas
            numElfos = self.gerenciador.contadorElfos

            if(numRenas == 9):
                self.ajudaRenas()                                           # Laça as renas
            if(numElfos == 3):
            # else:
                self.ajudaElfos()
            self.gerenciador.sem.release()
            
            self.gerenciador.eventoDespertador.clear()                  # Reseta o evento de despertar o papai Noel


