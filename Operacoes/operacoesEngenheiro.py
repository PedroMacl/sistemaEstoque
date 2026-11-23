from datetime import datetime

class Operacoes:

    def __init__(self):
        self.lista = []
        self.historico = []

    def registrarMovimentacao(self, tipo, nome, codigo, quantidade, saldo):

        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        movimentacao = (data, tipo, nome, codigo, quantidade, saldo)

        self.historico.append(movimentacao)


    def cadastrarEquipamento(self):

        nome = input("Nome do equipamento: ")
        codigo = input("Código do equipamento: ")
        quantidade = int(input("Quantidade: "))

        if quantidade <= 0:
            print("Informe uma quantidade válida!")
            return

        for i, equipamento in enumerate(self.lista):

            if equipamento[1] == codigo:

                nomeAntigo, codigoAntigo, quantidadeAntiga = equipamento

                if nomeAntigo.lower() != nome.lower():
                    print("Esse código já pertence a outro equipamento!")
                    return

                novaQuantidade = quantidadeAntiga + quantidade

                self.lista[i] = (nomeAntigo, codigoAntigo, novaQuantidade)

                self.registrarMovimentacao(
                    "ENTRADA", nomeAntigo, codigoAntigo,
                    quantidade, novaQuantidade
                )

                print("Quantidade atualizada com sucesso!")
                return

        self.lista.append((nome, codigo, quantidade))

        self.registrarMovimentacao(
            "ENTRADA", nome, codigo, quantidade, quantidade
        )

        print("Equipamento cadastrado com sucesso!")


    def listarEquipamentos(self):

        if not self.lista:
            print("Nenhum equipamento encontrado no estoque!")
            return

        for nome, codigo, quantidade in self.lista:

            print(f"\nEquipamento: {nome}")
            print(f"Código: {codigo}")
            print(f"Quantidade em estoque: {quantidade}")
            print("-" * 35)


    def removerEquipamento(self):

        codigo = input("Informe o código do equipamento: ")

        for i, equipamento in enumerate(self.lista):

            if equipamento[1] == codigo:

                nome, codigo, quantidade = equipamento

                quantidadeRemover = int(input("Quantidade que deseja remover: "))

                if quantidadeRemover <= 0:
                    print("Informe uma quantidade válida!")
                    return

                if quantidadeRemover > quantidade:
                    print("Quantidade insuficiente no estoque!")
                    return

                novaQuantidade = quantidade - quantidadeRemover

                self.registrarMovimentacao(
                    "SAÍDA", nome, codigo,
                    quantidadeRemover, novaQuantidade
                )

                if novaQuantidade == 0:
                    self.lista.pop(i)
                    print("Equipamento removido completamente do estoque!")

                else:
                    self.lista[i] = (nome, codigo, novaQuantidade)
                    print("Estoque atualizado com sucesso!")

                return

        print("Equipamento não encontrado!")


    def listarHistorico(self):

        if not self.historico:
            print("Nenhuma movimentação registrada!")
            return

        print("\n========== HISTÓRICO DE MOVIMENTAÇÕES ==========")

        for data, tipo, nome, codigo, quantidade, saldo in self.historico:

            print(f"\nData: {data}")
            print(f"Movimentação: {tipo}")
            print(f"Equipamento: {nome}")
            print(f"Código: {codigo}")
            print(f"Quantidade movimentada: {quantidade}")
            print(f"Saldo após movimentação: {saldo}")

            print("-" * 45)