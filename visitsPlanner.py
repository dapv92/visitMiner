from function import *
visitsCounts = 0
visits = 1000
urls = "https://bit.ly/3l8JzVs"
tVisits = 30
x = 1
procesos = []
inicio = time.time()
if __name__ == '__main__':
    numProcess = input("Cuantos navegadores desea ejecutar simultaneamente: ")
    processNum = int(numProcess)
    while True:
        # cola = Queue()
        # cola.put(visitsCounts)
        # definimos cantidad de procesos
        while x <= processNum:
            proceso1 = Process(target=visitMiner, args=(urls, tVisits,))
            procesos.append(proceso1)
            rtime = random.randint(1, 9)/10
            time.sleep(rtime)
            x += 1
        # Iniciamos procesor
        for proces in procesos:
            proces.start()
        print("Procesos iniciados")
        for fin in procesos:
            fin.join(timeout=tVisits) 
            if fin.is_alive():
                fin.terminate()
        print("fin de proceso")
        # if not cola.empty():
        #     contador = cola.get()
        #     print("Valor final del contador: ", contador)
        # else:
        #     print("La cola está vacía.")
        x = 1
        procesos = []
        visitsCounts += int(numProcess)
        ahora = time.time()
        tActual = (ahora - inicio) / 60
        print("Visitas Actuales: " + str(visitsCounts) + " de: " + str(visits))
        print("Tiempo Actual: ", tActual)
        if visitsCounts >= visits:
            finT = input("el programa va a finalizar")
            break
fin = time.time()
tiempoFin = (fin - inicio) / 60