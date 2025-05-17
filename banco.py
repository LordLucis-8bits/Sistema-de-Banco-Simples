class Banco:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} adicionado com sucesso!")

    def buscar_cliente(self, nome):
        for cliente in self.clientes:
            if cliente.nome == nome:
                return cliente
        print(f"Cliente {nome} nao encontrado!")
        return None
    
    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado!")
            return
        
        print("Lista de Clientes:")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}, Saldo: R${cliente.saldo:.2f}")
            
