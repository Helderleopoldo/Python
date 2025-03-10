
menu = """
        ******* Bem vindo ao Leopoldus Bank ******* 

        Digite um número para uma das opções abaixo:

        1 - Depósito
        2 - Saque
        3 - Extrato
        4 - Sair
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
        for movimento in self.extrato:
            print(movimento)
        print(f"Saldo atual: R${self.saldo:.2f}\n")


conta = ContaBancaria("Helder", 2000)

while True:
    opcao = input(menu).strip()  

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        conta.depositar(valor)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        conta.sacar(valor)

    elif opcao == "3":
        conta.exibir_extrato()

    elif opcao == "4":
        print("Obrigado por usar o Leopoldus Bank. Até logo!")
        break

    else:
        print("Opção inválida, tente novamente.")


# Exemplo de uso
#conta = ContaBancaria("Helder", 2000)
#conta1 = ContaBancaria("Carla", 3000)
#conta2 = ContaBancaria("Gabriel", 1000)
#conta3 = ContaBancaria("Camila", 1000)



