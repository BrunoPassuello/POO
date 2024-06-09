n = int(input())
nomeprimeiro = ''
maiorsalto = 0
a, b, c, nome = [(w) for w in input().split()]
A = float(a)
B = float(b)
C = float(c)

if A > B and A > C:
    maiorsalto = A
elif B > A and B > C:
    maiorsalto = B
elif C > B and C > A:
    maiorsalto = C
nomeprimeiro = nome
       
for _ in range(n-1):
    a, b, c, nome = [(w) for w in input().split()]
    A = float(a)
    B = float(b)
    C = float(c)
    
    if A > maiorsalto:
        maiorsalto = A
        nomeprimeiro = nome
    elif B > maiorsalto:
        maiorsalto = B
        nomeprimeiro = nome
    elif C > maiorsalto:
        maiorsalto = C
        nomeprimeiro = nome
           
print(nomeprimeiro)