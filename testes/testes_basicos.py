import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'algoritmo'))

from miller_rabin import miller_rabin

# Quantidade de rodadas de teste.
# Com 20 rodadas, a chance de erro é menor que 1/4^20.
RODADAS = 20

def teste_primos_conhecidos():
    primos_conhecidos = [101, 103, 997, 7919, 104729, 1299709, 15485863, 32452843, 49979687, 67867967, 86028121, 982451653]
    total_testes = 0
    total_erros = 0

    print(f"|{"-"*57}|")
    print (f"|-{"Testando Primos Conhecidos":^55}-|")
    print(f"|{"-"*57}|")
    for primo in primos_conhecidos:
        total_testes += 1
        if miller_rabin(primo, RODADAS):
            print(f"| {f'{primo} é um número primo.':<56}|")
        else:
            print(f"| {f'{primo} é primo, mas foi classificado como composto.':<56}|")
            total_erros += 1
    
    print(f"|{"-"*57}|")
    print(f"| {f'Total de falhas: {total_erros:>2} de {total_testes:>2} testes realizados.':<56}|")



# Compostos formados pelo produto de dois primos médios,
# para forçar o algoritmo a passar pela decomposição.
def teste_compostos_de_fatores_primos():
    compostos = [101 * 103, 104729 * 1299709, 32452843 * 49979687, 67867967 * 982451653]
    total_testes = 0
    total_erros = 0

    print(f"|{"-"*57}|")
    print (f"|-{"Testando Compostos de Fatores Primos":^55}-|")
    print(f"|{"-"*57}|")
    for composto in compostos:
        total_testes += 1
        if miller_rabin(composto, RODADAS):
            print(f"| {f'{composto} é um número composto,mas foi classificado como primo.':<56}|")
        else:
            print(f"| {f'{composto} é composto.':<56}|")
            total_erros += 1
    
    print(f"|{"-"*57}|")
    print(f"| {f'Total de falhas: {total_erros:>2} de {total_testes:>2} testes realizados.':<56}|")


# Números de Carmichael.
#
# São compostos que satisfazem o Pequeno Teorema de Fermat
# para toda base coprima com eles, ou seja, enganariam um
# teste de primalidade baseado só em Fermat. O Miller-Rabin
# foi criado justamente para não cair nessa armadilha.
def teste_numeros_de_carmichael():
    numeros_carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911, 41041, 62745, 63973]
    total_testes = 0
    total_erros = 0

    print(f"|{"-"*57}|")
    print (f"|-{"Testando Números de Carmichael":^55}-|")
    print(f"|{"-"*57}|")
    for carmichael in numeros_carmichael:
        total_testes += 1
        if miller_rabin(carmichael, RODADAS):
            print(f"| {f'{carmichael} é um número composto de Carmichael, mas foi classificado como primo.':<56}|")
            total_erros += 1
        else:
            print(f"| {f'{carmichael} é composto.':<56}|")
    
    print(f"|{"-"*57}|")
    print(f"| {f'Total de falhas: {total_erros:>2} de {total_testes:>2} testes realizados.':<56}|")


def teste_primos_de_mersenne():
    primos_mersenne = {
        "2 ** 61 - 1": 2305843009213693951,
        "2 ** 127 - 1": 170141183460469231731687303715884105727,
        "2 ** 89 - 1": 618970019642690137449562111,
        "2 ** 107 - 1": 162259276829213363391578010288127}
    total_testes = 0
    total_erros = 0

    print(f"|{"-"*57}|")
    print (f"|-{"Testando Primos de Mersenne":^55}-|")
    print(f"|{"-"*57}|")
    for primo,valor in primos_mersenne.items():
        total_testes += 1
        
        print (f"| {f'{primo} = {valor}':<56}|")
        if miller_rabin(valor, RODADAS):
            print(f"| {f'{primo} é um número primo.':<56}|")
        else:
            print(f"| {f'{primo} é primo, mas foi classificado como composto.':<56}|")
            total_erros += 1
    
    print(f"|{"-"*57}|")
    print(f"| {f'Total de falhas: {total_erros:>2} de {total_testes:>2} testes realizados.':<56}|")


def main():
    print(f"|{"-"*57}|")
    print (f"|-{"Testes básico do algoritmo Miller-Rabin":^55}-|")
    teste_primos_conhecidos()
    teste_compostos_de_fatores_primos()
    teste_numeros_de_carmichael()
    teste_primos_de_mersenne()
    print(f"|{"-"*57}|")
main()