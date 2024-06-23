numeros = [int(x) for x in input().split()]
maior = numeros[0]
for i in range(len(numeros)-1):
    if numeros[i] > maior:
        maior = numeros[i]

print(maior)