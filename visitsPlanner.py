# import subprocess
# procesosCant = 2
# x = 1
# subprocess.run("traMiner.py", shell=True)
# subprocess.run("traMiner.py", shell=True)
# while procesosCant >= x:
#     x += 1

from function import *
from multiprocessing import Process
numProcess = 2

if __name__ == '__main__':
    proceso1 = Process(target=visitMiner)
    proceso2 = Process(target=visitMiner)
    proceso3 = Process(target=visitMiner)
    proceso1.start()
    proceso2.start()
