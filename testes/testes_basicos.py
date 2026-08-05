import os
import sys

DIRETORIO_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(DIRETORIO_BASE, 'algoritmo'))

from algoritmo.miller_rabin import miller_rabin

# Realizando testes básicos do algoritmo Miller-Rabin, com números conhecidos, compostos de fatores primos, números de Carmichael e primos de Mersenne.

# Quantidade de rodadas de teste. 
#
# Com quarenta rodadas, a chance de erro é (1/4)^40, o que torna o teste confiável para números grandes, mesmo acima de 2^64.
RODADAS = 40

# Função que testa o algoritmo Miller-Rabin com números primos pequenos e médios.
def teste_primos_conhecidos():
    primos_conhecidos = [101, 103, 997, 7919, 104729, 1299709, 15485863, 32452843, 49979687, 67867967, 86028121, 982451653]

    total_erros = 0

    print(f"{'-' * 60}")
    print (f"-{"Testando Primos Conhecidos":^58}-")
    print(f"{'-' * 60}")

    # Testando cada primo conhecido.
    for primo in primos_conhecidos:
        if miller_rabin(primo, RODADAS):
            print(f" {f'{primo} é um número primo.':<58}")
        else:
            #Espera-se que essa mensagem nunca seja exibida, pois todos os números testados são primos.
            print(f" {f'{primo} é primo, mas foi classificado como composto.':<58}")
            total_erros += 1
    
    # Imprimindo o total de falhas.
    print(f"{'-' * 60}")
    print(f" {f'Total de falhas: {total_erros:>2} de {len(primos_conhecidos):>2} testes realizados.':<58}")


# Função que testa o algoritmo Miller-Rabin com números compostos não triviais, formados por fatores primos.
def teste_compostos_de_fatores_primos():
    compostos = [101 * 103, 104729 * 1299709, 32452843 * 49979687, 67867967 * 982451653]
    total_erros = 0

    print(f"{'-' * 60}")
    print (f"-{"Testando Compostos de Fatores Primos":^58}-")
    print(f"{'-' * 60}")

    # Testando cada número composto.
    for composto in compostos:
        if miller_rabin(composto, RODADAS):

            # Espera-se que essa mensagem seja exibida, pois todos os números testados são compostos.
            print(f" {f'{composto} é um número composto,mas foi classificado como primo.':<56}")
            total_erros += 1
        else:
            print(f" {f'{composto} é composto.':<56}")
    
    print(f"{'-' * 60}")
    print(f" {f'Total de falhas: {total_erros:>2} de {len(compostos):>2} testes realizados.':<56}")


# Números de Carmichael.
#
# São números ímapres compostos que passam no teste de primalidade 
# de Fermat para todas as bases que são coprimas com o número e 
# também em outros testes mais simples.
#
# O teste de Miller-Rabin, com sua robustez, evita a falsa positiva 
# desses pseudoprimos.Ainda assim, alguns números de Carmichael podem
# passar no teste de Miller-Rabin, dependendo da quantidade de rodadas
# e das bases escolhidas.
#
# Referências: https://files.cercomp.ufg.br/weby/up/1170/o/APChavesRO14.pdf
# https://en.wikipedia.org/wiki/Carmichael_number
def teste_numeros_de_carmichael():
    numeros_carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911, 162401, 172081, 188461,41041, 62745, 63973]
    total_erros = 0

    print(f"{'-' * 60}")
    print (f"-{"Testando Números de Carmichael":^58}-")
    print(f"{'-' * 60}")

    # Testando cada número da sequência.
    for carmichael in numeros_carmichael:
        if miller_rabin(carmichael, RODADAS):

            # Espera-se que essa mensagem seja exibida, pois todos os números testados são compostos.
            print(f" {f'{carmichael} é um número composto de Carmichael, mas foi classificado como primo.':<58}")
            total_erros += 1
        else:
            print(f" {f'{carmichael} é composto.':<58}")
    
    print(f"{'-' * 60}")
    print(f" {f'Total de falhas: {total_erros:>2} de {len(numeros_carmichael):>2} testes realizados.':<58}")


# Os primos de Mersenne são números da forma 2^p - 1, onde p é primo.
# É válido dizer que nem todo expoente primo gera um primo de Mersenne.
# Por exemplo, 2^11 - 1 = 2047 = 23 * 89, que é composto.
#
#Referência: https://dma.uem.br/kit/jeepema-1/art3_1801.pdf
def teste_primos_de_mersenne():
    primos_mersenne = {
        "2 ** 61 - 1": 2305843009213693951,
        "2 ** 127 - 1": 170141183460469231731687303715884105727,
        "2 ** 89 - 1": 618970019642690137449562111,
        "2 ** 107 - 1": 162259276829213363391578010288127}
    total_erros = 0

    print(f"{'-' * 60}")
    print (f"-{"Testando Primos de Mersenne":^58}-")
    print(f"{'-' * 60}")

    # Testando cada número da sequência.
    for primo,valor in primos_mersenne.items():
        print (f" {f'{primo} = {valor}':<58}")
        if miller_rabin(valor, RODADAS):
            print(f" {f'{primo} é um número primo.':<58}")
        else:
            
            #Espera-se que essa mensagem nunca seja exibida, pois todos os números testados são primos.
            print(f" {f'{primo} é primo, mas foi classificado como composto.':<58}")
            total_erros += 1
    
    print(f"{"-"*60}")
    print(f" {f'Total de falhas: {total_erros:>2} de {len(primos_mersenne):>2} testes realizados.':<58}")


def main():
    print("\nTestes Básicos - Miller-Rabin\n")
    teste_primos_conhecidos()
    teste_compostos_de_fatores_primos()
    teste_numeros_de_carmichael()
    teste_primos_de_mersenne()
    print(f"{"-"*60}")


if __name__ == "__main__":
    main()