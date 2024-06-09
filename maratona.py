#+2000m após tomar agua (distancia intermediaria)
#distancia entre 2 posos <= distancia intermediaria
distint = [int(x) for x in input().split()]
postos = [int(x) for x in input().split()]
saida = ''
i = 1
for i in range(distint[0]-1):
    x = abs(postos[i] - (postos[i+1]))
    if x > distint[1]:
        saida = 'N'
        break
    else:
        saida = 'S'
        
print(saida)