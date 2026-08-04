import random


def decomposicao(n):
    # O Miller-Rabin precisa escrever:
    #
    # n - 1 = 2^s * d
    #
    # onde d obrigatoriamente precisa ser um número ímpar.

    s = 0  # Quantidade de vezes que conseguimos dividir por 2.
    d = n - 1  # Valor que será dividido até se tornar ímpar.

    # Enquanto d for par, continuamos dividindo por 2.
    # No final teremos:
    #
    # n - 1 = 2^s * d
    while d % 2 == 0:
        d //= 2
        s += 1

    return s, d


def testemunha(base_aleatoria, numero_testado, expoente_da_decomposicao, parte_impar_da_decomposicao):

    # Calculamos:
    #
    # x = a^d mod n
    #
    # Se n realmente for primo, uma das propriedades
    # abaixo deve acontecer:
    #
    # a^d ≡ 1 (mod n)
    #
    # ou
    #
    # a^(2^r * d) ≡ -1 (mod n)
    x = pow(base_aleatoria, parte_impar_da_decomposicao, numero_testado)

    # Se cair logo em 1 ou em -1 (mod n),
    # então essa base não conseguiu provar
    # que o número é composto.
    if x == 1 or x == numero_testado - 1:
        return True

    # Caso contrário, vamos elevando ao quadrado,
    # pois queremos verificar:
    #
    # a^(2d)
    # a^(4d)
    # a^(8d)
    # ...
    #
    # até chegar em a^(2^(s-1) * d)
    for _ in range(expoente_da_decomposicao - 1):

        x = (x * x) % numero_testado

        # Encontramos -1 (mod n).
        # Essa base continua sem conseguir provar
        # que o número é composto.
        if x == numero_testado - 1:
            return True

        # Se chegar em 1 antes de encontrar -1,
        # encontramos uma situação que só acontece
        # quando o número é composto.
        if x == 1:
            return False

    # Se chegou até aqui,
    # nenhuma das propriedades de um primo aconteceu.
    # Então essa base conseguiu provar
    # que o número é composto.
    return False


def miller_rabin(numero, quantidade_de_rodadas):

    # Casos básicos.

    # 2 e 3 são primos.
    if numero in (2, 3):
        return True

    # Todo número menor que 2 ou par
    # (tirando o próprio 2) é composto.
    if numero < 2 or numero % 2 == 0:
        return False

    # Fazemos a decomposição:
    #
    # n - 1 = 2^s * d
    expoente_da_decomposicao, parte_impar_da_decomposicao = decomposicao(numero)

    # Vamos repetir o teste várias vezes.
    # A cada rodada escolhemos uma base diferente.
    for _ in range(quantidade_de_rodadas):

        # Escolhemos uma testemunha aleatória.
        #
        # Quanto mais rodadas fizermos,
        # menor fica a chance de um número composto
        # passar pelo teste.
        base_aleatoria = random.randrange(2, numero - 1)

        # Basta uma única testemunha provar
        # que o número é composto para encerrarmos
        # o algoritmo.
        if not testemunha(
            base_aleatoria,
            numero,
            expoente_da_decomposicao,
            parte_impar_da_decomposicao
        ):
            return False

    # Se nenhuma testemunha conseguiu provar
    # que o número é composto,
    # então ele é considerado provavelmente primo.
    #
    # A probabilidade máxima de erro é:
    #
    # (1/4)^k
    #
    # onde k é a quantidade de rodadas.
    return True


def main():

    numero = int(input("Número: "))
    rodadas = int(input("Rodadas: "))

    if miller_rabin(numero, rodadas):
        print(f"{numero} é provavelmente primo.")
    else:
        print(f"{numero} é composto.")


main()
