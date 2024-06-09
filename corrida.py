ncarros, nvoltas = [int(x) for x in input().split()]
soma = 0
primeiro = 0
iprimeiro = 0
segundo = 0
isegundo = 0
terceiro = 0
iterceiro = 0
i = 1
for _ in range(ncarros):
    tempos = [int(x) for x in input().split()]
    soma = sum(tempos)
    if soma > terceiro and soma > segundo and soma > primeiro:
        iprimeiro = i
        primeiro = soma
    else:
        if soma > terceiro and soma > segundo and soma < primeiro:
            isegundo = i
            segundo = soma
        else:
            if soma > terceiro and soma < segundo and soma < primeiro:
                iterceiro = i
                terceiro = soma
    i += 1
    soma = 0
print(iprimeiro)
print(isegundo)
print(iterceiro)