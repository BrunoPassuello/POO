while True:
    
    A, D = [int(x) for x in input().split()]
    if A == 0 and D == 0:
        break
    else:
        atacantes = [int(x) for x in input().split()]
        defensores = [int(x) for x in input().split()]
        atacantes.sort()
        defensores.sort()
        del defensores[0]
        if atacantes[0] >= defensores[0]:
            print("N")
        else:
            print("Y")
