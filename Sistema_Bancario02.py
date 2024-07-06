import textwrap

def menu():
    menu = """\n

========== MENU ==========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova Conta
[5] Listar Contas
[6] Novo Usuário
[7] Sair

Informe a operação que deseja realizar: 
"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite_saques, numero_saques, limite):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("Operação fahlou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, / , *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de descimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número, bairro, cidade/ sigla estado): ")


    usuarios.append({"nome" : nome, "data_nascimento": data_nascimento, "cpf" : cpf, "endereco" : endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nConta criada vom sucesso!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta['angencia']}
            C/C: {conta ["numero+conta"]}
            Titular: {conta["Usuário"]["nome"]}
        """
        print("=" * 80)
        print(textwrap.dedent(linha))



def main():
    limite_saques = 3
    agencia = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = limite_saques,

            )


        elif opcao == "3":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta,usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada!")

main()

            