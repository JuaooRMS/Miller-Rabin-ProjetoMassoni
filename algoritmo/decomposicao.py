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