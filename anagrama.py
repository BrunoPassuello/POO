palavra1 = input()
palavra2 = input()
tamanho1 = len(palavra1)
tamanho2 = len(palavra2)
letra1 = 0
letra2 = 0
contagem = 0
if tamanho1 == tamanho2:
    
    for _ in range(0, tamanho1, 1):
        
        while palavra1[letra1] != palavra2[letra2]:
            letra2 += 1
        if palavra1[letra1] == palavra2[letra2]:
            contagem +=1
    letra1 += 1
    letra2 = 0
    if contagem == tamanho1:
        print(True)
    else:
        print(False)
                        
else:
    print(False)
