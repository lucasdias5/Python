while True:
    import math

    #titulo

    print("\n{:=^20}".format("CALCULADORA"))
    
    #entrada

    primeiro_valor = float(input("\ninforme o primeiro valor: "))
    operacao = input("escolha a operação: ")
    
    #caso a operacao seja raiz quadrada

    if operacao == "raiz quadrada":
        print("resultado:", math.sqrt(primeiro_valor))
        loop_raiz = str(input("Deseja continuar?: "))
        if loop_raiz == "sim":
            continue
        elif loop_raiz == "nao":
            break    

    segundo_valor = float(input("informe o segundo valor: "))

    #variaveis das operacoes

    soma = primeiro_valor + segundo_valor
    subtracao = primeiro_valor - segundo_valor
    multiplicacao = primeiro_valor * segundo_valor
    divisao = primeiro_valor / segundo_valor
    potencia = primeiro_valor ** segundo_valor
    porcentagem = (primeiro_valor * segundo_valor) / 100
    soma_porcentagem = primeiro_valor + ((primeiro_valor * segundo_valor) / 100)
    subtracao_porcentagem = primeiro_valor - ((primeiro_valor * segundo_valor) / 100)

    #processamento e saida

    match operacao:
        case "+":
            print("O resultado é: ", soma)
        case "-":
            print("O resultado é: ", subtracao)
        case "*":
            print("O resultado é: ", multiplicacao)
        case "/":
            print("O resultado é: ", divisao)
        case "^":
            print("O resultado é: ", potencia)
        case "%":
            print("O resultado é: ", porcentagem)
        case "+%":
            print("O resultado é: ", soma_porcentagem)
        case "-%":
            print("O resultado é: ", subtracao_porcentagem)
        case _:
            print("Erro: Operação inválida.")


    #loop

    loop = input("Deseja repetir?: ")

    if loop == "nao":
        break
    elif loop == "sim":
        continue