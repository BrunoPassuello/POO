while True:
    try: 
        n = int(input())

        matriz = [[0 for _ in range(n)] for _ in range(n)]

        maximomatriz = n - 1

        minimodo1 = round((n / 3)) - 1
        maximodo1 = maximomatriz - minimodo1
        #1
        for i in range(minimodo1, maximodo1+1, 1):
            for j in range(minimodo1, maximodo1+1, 1):
                matriz[i][j] = 1
        #4
        lugardo4 = int(maximomatriz / 2)
        matriz[lugardo4][lugardo4] = 4        

        #2
        for i in range(n):
            if matriz[i][i] == 0:
                matriz[i][i] = 2
                
        #3
        k = maximomatriz
        for i in range(n):
            for j in range(1):
                if matriz[i][k] == 0:
                    matriz[i][k] = 3
            k -= 1

        for i in range(n):
            linha = ''
            for j in range(n):
                    m = matriz[i][j]
                    linha += str(m)
            print(linha)
        print('')
            
    except EOFError:
        break
    