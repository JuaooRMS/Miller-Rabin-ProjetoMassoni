import sys
import os

DIRETORIO_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(DIRETORIO_BASE, "algoritmo"))

from miller_rabin import *
import matplotlib.pyplot as plt
import time
import random

def gerar_numero_aleatorio(n_bits):
    return random.getrandbits(n_bits)


def grafico_desempenho():
    tamanhos = [16, 32, 64, 128, 256, 512, 1024, 2048]
    tempos = []

    for tam in tamanhos:
        soma_tempos = 0

        for _ in range(1000):
            n = gerar_numero_aleatorio(tam)
            inicio = time.perf_counter()
            miller_rabin(n, 10)
            soma_tempos += (time.perf_counter() - inicio)

        tempos.append(soma_tempos/1000)


    plt.plot(tamanhos, tempos, label="Analise Assintótica")
    plt.xlabel("Tamanho")
    plt.ylabel("Tempo")
    plt.show()