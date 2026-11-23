from engenheiro import Engenheiro

opcao=0

while opcao!=2:

    opcao=int(input("INFORME UMA AÇÃO:\n" \
    "1-ÁREA DO ENGENHEIRO \n" \
    "2- SAIR "))

    match opcao:

        case 1:
            Engenheiro.loginEngenheiro()
        case 2:
            print("Saindo...")
            break
        case _:
            print("Opção inválida")    



