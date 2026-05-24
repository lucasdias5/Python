while True:

    #TÍTULO

    print("\n{:=^20}".format("BANCO"))

    #ENTRADA

    saldo = float(input("\nInforme o saldo em conta: "))

    print("\nSaldo: ",saldo)
    print("\nAperte 1 para sacar")
    print("Aperte 2 para depositar")

    operacao = int(input("\nVoce deseja sacar ou depositar?: "))

    if operacao == 1:
        valor = float(input("Qual valor você deseja sacar?: "))
    elif operacao == 2:
        valor = float(input("Qual valor você deseja depositar: "))
    else:
        print("\nErro: operacao invalida")
        print("\nAperte 1 para repetir")
        print("Aperte 2 para sair")

        loop_erro_valor = int(input("Voce deseja repetir?: "))
        
        if loop_erro_valor == 1:
            continue
        elif loop_erro_valor == 2:
            break

    #se o saldo for insuficiente

    if operacao == 1 and valor > saldo:
        print("\nErro: saldo insuficiente")
        print("\nAperte 1 para repetir")
        print("Aperte 2 para sair")

        loop_erro_valor = int(input("Voce deseja repetir?: "))
        
        if loop_erro_valor == 1:
            continue
        elif loop_erro_valor == 2:
            break
    
    #processamento e saída

    if operacao == 1:
        print("\nVoce sacou: ",valor, "\nSeu saldo em conta agora é: ", saldo - valor)
    elif operacao == 2:
        print("\nVoce depositou: ",valor, "\nSeu saldo em conta agora é: ", saldo + valor)

    #loop

    print("\nAperte 1 para repetir")
    print("Aperte 2 para sair")

    loop = int(input("Voce deseja repetir?: "))

    if loop == 1:
        continue
    elif loop == 2:
        break