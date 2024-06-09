cartas = [int(x) for x in input().split()]
cartascres = cartas.copy()
cartascres.sort()
cartasdecres = cartascres.copy()
cartasdecres.sort(reverse = True)

if cartas == cartascres:
    print('C')
else:
    if cartas == cartasdecres:
        print('D')
    else:
        print('N')