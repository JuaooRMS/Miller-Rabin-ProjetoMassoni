import os
import random
import sys
from dataclasses import dataclass

DIRETORIO_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(DIRETORIO_BASE, "algoritmo"))

from miller_rabin import miller_rabin


NUMEROS_DE_CARMICHAEL = (
    561, 1105, 1729, 2465, 2821,
    6601, 8911, 10585, 15841, 29341
)

RODADAS_MILLER_RABIN = (1, 2, 3, 5, 10, 40)


@dataclass
class ResultadoCarmichael:
    rodadas: int
    falsos_positivos: int
    total_testes: int
    taxa_erro: float


def executar_teste_carmichael(repeticoes_por_rodada: int = 1000):
    print("Teste com números de Carmichael\n")

    print(
        f"{'Rodadas':<12}"
        f"{'Falsos Positivos':<20}"
        f"{'Total de Testes':<18}"
        f"{'Taxa de Erro'}"
    )

    resultados = []

    teste_miller_rabin = miller_rabin

    for quantidade_rodadas in RODADAS_MILLER_RABIN:

        falsos_positivos = 0
        total_testes = 0

        for numero in NUMEROS_DE_CARMICHAEL:

            for _ in range(repeticoes_por_rodada):

                total_testes += 1

                if teste_miller_rabin(numero, quantidade_rodadas):
                    falsos_positivos += 1

        taxa_erro = (falsos_positivos / total_testes) * 100

        resultados.append(
            ResultadoCarmichael(
                rodadas=quantidade_rodadas,
                falsos_positivos=falsos_positivos,
                total_testes=total_testes,
                taxa_erro=taxa_erro
            )
        )

        print(
            f"{quantidade_rodadas:<12}"
            f"{falsos_positivos:<20}"
            f"{total_testes:<18}"
            f"{taxa_erro:.5f}%"
        )

    return resultados


def main():
    executar_teste_carmichael(
        repeticoes_por_rodada=1000
    )


if __name__ == "__main__":
    main()