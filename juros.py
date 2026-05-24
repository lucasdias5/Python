while True:
    titulo = "CALCULADORA DE JUROS"
    print("\n{:=^30}".format(titulo))

    tipo = str(input("Qual tipo de juros você quer calcular?: "))
    capital = float(input("\nInsira o valor inicial: "))
    taxa = float(input("Insira o valor da taxa: "))
    tempo = float(input("Insira o tempo: "))

    juros = capital * taxa/100 * tempo
    jc = capital * (1+taxa/100)**tempo

    if tipo == "simples":
        print("Valor dos juros: ",juros,"\nTotal a pagar: ",capital + juros)
    elif tipo == "composto":
        print("Valor dos juros: ",jc,"\nTotal a pagar: ",capital + jc)

    sair = str(input("Deseja continuar?: "))
    if sair == "nao":break