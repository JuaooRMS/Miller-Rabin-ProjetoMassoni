from algoritmo.main_miller_rabin import testar_miller_rabin

from graficos.desempenho import grafico_desempenho
from graficos.erro import grafico_taxa_de_erro
from graficos.comparacao import gerar_grafico



def menu():

    while True:

        print("\n===== Miller-Rabin =====")
        print("1 - Testar número com Miller-Rabin")
        print("2 - Gráfico de desempenho (bits x tempo)")
        print("3 - Gráfico da taxa de erro (Carmichael)")
        print("4 - Comparação Miller-Rabin x Ingênuo")
        print("5 - Executar todos os gráficos")
        print("0 - Sair")


        opcao = input("\nEscolha: ")


        if opcao == "1":

            testar_miller_rabin()


        elif opcao == "2":

            grafico_desempenho()


        elif opcao == "3":

            grafico_taxa_de_erro()


        elif opcao == "4":

            gerar_grafico()


        elif opcao == "5":

            grafico_desempenho()

            grafico_taxa_de_erro()

            gerar_grafico()


        elif opcao == "0":

            break


        else:

            print("Opção inválida!")



if __name__ == "__main__":
    menu()