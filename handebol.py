N, M = [int(x) for x in input().split()]
contagem = 0
for _ in range(N):
    jogos = [int(x) for x in input().split()]
    if 0 not in jogos:
        contagem += 1
print(contagem)
    