from datetime import datetime
LIMITE_SAQUES = int(3)

data_hora = datetime.now();

format_data_hora = data_hora.strftime("%Y-%m-%d %H:%M:%S")

dia = data_hora.day
hora = data_hora.time

saldo = float(0)
limite = float(500)
extrato = str("")
numero_saques = int(0)

menu = """
    MENU

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [9] Sair

: """

while(True):

    opcao = input(menu)

    if opcao == "1":

        print("\n===================== DEPOSITO =================\n")
        deposito = float(input("\n Digite o valor do deposito: "))
            
        if(deposito < 0):
            print("Digite um valor valido!")
            continue;

        saldo += deposito
        print("\nDeposito realizado com sucesso!")
        print(f"\nSaldo: R${saldo:10.2f}")
        extrato += f"\n Data: {format_data_hora} - Deposito: R${deposito:10.2f}"
            
    elif opcao == "2":
        print("\n===================== SAQUE =================\n")
        if(LIMITE_SAQUES - numero_saques <= 0):
            print("Limite de saques atigindo, volte amanha!")
            continue

        print("Saques restantes de hoje: %d" % (LIMITE_SAQUES - numero_saques))
            
        saque = float(input("Digite o valor do saque: "))
        if(saque > saldo):
            print("Saldo insuficiente para o saque!")
            continue
        elif(saque > 500.00):
            print("Limite atingido, maximo de R$ 500.00 por saque!")
            continue

        saldo -= saque
        numero_saques += 1;
        print("\nSaque realizado com sucesso!")
        print(f"\nSaldo: R${saldo:10.2f}")
        extrato += f"\n Data: {format_data_hora} - Saque: - R${saque:10.2f}"
            
    elif opcao == "3":
        print("\n===================== EXTRATO =================\n")
        if(extrato == ""):
            print("Não foram realizadas movimentações")

        print(extrato + 
              "\n------------------------------------------------\n" + 
              f"\n Saldo: {saldo:10.2f}");
    
    elif opcao =="9":
        print("Sair")
        break

    else:
        print("Operacao invalida, digite novamente a operacao desejada!")
