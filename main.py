from cliente import Cliente
from banco import Banco
banco = Banco()

while True:
    print("\n1 - Cadastrar Cliente")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver saldo")
    print("5 - Listar Clientes")
    print("6 - Sair")
    opcao = input("Escolha uma opcao: ")
    
    if opcao == "1":
        nome = input("Nome: ")
        cpf = input("CPF: ")
        saldo = float(input("Saldo inicial: "))
        novo_cliente = Cliente(nome, cpf, saldo)
        banco.adicionar_cliente(novo_cliente)

    elif opcao == "2":
        nome = input("Nome do cliente: ")
        cliente = banco.buscar_cliente(nome)
        if cliente:
            valor = float(input("Valor a depositar: "))
            cliente.depositar(valor)
        else:
            print("Cliente nao encontrado!")

    elif opcao == "3":
        nome = input("Nome do cliente: ")
        cliente = banco.buscar_cliente(nome)
        if cliente:
            valor = float(input("Valor a sacar: "))
            cliente.sacar(valor)
        else:
            print("Cliente nao encontrado!")

    elif opcao == "4":
        nome = input("Nome do cliente: ")
        cliente = banco.buscar_cliente(nome)
        if cliente:
            cliente.extrato()
        else:
            print("Cliente nao encontrado!")

    elif opcao == "5":
        banco.listar_clientes()    

    elif opcao == "6":
        print("Saindo do sistema...")
        break

    else:
        print("Opcao invalida! Tente novamente.!")

