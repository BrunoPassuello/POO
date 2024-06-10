nome = input().split()
novo_nome = ''
i = 0
nome_2 = nome[1:-1]
for palavra in nome_2:
    if palavra == 'dos' or palavra == 'da' or palavra == 'de' or palavra == 'das' or palavra == 'e':
        novo_nome += ' ' + palavra 
        break
    
    else:
        novo_nome += ' ' + palavra[0] + '.'
print(f"{nome[0]}{novo_nome} {nome[-1]}")