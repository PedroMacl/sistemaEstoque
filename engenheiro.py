from Operacoes.operacoesEngenheiro import Operacoes

senha = "1234"

class Engenheiro:

    operacoes = Operacoes()

    @staticmethod
    def menuEngenheiro():

        opcao = 0

        while opcao != 5:

            opcao = int(input(
                "INFORME UMA AÇÃO:\n"
                "1 - Cadastrar novo equipamento\n"
                "2 - Listar equipamentos no estoque\n"
                "3 - Remover equipamento do estoque\n"
                "4 - Consultar Histórico\n" \
                "5-Voltar\n"
            ))

            match opcao:

                case 1:
                    Engenheiro.operacoes.cadastrarEquipamento()

                case 2:
                    Engenheiro.operacoes.listarEquipamentos()

                case 3:
                    Engenheiro.operacoes.removerEquipamento()

                case 4:
                     Engenheiro.operacoes.listarHistorico()   

                case 5:
                    print("Voltando ao menu principal...")

                case _:
                    print("Opção inválida!")

    @staticmethod
    def loginEngenheiro():

        while True:

            senhaInformada = input("Informe sua senha: ")

            if senhaInformada == senha:
                print("SEJA BEM-VINDO A SUA CONTA!\n")
                Engenheiro.menuEngenheiro()
                break

            else:
                print("Senha incorreta!")