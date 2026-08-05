import os
import sys
from dataclasses import dataclass

DIRETORIO_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(DIRETORIO_BASE, "algoritmo"))

from miller_rabin import miller_rabin

# Números de Carmichael são números compostos que conseguem
# passar pelo teste de Fermat para algumas bases.
#
# Eles são utilizados para testar algoritmos de primalidade,
# pois representam casos difíceis onde testes mais simples
# podem falhar.
#
# O Miller-Rabin foi criado justamente para evitar esse tipo
# de falso positivo encontrado no teste de Fermat.
NUMEROS_DE_CARMICHAEL = (
    561, 1105, 1729, 2465, 2821,
    6601, 8911, 10585, 15841, 29341,
    41041, 46657, 52633, 62745,
    63973, 75361, 101101, 115921,
    126217, 162401, 172081, 188461,
    252601, 278545, 294409, 314821
)

# Quantidade de rodadas utilizadas no teste.
#
# Cada rodada representa uma nova testemunha (base).
# Quanto maior o número de rodadas, menor a chance
# de um número composto passar como primo.
RODADAS_MILLER_RABIN = (
    1, 2, 3, 5, 10, 20, 40
)


@dataclass
class ResultadoCarmichael:

    # Quantidade de testemunhas utilizadas.
    rodadas: int

    # Quantidade de vezes que um número composto
    # foi classificado incorretamente como primo.
    falsos_positivos: int

    # Quantidade total de testes realizados.
    total_testes: int

    # Taxa de erro encontrada experimentalmente.
    taxa_erro: float

    # Limite máximo de erro esperado pelo Miller-Rabin:
    #
    # (1/4)^k
    #
    # onde k é o número de rodadas.
    limite_teorico: float

    # Quantidade esperada de falsos positivos
    # segundo a probabilidade teórica.
    falsos_esperados: float


def executar_teste_carmichael(repeticoes_por_rodada=1000):


    print("Teste com números de Carmichael\n")


    print(
        f"{'Rodadas':<10}"
        f"{'Falsos':<12}"
        f"{'Total':<12}"
        f"{'Erro (%)':<15}"
        f"{'Limite (%)':<18}"
        f"{'Esperado'}"
    )


    resultados = []

    # Testamos diferentes quantidades de testemunhas.
    for quantidade_rodadas in RODADAS_MILLER_RABIN:

        falsos_positivos = 0
        total_testes = 0

        # Cada número de Carmichael é testado várias vezes.
        #
        # Como as bases do Miller-Rabin são aleatórias,
        # cada execução pode escolher testemunhas diferentes.
        for numero in NUMEROS_DE_CARMICHAEL:


            for _ in range(repeticoes_por_rodada):


                total_testes += 1

                # Se um número de Carmichael passar,
                # significa que ocorreu um falso positivo,
                # pois todos esses números são compostos.
                if miller_rabin(numero, quantidade_rodadas):

                    falsos_positivos += 1

        # Calcula a porcentagem de falsos positivos observada.
        taxa_erro = (falsos_positivos / total_testes) * 100

        # O Miller-Rabin possui limite máximo de erro:
        #
        # (1/4)^k
        #
        # onde k é o número de rodadas.
        limite_teorico = ((1 / 4) ** quantidade_rodadas) * 100

        # Calcula quantos erros seriam esperados
        # seguindo a probabilidade teórica.
        falsos_esperados = total_testes * ((1 / 4) ** quantidade_rodadas)

        resultado = ResultadoCarmichael(

            rodadas=quantidade_rodadas,

            falsos_positivos=falsos_positivos,

            total_testes=total_testes,

            taxa_erro=taxa_erro,

            limite_teorico=limite_teorico,

            falsos_esperados=falsos_esperados
        )

        resultados.append(resultado)

        print(

            f"{resultado.rodadas:<10}"

            f"{resultado.falsos_positivos:<12}"

            f"{resultado.total_testes:<12}"

            f"{resultado.taxa_erro:<15.8f}"

            f"{resultado.limite_teorico:<18.8f}"

            f"{resultado.falsos_esperados:.6f}"

        )

    return resultados

def main():

    executar_teste_carmichael(1000)

if __name__ == "__main__":

    main()