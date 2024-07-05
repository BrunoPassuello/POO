n, m = [int(x) for x in input().split()]  #(n,m)

matriz = []
for _ in range(n):
    matriz.append([int(x) for x in input().split()])
    
maximo = 0
soma = 0
for i in range(n):
    if sum(matriz[i]) > maximo:
        maximo = sum(matriz[i])

for j in range(m): 
    for i in range(n):
        soma += matriz[i][j]
    if soma > maximo:
        maximo = soma
    soma = 0

print(maximo)