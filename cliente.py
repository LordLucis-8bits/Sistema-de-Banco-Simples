class Cliente:
    def __init__(self, nome: str, cpf: str, saldo: float):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R${valor:.2f}realizado com sucesso!")
        else:
            print("Valor de deposito invalido!")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f}realizado com sucesso!")
        else:
            print("Valor de saque invalido ou saldo insuficiente!")       

    def extrato(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Saldo: R${self.saldo:.2f}")


