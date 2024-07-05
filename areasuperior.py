operacao = input()

matriz = []
dim = 12
media = 0
i = 1 #esquerda
j = 11 #direita (11-1)

for m in range(dim):
    linha = []
    for n in range(dim):
        linha.append(float(input()))
    matriz.append(linha)
    
if operacao == 'S':
    for k in range(0, 5, 1):
        for l in range(i, j, 1): #10x
            media += matriz[k][l]
        i += 1
        j -= 1
else:
    for k in range(0, 5, 1):
        for l in range(i, j, 1): #10x
            media += matriz[k][l]
        i += 1
        j -= 1
    media = media / 30
    
print(f"{media:.1f}")