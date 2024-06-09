n = int(input())
binario = 0
while n // 2 != 0:
    n = n // 2
    binario = (n % 2)
    
print(binario)