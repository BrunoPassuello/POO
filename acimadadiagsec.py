operacao = input()

matriz = []
dim = 12
media = 0
k = 11
for m in range(dim):
    linha = []
    for n in range(dim):
        linha.append(float(input()))
    matriz.append(linha)
    
if operacao == 'S':
    for i in range(0, (dim-1), 1):
        for j in range(0, k, 1):    
            media += matriz[i][j]  ##soma
        k -= 1
        
else:
    for i in range(0, (dim-1), 1):
        for j in range(0, k, 1):
            media += matriz[i][j]
        k -= 1
    media = media / 66
print(f"{media:.1f}")

