while True:
    try:
        n, m = [int(x) for x in input().split()]

        matriz =[]

        for _ in range(n):
            matriz.append(input().split())

        virar = ''

        for i in range(n):
            for j in range(m):
                if matriz[i][j] == 'X':
                    matriz[i][j] = '2'
                    y = i
                    x = j
                    break
        for i in range(n):
            for j in range(m):
                matriz[i][j] = int(matriz[i][j])
        i = y
        j = x
        virar = ''
        virado = ''
        contagem = 1

        if i > 0 and matriz[i-1][j] == 0: #cima
                virado = 'c'
        if i < n-1 and matriz[i+1][j] == 0: #baixo
                virado = 'b'
        if j > 0 and matriz[i][j-1] == 0: #esquerda
                virado = 'e'
        if j < m-1 and matriz[i][j+1] == 0: #direita
                virado = 'd'

        while i > 0 and matriz[i-1][j] == 0 or i < n-1 and matriz[i+1][j] == 0 or j > 0 and matriz[i][j-1] == 0 or j < m-1 and matriz[i][j+1] == 0:
            
            if i > 0 and matriz[i-1][j] == 0: #cima
                if virado == 'd':
                    virar += 'L'
                    virado = 'c'
                elif virado == 'e':
                    virar += 'R'
                    virado = 'c'
                
                i = i-1
                matriz[i][j] = 1
                virar += 'F'
            if i < n-1 and matriz[i+1][j] == 0: #baixo
                if virado == 'd':
                    virar += 'R'
                    virado = 'b'
                elif virado == 'e':
                    virar += 'L'
                    virado = 'b'
                i = i+1
                matriz[i][j] = 1
                virar += 'F'
            if j > 0 and matriz[i][j-1] == 0: #esquerda
                if virado == 'c':
                    virar += 'L'
                    virado = 'e'
                elif virado == 'b':
                    virar += 'R'
                    virado = 'e'
                j = j-1
                matriz[i][j] = 1
                virar += 'F'
            if j < m-1 and matriz[i][j+1] == 0: #direita
                if virado == 'c':
                    virar += 'R'
                    virado = 'd'
                elif virado == 'b':
                    virar += 'L'
                    virado = 'd'
                j = j+1
                matriz[i][j] = 1
                virar += 'F'
                
        virar += 'E'
        formatacao = ''
        for letra in virar:
            formatacao += letra
            formatacao += ' '
        formatacao = formatacao[:-1] 
        print(formatacao)
    except EOFError:
        break