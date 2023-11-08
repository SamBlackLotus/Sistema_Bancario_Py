menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""
saldo = 0
limite = 500
extrato = " "
quantidade_saque = 0
LIMITE_SAQUE = 3


while True:

    opcao = input()

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Valor de R$ {valor:.2f} depositado com sucesso!\nRetire seu comprovante. ")
        else:
            print("Operação falhou! O valor informado é inválido.")
               
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = quantidade_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! O saldo é suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor solicitado excede o limite permitido.")

        elif excedeu_saques:
            print("Operação falhou! Quantidade diária de saques excedida.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            quantidade_saque += 1
            print(f"Valor de R$ {valor:.2f} sacado!\nRetire seu dinheiro.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    
    elif opcao == "3":
        print("\n*************** EXTRATO ***************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("****************************************")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")