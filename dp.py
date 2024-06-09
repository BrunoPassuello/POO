import math
n = int(input())
numeros = []
dp1 = 0
for mediaaritmetica in range(n):
    xi = float(input())
    numeros.append(xi)
    media = sum(numeros) / len(numeros)  
for x in numeros:
    dp1 += (x-media)**2
dp = math.sqrt(dp1/(n-1))

print(dp)