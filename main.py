menu = """
-----------  MENU  ------------
    [0] DEPOSITAR
    [1] SACAR
    [2] EXTRATO
    [3] SAIR
-------------------------------
"""

LIMITE_SAQUE = 3
LIMITE_VALOR_SAQUE = 500
saldo = 0
extrato = ""

while True:

    escolha = int(input(menu))
    print()

    if escolha == 0:    #DEPOSITAR
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        saldo += valor_deposito
        extrato += f"Depósito realizado: R$ {valor_deposito:.2f}\n"
        print("Depósito realizado com sucesso!")

    elif escolha == 1:    #SACAR

        if LIMITE_SAQUE != 0:
            valor_saque = float(input("Digite o valor que deseja sacar: "))
            if valor_saque > LIMITE_VALOR_SAQUE:
                print("O saque não foi realizado. O valor máximo do saque é de R$ 500.00")
            elif valor_saque > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= valor_saque
                extrato += f"Saque realizado: R$ {valor_saque:.2f}\n"
                print("Saque realizado com sucesso!")
                LIMITE_SAQUE -= 1
        else:
            print("Não é possísel realizar o saque. Você já usou todos os saques diários.")


    elif escolha == 2:    #EXTRATO
        print("----------- EXTRATO -----------")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("-------------------------------")
    
    elif escolha == 3:    #SAIR
        print("Até a próxima! Estaremos ansiosos para vê-lo novamente em breve!\nSaindo...")
        break

    else:
        print("Opção inválida. Por favor, escolha novamente.")


