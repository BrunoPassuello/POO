qnt = int(input())

sequencia = 0
maior = 0
maiorsequencia = 0

n = int(input())
sequencia += 1
maior = n
maiorsequencia = sequencia
for _ in range(qnt-1):
    n = int(input())
    sequencia += 1
    if n > maior:
        maior = n
        maiorsequencia = sequencia

print(f"{maior} {maiorsequencia}")
        
