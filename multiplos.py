#intervalo [1, m]
n = int(input())
m = int(input())

i = 0
k = 0
while i <= m:
    i = i+1
    if i % n == 0:
        k += i
        print(k, end=' ')
        k = 0
        


        
