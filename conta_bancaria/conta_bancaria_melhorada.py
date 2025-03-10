menu = """
        ******* Bem-vindo ao Leopoldus Bank ******* 

        Escolha uma opção:

        1 - Criar nova conta
        2 - Acessar conta
        3 - Sair
"""

menu_conta = """
        *** Conta Bancária ***

        1 - Depósito
        2 - Saque
        3 - Extrato
        4 - Trocar de conta
        5 - Sair
"""

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []
        self.saques_realizados = 0
        self.limite_saques_diario = 3
        self.limite_valor_saque = 500

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saques_diario:
            print("Limite de saques diários atingido.")
            return

        if valor > self.limite_valor_saque:
            print(f"Valor máximo por saque é R${self.limite_valor_saque:.2f}.")
            return

        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R${valor:.2f}")
            self.saques_realizados += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def exibir_extrato(self):
        print("\nExtrato da conta:")
        if not self.extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"Saldo atual: R${self.saldo:.2f}\n")


# Dicionário para armazenar múltiplas contas
contas = {}

while True:
    opcao = input(menu).strip()

    if opcao == "1":
        nome = input("Digite o nome do titular da conta: ").strip()
        if nome in contas:
            print("Já existe uma conta com esse nome. Tente outro.")
        else:
            saldo_inicial = float(input("Digite o saldo inicial: "))
            contas[nome] = ContaBancaria(nome, saldo_inicial)
            print(f"Conta criada para {nome} com saldo inicial de R${saldo_inicial:.2f}!")

    elif opcao == "2":
        nome = input("Digite o nome do titular da conta: ").strip()
        if nome not in contas:
            print("Conta não encontrada. Crie uma nova conta primeiro.")
        else:
            conta = contas[nome]
            print(f"Acessando conta de {conta.titular}...\n")

            while True:
                opcao_conta = input(menu_conta).strip()

                if opcao_conta == "1":
                    valor = float(input("Informe o valor do depósito: "))
                    conta.depositar(valor)

                elif opcao_conta == "2":
                    valor = float(input("Informe o valor do saque: "))
                    conta.sacar(valor)

                elif opcao_conta == "3":
                    conta.exibir_extrato()

                elif opcao_conta == "4":
                    print("Trocando de conta...")
                    break

                elif opcao_conta == "5":
                    print("Obrigado por usar o Leopoldus Bank. Até logo!")
                    exit()

                else:
                    print("Opção inválida, tente novamente.")

    elif opcao == "3":
        print("Obrigado por usar o Leopoldus Bank. Até logo!")
        break

    else:
        print("Opção inválida, tente novamente.")
