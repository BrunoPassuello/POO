n = 12
matriz = []
listamedias = []
saida = ''
for _ in range(12):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)

for i in range(12):
    media = (sum(matriz[i]))/len(matriz[i])
    listamedias.append(round(media, 2))
    
for numero in listamedias:
    saida += str(numero)
    saida += ' '
    
print(saida, end='')