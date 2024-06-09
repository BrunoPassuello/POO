n = int(input())
distcentro = 0
media = 0
praia, distancia = input().split(';')
distancia = int(distancia)

maislonge = distancia
praiamaislonge = praia
if 15 <= distancia <= 20:
    distcentro += 1
media += distancia
for _ in range(n-1):
    praia, distancia = input().split(';')
    distancia = int(distancia)
    if distancia > maislonge:
        maislonge = distancia
        praiamaislonge = praia
    if 15 <= distancia <= 20:
        distcentro += 1
    media += distancia
    
media = round(media/n, 1)
    
print(f"{praiamaislonge};{distcentro};{media}")    