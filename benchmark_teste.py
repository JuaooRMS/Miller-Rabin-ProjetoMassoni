import matplotlib.pyplot as plt
import numpy as np
import time
import random
from teste_algoritmo import *

def gerar_array(tamanho):
    rng = np.random.default_rng()
    return rng.integers(low=0, high=11, size=tamanho)

tamanhos_x = [1000, 5000, 10000]
tempos_y_quick = []
tempos_y_bubble = []

for n in tamanhos_x:
    array = gerar_array(n)

    inicio = time.perf_counter()
    quick_sort(array, 0, len(array) - 1)
    tempos_y_quick.append(time.perf_counter() - inicio)

    inicio = time.perf_counter()
    bubble_sort(array)
    tempos_y_bubble.append((time.perf_counter() - inicio))

plt.title("Comparacao de algoritmos de sort")
plt.plot(tamanhos_x, tempos_y_quick, label="QUICK SORT")
plt.plot(tamanhos_x, tempos_y_bubble, label="BUBBLE SORT")
plt.xlabel("Tamanho do array")
plt.ylabel("Tempo de execucao")
plt.legend()
plt.show()