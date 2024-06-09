qnt = int(input())
menor = 0

n = int(input())
menor = n
for _ in range(qnt-1):
    n = int(input())
    if menor > n:
        menor = n
   
print(menor)        