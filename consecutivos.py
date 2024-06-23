n = int(input())
numeros = [int(x) for x in input().split()]
maiorseq = 0
contagem = 1
for i in range(len(numeros)-1):
    if numeros[i] == numeros[i+1]:
        contagem += 1
    else:
        contagem = 1
    if contagem > maiorseq:
        maiorseq = contagem

print(maiorseq)