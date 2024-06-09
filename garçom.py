#a, b, c = [int(w) for w in input().split()]
n = int(input())
quebrados = 0
for i in range(n):
    latas, copos = [int(w) for w in input().split()]
    if latas > copos:
        quebrados += copos
        
    else:
        quebrados += 0
        
        
print(quebrados)
    

