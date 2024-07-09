casosdeteste = int(input())
for _ in range(casosdeteste):
    n, m, x, y = [int(x) for x in input().split()]
    matriz = []
    for _ in range(n):
        matriz.append([int(x) for x in input().split()])
    #matriz  
    ni = n-1
    mi = m-1
    #soco (x,y)
    xi = x-1
    yi = y-1
    
    matriz[xi][yi] = matriz[xi][yi] + 10
     
    direita = mi - yi
    esquerda = yi
    cima = xi 
    baixo = ni - xi
    contagem = 0
    d = 0
    
    #cima
    for i in range(1, cima+1):
        contagem += 1
        d += 1
        matriz[xi+i][yi+d] = matriz[xi][yi+d] + 10 - contagem
    
    
    
    
    
    
    
    
    
    
    
    #mesma linha
    for _ in range(direita):
        contagem += 1
        d += 1
        matriz[xi][yi+d] = matriz[xi][yi+d] + 10 - contagem
            
    contagem = 0
    d = 0
    for _ in range(esquerda):
        contagem += 1
        d += 1
        matriz[xi][yi-d] = matriz[xi][yi-d] + 10 - contagem    
    #cima
    d = 0
    contagem = 0
    for i in range(cima):
        contagem += 1
        d += 1
        matriz[xi+d][yi] = matriz[xi+d][yi] + 10 - contagem
    
    #baixo
    d = 0
    contagem = 0
    for i in range(cima):
        contagem += 1
        d += 1
        matriz[xi-d][yi] = matriz[xi-d][yi] + 10 - contagem