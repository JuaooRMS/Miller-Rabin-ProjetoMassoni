from testes.testes_carmichael import executar_teste_carmichael
import matplotlib.pyplot as plt


def grafico_taxa_de_erro():


    # Executa o experimento com números compostos difíceis.
    #
    # O objetivo é observar quantas vezes o Miller-Rabin
    # classifica incorretamente um composto como primo.
    resultados = executar_teste_carmichael(
        repeticoes_por_rodada=1000
    )



    # Número de testemunhas utilizadas.
    rodadas = [
        resultado.rodadas
        for resultado in resultados
    ]



    # Taxa encontrada experimentalmente.
    #
    # Como podemos obter zero falsos positivos,
    # colocamos um valor mínimo para conseguir
    # representar no gráfico logarítmico.
    taxas_experimentais = [
        max(resultado.taxa_erro, 1e-10)
        for resultado in resultados
    ]



    # Limite superior de erro do Miller-Rabin.
    #
    # A probabilidade de um número composto passar
    # por k rodadas é limitada por:
    #
    # (1/4)^k
    #
    # Esse valor representa o pior caso,
    # não uma taxa esperada.
    taxas_teoricas = [
        (1 / 4) ** rodada * 100
        for rodada in rodadas
    ]



    plt.figure(figsize=(8, 5))



    plt.plot(
        rodadas,
        taxas_experimentais,
        marker="o",
        label="Taxa experimental"
    )



    plt.plot(
        rodadas,
        taxas_teoricas,
        marker="s",
        linestyle="--",
        label="Limite superior teórico $(1/4)^k$"
    )



    plt.title(
        "Taxa de erro do Miller-Rabin"
    )


    plt.xlabel(
        "Quantidade de rodadas (k)"
    )


    plt.ylabel(
        "Probabilidade de erro (%)"
    )



    # A probabilidade diminui exponencialmente,
    # então a escala logarítmica permite visualizar
    # melhor a redução do erro.
    plt.yscale("log")



    plt.grid(True)

    plt.legend()

    plt.show()