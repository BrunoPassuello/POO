contagem = 0
while True:
    qnt = int(input().lower().replace(' ', ''))
    if qnt != 0:
        numeros = [int(x) for x in input().split()]
        contagem += 1
        for i in range(len(numeros)):
            if numeros[i] == i+1:
                print(f"Teste {contagem}")
                print(i+1)
                print("")
                break