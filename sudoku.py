teste = int(input())
contagem = 0
for _ in range(teste):
    contagem += 1
    matriz = []
    dim = 9
    sudoku = True
    for _ in range(dim):
        matriz.append([int(x) for x in input().split()])
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    comparacao = set()
    for i in range(dim):
        comparacao = set()
        for j in range(dim):
            numero = matriz[i][j]
            comparacao.add(numero)
    if comparacao != numeros:
        sudoku = False
        print(f"Instancia {contagem}")
        print("NAO")
        print("")
    else:
        for j in range(dim):
            comparacao = set()
            for i in range(dim):
                numero = matriz[i][j]
                comparacao.add(numero)
        if comparacao != numeros:
            sudoku = False
            print(f"Instancia {contagem}")
            print("NAO")
            print("")
        else:
            for l in range(0, dim, 3):
                conj = set()
                for c in range(0, dim, 3):
                    conj = set( matriz[l][c:c+3] + matriz[l+1][c:c+3] + matriz[l+2][c:c+3] ) 
                    if conj != comparacao:
                        sudoku = False
                        print(f"Instancia {contagem}")
                        print("NAO")
                        print("")
    if sudoku:
        print(f"Instancia {contagem}")
        print("SIM")
        print('')