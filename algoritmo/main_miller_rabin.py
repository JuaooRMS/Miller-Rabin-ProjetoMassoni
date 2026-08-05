from algoritmo.miller_rabin import miller_rabin

def testar_miller_rabin():

    numero = int(input("Número: "))
    rodadas = int(input("Rodadas: "))

    if miller_rabin(numero, rodadas):
        print(f"{numero} é provavelmente primo.")
    else:
        print(f"{numero} é composto.")


if __name__ == "__main__":
    testar_miller_rabin()

# OBSERVAÇÃO
#
# Nesta implementação foram utilizadas testemunhas (bases) aleatórias, que é a
# versão probabilística do algoritmo de Miller-Rabin. A cada rodada uma nova
# base é escolhida aleatoriamente no intervalo [2, n - 2], fazendo com que a
# probabilidade de um número composto ser classificado como primo seja, no
# máximo:
#
#                           (1/4)^k
#
# onde k é a quantidade de rodadas realizadas.
#
# Entretanto, para números menores que 2^64 (inteiros de 64 bits), existe uma
# otimização bastante conhecida: em vez de utilizar bases aleatórias, pode-se
# utilizar um conjunto fixo de testemunhas:
#
#     [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
#
# Como aplicações criptográficas (como o RSA) normalmente trabalham com números
# de 1024, 2048, 3072 ou 4096 bits, essas sete bases deixam de ser suficientes.
# Nesses casos, é utilizada a versão probabilística do Miller-Rabin com
# testemunhas aleatórias, que continua sendo extremamente confiável quando
# executada com várias rodadas. Mas achei interessante deixar essa informação registrada.
#
# Encontrei essas informações nessa fonte abaixo e no seguinte tópico "Deterministic version" ele menciona as 7 bases.
#
# CP-Algorithms – Primality Tests:
# https://cp-algorithms.com/algebra/primality_tests.html
