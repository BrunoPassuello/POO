qnt = int(input())

contagem = 0
for _ in range(qnt):
    nome = input()
    x = len(nome)
    if 'Maria' in nome:
        indice_maria = nome.index('Maria')
        if indice_maria + 5 < len(nome) and nome[indice_maria+5] == ' ':
            contagem += 1
        if nome[x-5:x+4] == 'Maria':
            contagem += 1
print(contagem)
