n = int(input())
for _ in range(n):
    lista = []
    listaorg = []
    conjunto = set()
    lista = input().split()
    conjunto.update(lista)
    listaorg.extend(conjunto)
    listaorg.sort()
    print(" ".join(listaorg))
    
    
    