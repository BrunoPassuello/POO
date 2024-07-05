while True:
    n = int(input())
    if n != 0:
        print('')
    ##matriz nXn

        matriz = [[0 for _ in range(n)] for _ in range(n)]

        k = 0 # a cada linha k += 1
        for i in range(n):
            l = k
            for j in range(n):
                matriz[i][j] = 2 ** l
                l += 1
            k += 1

        g = matriz[-1][-1]
        g = len(str(g))
        for linha in matriz:
                # Formatar cada elemento da linha com espaçamento de 2
                linha_formatada = " ".join(f"{num:>{g}}" for num in linha)
                print(linha_formatada)
    
    else:
        break