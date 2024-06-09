pulo, qnt = [int(x) for x in input().split()]
alturas = [int(x) for x in input().split()]

posicao = 0
certos = 0 

for _ in range(qnt-1):
    if ((alturas[posicao+1]) - alturas[posicao]) <= pulo:
        certos += 1
        posicao += 1
        
    else:
        break
if certos == qnt-1:
    print('YOU WIN')
else:
    print('GAME OVER')
        