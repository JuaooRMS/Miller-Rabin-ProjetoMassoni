import sys
import os

sys.path.append(os.path.abspath("../algoritmo"))

from miller_rabin import *
import matplotlib.pyplot as plt
import time
import random

def gerar_numero_aleatorio(n_digitos):
    return random.randint(pow(10, n_digitos-1), pow(10, n_digitos) - 1)


tamanhos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tempos = []

for tam in tamanhos:
    n = gerar_numero_aleatorio(tam)
    soma_tempos = 0

    for _ in range(1000):
        inicio = time.perf_counter()
        miller_rabin(n, 20)
        soma_tempos += (time.perf_counter() - inicio)

    tempos.append(soma_tempos/1000)


plt.plot(tamanhos, tempos)
plt.show()



