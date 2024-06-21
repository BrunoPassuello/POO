n = int(input().strip())
operacao = input()

matriz = []
dim = 12
##matriz mXn

for m in range(dim):
    linha = []
    for n in range(dim):
        linha.append(float(input()))
    matriz.append(linha)
soma = 0
media = 0
if operacao == 'S':
    media = sum(matriz[n-1])
else:
    media = (sum(matriz[n-1]))/dim
print(f"{media:.1f}")
