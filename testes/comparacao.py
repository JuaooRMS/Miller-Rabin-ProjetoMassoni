import os
import sys
import math
import random
import time
from dataclasses import dataclass

DIRETORIO_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(DIRETORIO_BASE, "algoritmo"))

from algoritmo.miller_rabin import miller_rabin



# Quantidades de bits que serão utilizadas nos testes.
#
# A ideia é verificar como o tempo de execução aumenta
# conforme o tamanho do número cresce.
TAMANHOS_BITS = [
    16,
    20,
    24,
    28,
    32
]


@dataclass
class ResultadoComparacao:

    # Guarda o tamanho do número em bits,
    # o tempo gasto pelo Miller-Rabin
    # e o tempo gasto pelo método ingênuo.
    bits: int
    tempo_miller: float
    tempo_ingenuo: float




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




def teste_ingenuo(numero):

    # Esse é o método tradicional(ingenua) de verificar
    # se um número é primo.
    #
    # A ideia é tentar encontrar algum divisor
    # que prove que o número é composto.
    #
    # Como todo número composto possui pelo menos
    # um divisor menor ou igual a sua raiz quadrada,
    # precisamos testar apenas até √n.
    

    if numero < 2:
        return False


    if numero == 2:
        return True


    # Todo número par diferente de 2 é composto.
    if numero % 2 == 0:
        return False



    limite = math.isqrt(numero)


    # Testamos todos os possíveis divisores ímpares.
    #
    # Se algum divisor for encontrado,
    # então temos certeza que o número é composto.
    for divisor in range(3, limite + 1, 2):

        if numero % divisor == 0:
            return False



    # Se nenhum divisor foi encontrado,
    # então o número é primo.
    return True




def executar_comparacao(repeticoes=100):


    resultados = []


    # Executamos o experimento para diferentes
    # tamanhos de números.
    for bits in TAMANHOS_BITS:


        tempo_miller = 0
        tempo_ingenuo = 0



        # Repetimos várias vezes para diminuir
        # a influência de variações do sistema.
        for _ in range(repeticoes):


            numero = gerar_numero(bits)



            # Medimos o tempo do Miller-Rabin.
            inicio = time.perf_counter()

            miller_rabin(numero, 10)

            fim = time.perf_counter()

            tempo_miller += fim - inicio




            # Medimos o tempo do método ingênuo.
            inicio = time.perf_counter()

            teste_ingenuo(numero)

            fim = time.perf_counter()

            tempo_ingenuo += fim - inicio



        # Calculamos a média dos tempos.
        #
        # Essa média representa uma aproximação
        # mais confiável do custo de cada algoritmo.
        resultados.append(
            ResultadoComparacao(
                bits,
                tempo_miller / repeticoes,
                tempo_ingenuo / repeticoes
            )
        )


    return resultados




def main():

    resultados = executar_comparacao()


    print("\nComparação Miller-Rabin x Ingênuo\n")


    print(
        f"{'Bits':<10}"
        f"{'Miller-Rabin':<20}"
        f"{'Ingênuo'}"
    )



    for resultado in resultados:

        print(
            f"{resultado.bits:<10}"
            f"{resultado.tempo_miller:<20.8f}"
            f"{resultado.tempo_ingenuo:.8f}"
        )



if __name__ == "__main__":
    main()