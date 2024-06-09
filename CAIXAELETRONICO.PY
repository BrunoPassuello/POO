qnt = int(input())
contagem = qnt
notas = {}
listnotas = []
for _ in range(qnt):
    cedulas = float(input())
    qnt = int(input())
    notas[cedulas] = qnt
    listnotas.append(cedulas)    
listnotas.sort()
listnotas.reverse()
copianotas = notas.copy()
valor = float(input())
x = 0
i = 0

for _ in range(contagem):
    while listnotas[i] <= valor:
        x = listnotas[i]
        if notas[x] <= 0:
            break
        else:
            notas[x] = notas[x] - 1
            valor = valor - listnotas[i]
    i += 1

resultado = {chave: copianotas[chave] - notas.get(chave, 0) for chave in copianotas}
valores = resultado.values()
lista_valores = list(valores)
print(*lista_valores, sep=' ', end='')

