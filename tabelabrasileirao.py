#Cv , Ce, Cs, Fv, Fe, Fs

tabela = [int(x) for x in input().split()]
pontosC = 0
pontosC += tabela[0] * 3
pontosC += tabela[1] 

pontosF = 0
pontosF += tabela[3] * 3
pontosF += tabela[4]
if pontosC != pontosF:
    if pontosC > pontosF:
        print('C')
    else:
        print('F')
else:
    if tabela[2] == tabela[5]:
            print('=')
    else:
        if tabela[2] > tabela[5]:
            print('C')
        else:
            print('F')
