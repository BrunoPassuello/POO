casosdeteste = int(input())

n, m, x, y = [int(x) for x in input().split()]

matriz = [[0 for _ in range(n)] for _ in range(m)]
n = n-1
x = x-1
matriz[x][y] = 10

esquerda = y
e = esquerda - 1
direita = m - y
d = direita + 1
contagem = 1
for _ in range(esquerda):
    matriz[x][e] = 10 - contagem
    contagem += 1
    e -= 1
contagem = 1
for _ in range(direita):
    matriz[x][d] = 10 - contagem
    contagem += 1
    d += 1