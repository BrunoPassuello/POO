gabarito = input()
prova = input()

qnt = len(gabarito)
contagem = 0
corretas = 0

for _ in range(0, qnt, 1):
    if gabarito[contagem] == prova[contagem]:
        corretas += 1
        contagem += 1
    else:
        contagem += 1
print(corretas)
    
