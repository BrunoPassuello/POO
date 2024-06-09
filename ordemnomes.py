qnt1 = int(input())

nomes = []

for _ in range(qnt1):
    nome = input()
    nomes.append(nome)
    
    
qnt2 = int(input())

for _ in range(qnt2):
    nome = input()
    nomes.append(nome)
    
nomes.sort()
contagem = 0
tamanho = len(nomes)

for _ in range(tamanho):
    print(nomes[contagem])
    contagem += 1