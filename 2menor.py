qnt = int(input())
menor = 0
segmenor = 0

n = int(input())
menor = n
n = int(input())
if n >= menor:
    segmenor = n
else:
    segmenor = menor
    menor = n
for _ in range(qnt-2):
    n = int(input())
    if menor > n:
        segmenor = menor
        menor = n
    if segmenor > n and n > menor:
        segmenor = n
        
print(segmenor)        
