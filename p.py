frase = input()

frasenova = ''
contagem = 0
for p in range(len(frase)-1):
    if frase[contagem] == 'p' and frase[contagem+1] != 'p':
        frasenova += frase.replace(frase[contagem], '')
        contagem += 1
    else:
        frasenova += frase[contagem]
print(frasenova)