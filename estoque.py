tipo, tamanho = [int(x) for x in input().split()]
matriz = []

for m in range(tipo):
    matriz.append([int(x) for x in input().split()])

n = int(input())

for estoque in range(n):
    i, j = [int(x) for x in input().split()]
    if matriz[i-1][j-1] != 0:
        estoque += 1
        matriz[i-1][j-1] += -1
    else:
        estoque += 0

print(estoque)