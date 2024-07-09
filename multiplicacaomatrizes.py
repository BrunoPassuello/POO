dim = int(input())

p, q, r, s, x, y = [int(x) for x in input().split()]

I, J = [int(x) for x in input().split()]  #posicao q eu quero em C

#Matriz A
matrizA = [[0 for _ in range(dim)] for _ in range(dim)]
for i in range(dim):
    for j in range(dim):
        numero = (p * (i+1) + q * (j+1)) % x
        matrizA[i][j] = numero

#Matriz B
matrizB = [[0 for _ in range(dim)] for _ in range(dim)]
for i in range(dim):
    for j in range(dim):
        numero = (r * (i+1) + s * (j+1)) % y
        matrizB[i][j] = numero
        
#matriz C
matrizC = [[0 for _ in range(dim)] for _ in range(dim)]
for l in range(dim):
    for i in range(dim):
        numero = 0
        for j in range(dim):
            numero += matrizA[i][j] * matrizB[j][l]
        matrizC[i][l] = numero

valor = matrizC[I-1][J-1]
print(valor)