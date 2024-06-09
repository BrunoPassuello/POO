num = int(input())

soma = 0
p = 1
for _ in range(num):
    n = int(input())
    for i in range(1, n, p):   
        if n % p == 0:
            soma += i
        p += 1

    if n == soma:
        print(f"{n} eh perfeito")
    else:
        print(f"{n} nao eh perfeito")
    soma = 0
    p = 1
    
