import sys
import os
import matplotlib.pyplot as plt
import time
import random
from dataclasses import dataclass

DIRETORIO_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(DIRETORIO_BASE, "algoritmo"))

from miller_rabin import miller_rabin

TAMANHOS_BITS = [
    8,
    16,
    32,
    64,
    128,
    256,
    512,
    1024,
    2048
    ]

# Análise de como o tempo de execução escala de acordo com os tamanhos das entradas em bits que
# comprova a complexidade do algoritmo como O(log(n)).

@dataclass
class ResultadoDesempenho:
    # Usaremos a represetação dos números em bits, pois estas representações se mantém de acordo
    # com o real tamanho das entradas no computador.
    #
    # Pelo caráter probabilístico do teste de Miller-Rabin, realizaremos sucessivos testes com números de N
    # bits e tiraremos a média dos tempos de execução de cada uma das rodadas.  

    bits: int
    tempo_medio: int

def gerar_numero(bits):

    # Gera um número aleatório com a quantidade
    # de bits desejada.
    numero = random.getrandbits(bits)


    # O Miller-Rabin trabalha melhor com números ímpares,
    # pois números pares maiores que 2 já são compostos.
    numero |= 1


    # Garante que o número realmente possua
    # a quantidade de bits escolhida.
    #
    # Sem isso, o gerador poderia retornar
    # números menores que o tamanho esperado.
    numero |= (1 << (bits - 1))


    return numero


def teste_desempenho(repeticoes):
    # Executa os testes com N repetições para cada tamanho de número em bits
    # previsto na constante TAMANHOS_BITS. 

    resultado = []


    for bits in TAMANHOS_BITS:

        # Acumula a soma de todos os tempos para um dado tamanho em bits.
        soma_tempos = 0

        # A critério de teste, usaremos um k qualquer igual a 10, já que estamos apenas interessados
        # no tempo de execução do algoritmo, não com a sua confiabilidade.

        for _ in range(repeticoes):

            numero = gerar_numero(bits)
            inicio = time.perf_counter()
            miller_rabin(numero, 10)
            soma_tempos += (time.perf_counter() - inicio)

        # Guarda os dados em forma de um data class.
        resultado.append(ResultadoDesempenho(bits, soma_tempos/repeticoes))

    return resultado


def plotar_grafico(resultados):

    # Recupera os dados para plotagem do gráfico, sendo bits os valores
    # do eixo x, e tempos os valores para o eixo y.

    bits = [resultado.bits for resultado in resultados]
    tempos = [resultado.tempo_medio for resultado in resultados]

    plt.plot(bits, tempos, label="Curva de complexidade O(log(n))")
    plt.title("Análise de desempenho do algoritmo de Miller-Rabin")
    plt.xlabel("Tamanho da entrada (bits)")
    plt.ylabel("Tempo de execução (em segundos)")

    # Define a escala do gráfico como log, para facilitar
    # a visualização da complexidade do algoritmo.

    plt.yscale("log")

    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    resultados = teste_desempenho(1000)
    plotar_grafico(resultados)

if __name__ == "__main__":
    main()