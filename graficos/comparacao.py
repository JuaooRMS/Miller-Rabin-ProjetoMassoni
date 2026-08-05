import os
import sys
import matplotlib.pyplot as plt

DIRETORIO_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(DIRETORIO_BASE, "testes"))

from comparacao import executar_comparacao

def gerar_grafico():

    # Executa a comparação entre os algoritmos.
    #
    # Cada tamanho de número é testado várias vezes
    # e o tempo médio é utilizado para reduzir
    # variações causadas pelo sistema.
    resultados = executar_comparacao(
        repeticoes=100
    )

    # Quantidade de bits dos números testados.
    bits = [
        resultado.bits
        for resultado in resultados
    ]

    # Tempo médio gasto pelo Miller-Rabin.
    tempos_miller = [
        resultado.tempo_miller
        for resultado in resultados
    ]

    # Tempo médio gasto pelo método ingênuo.
    tempos_ingenuo = [
        resultado.tempo_ingenuo
        for resultado in resultados
    ]

    plt.figure(figsize=(8, 5))

    # Curva do algoritmo probabilístico Miller-Rabin.
    plt.plot(
        bits,
        tempos_miller,
        marker="o",
        label="Miller-Rabin"
    )

    # Curva do método tradicional.
    #
    # Esse método testa possíveis divisores até √n,
    # portanto seu crescimento é muito maior.
    plt.plot(
        bits,
        tempos_ingenuo,
        marker="s",
        label="Teste Ingênuo"
    )

    plt.title(
        "Comparação de desempenho: Miller-Rabin x Teste Ingênuo"
    )

    plt.xlabel(
        "Tamanho do número (bits)"
    )

    plt.ylabel(
        "Tempo médio (segundos)"
    )



    # O teste ingênuo cresce rapidamente,
    # então a escala logarítmica facilita
    # visualizar a diferença entre os algoritmos.
    plt.yscale("log")



    plt.grid(True)

    plt.legend()

    plt.show()




def main():

    gerar_grafico()


if __name__ == "__main__":

    main()