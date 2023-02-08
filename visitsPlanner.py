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
x = 1
if __name__ == '__main__':
    while x <= numProcess:
        proceso = Process(target=visitMiner)
        proceso.start()
        x += 1