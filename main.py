from algoritmo.main_miller_rabin import testar_miller_rabin

from graficos.desempenho import grafico_desempenho
from graficos.erro import grafico_taxa_de_erro
from graficos.comparacao import gerar_grafico

from testes.testes_basicos import main as testes_basicos
from testes.testes_carmichael import main as testes_carmichael
from testes.testes_de_estresse import main as testes_estresse
from testes.comparacao import main as teste_comparacao


def menu():

    while True:

        print("\n===== Miller-Rabin =====")
        print("1 - Testar número com Miller-Rabin")
        print("2 - Gráfico de desempenho (bits x tempo)")
        print("3 - Gráfico da taxa de erro (Carmichael)")
        print("4 - Comparação Miller-Rabin x Ingênuo")
        print("5 - Executar todos os gráficos")
        print("6 - Executar todos os testes")
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

        elif opcao == "6":

            print("\n" + "=" * 70)
            print("TESTES BÁSICOS".center(70))
            print("=" * 70)
            testes_basicos()

            print("\n" + "=" * 70)
            print("TESTES DE CARMICHAEL".center(70))
            print("=" * 70)
            testes_carmichael()

            print("\n" + "=" * 70)
            print("TESTES DE ESTRESSE".center(70))
            print("=" * 70)
            testes_estresse()

            print("\n" + "=" * 70)
            print("TODOS OS TESTES FORAM EXECUTADOS!".center(70))
            print("=" * 70)

        elif opcao == "0":

            break


        else:

            print("Opção inválida!")

if __name__ == "__main__":
    menu()