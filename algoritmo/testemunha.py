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