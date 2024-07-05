matriz = []
magico = True
n = int(input()) #matriz nxn
soma = 0

for _ in range(n):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)

numero = sum(matriz[0])

for i in range(n-1):   #linha
    if sum(matriz[i]) != sum(matriz[i+1]):
        magico = False
        break
        
for j in range(n):   #coluna
    for i in range(n):
        soma += matriz[i][j]
    if soma != numero:
        magico = False
        break
    else:
        soma = 0
        
soma = 0

for i in range(n): #diagonal princ
    soma += matriz[i][i]
if soma != numero:
    magico = False
else:
    soma = 0
        
j = 0
for i in range((n-1), -1, -1):
    soma += matriz[i][j]
    j += 1
if soma != numero:
    magico = False
        
            
print(magico)