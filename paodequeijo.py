while True:
    try:
        n, m = [int(x) for x in input().split()]
        matriz = []
        matriznova = [[0 for _ in range(m)] for _ in range(n)]


        for _ in range(n):
            matriz.append([int(x) for x in input().split()]) 

        for i in range(n):
            for j in range(m):
                paesadjacentes = 0
                if matriz[i][j] == 1:
                    matriznova[i][j] = 9
                    
                else:
                    if i > 0 and matriz[i-1][j] == 1:  # cima
                        paesadjacentes += 1
                    if i < n-1 and matriz[i+1][j] == 1:  # baixo
                        paesadjacentes += 1
                    if j > 0 and matriz[i][j-1] == 1:  # esquerda
                        paesadjacentes += 1
                    if j < m-1 and matriz[i][j+1] == 1:  # direita
                        paesadjacentes += 1
                    matriznova[i][j] = paesadjacentes

        for i in range(n):
            linha = ''
            for j in range(m):
                numero = matriznova[i][j]
                linha += str(numero)
            print(linha)
    except EOFError:
        break
