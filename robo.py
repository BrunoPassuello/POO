#matriz
n, m = [int(x) for x in input().split()]
#posicaorobo
i, j = [int(x) for x in input().split()]

matriz = []
for _ in range(n):
    matriz.append([int(x) for x in input().split()])
    
i = i-1
j = j-1
posicaoy = i
poxicaox = j
matriz[i][j] = 0
while i > 0 and matriz[i-1][j] == 1 or i < n-1 and matriz[i+1][j] == 1 or j > 0 and matriz[i][j-1] == 1 or j < m-1 and matriz[i][j+1] == 1:
    if i > 0 and matriz[i-1][j] == 1: #cima
        i = i-1
        matriz[i][j] = 0
        
    if i < n-1 and matriz[i+1][j] == 1: #baixo
        i = i+1
        matriz[i][j] = 0
        
    if j > 0 and matriz[i][j-1] == 1: #esquerda
        j = j-1
        matriz[i][j] = 0
        
    if j < m-1 and matriz[i][j+1] == 1: #direita
        j = j+1
        matriz[i][j] = 0
    
print(f"{i+1} {j+1}")