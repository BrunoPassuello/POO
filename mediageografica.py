qnt = int(input())
produto = 1
for _ in range(qnt):
    produto *= float(input())
media = produto ** (1 / qnt)
print(media)
    