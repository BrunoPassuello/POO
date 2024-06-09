qnt = int(input("Quantas palavras você quer adicionar à lista? "))
lista = []  # A lista deve ser inicializada fora do loop

for _ in range(qnt):
    palavra = input("Digite uma palavra: ")  # Coletar a palavra individualmente
    lista.append(palavra)  # Adicionar a palavra à lista

lista.sort()  # Ordenar a lista após adicionar todas as palavras
print(lista)  # Imprimir a lista ordenada