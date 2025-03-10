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


# Exemplo de uso
conta = ContaBancaria("Helder", 2000)
conta1 = ContaBancaria("Carla", 3000)
conta2 = ContaBancaria("Gabriel", 1000)
conta3 = ContaBancaria("Camila", 1000)
conta.depositar(500)
conta.sacar(200)
conta.sacar(500)
conta.sacar(300)
conta.exibir_extrato()
conta1.depositar(500)
conta1.sacar(200)
conta1.sacar(500)
conta1.sacar(300)
conta1.exibir_extrato()
conta3.depositar(500)
conta3.sacar(200)
conta3.sacar(500)
conta3.sacar(300)
conta3.exibir_extrato()
conta2.depositar(500)
conta2.sacar(200)
conta2.sacar(500)
conta2.sacar(300)
conta2.exibir_extrato()
