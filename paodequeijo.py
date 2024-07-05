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
            if 