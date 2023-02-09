from function import *
inicio = time.time()
if __name__ == '__main__':
    while True:
        visitsCounts = 0
        x = 1
        procesos = []
        datos = visitData()
        visits = int(datos[0])
        tVisits = int(datos[1])
        urls = str(datos[2])
        tVisitsTO = tVisits + 10
        numProcess = 15
        processNum = int(numProcess)
        # cola = Queue()
        # cola.put(visitsCounts)
        # definimos cantidad de procesos
        while x <= processNum:
            proceso1 = Process(target=visitMiner, args=(urls, tVisits,))
            procesos.append(proceso1)
            x += 1
        # Iniciamos procesor
        for proces in procesos:
            proces.start()
            rtime1 = int(random.randint(10, 60))
            rtime = rtime1 / 100
            print(rtime)
            time.sleep(rtime)
        print("Procesos iniciados")
        for fin in procesos:
            fin.join(timeout=tVisitsTO) 
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
        # Cerramos las ventanas de chrome que queden
        os.system("taskkill /f /im chrome.exe")
        if visitsCounts >= visits:
            finT = input("el programa va a finalizar")
            break
fin = time.time()
tiempoFin = (fin - inicio) / 60