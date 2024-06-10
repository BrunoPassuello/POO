qnt_carros, n_voltas = [int(x) for x in input().split()]

lugares = [99999990,99999995,99999999]
i1 = 0
i2 = 0
i3 = 0
i = 0
for _ in range(qnt_carros):
    tempo = ([int(x) for x in input().split()])
    tempo_somado = sum(tempo)
    i += 1
    if tempo_somado < lugares[2] and tempo_somado > lugares[1]:
        lugares[2] = tempo_somado
        i3 = i        
    if tempo_somado < lugares[1] and tempo_somado > lugares[0]:
        lugares[2] = lugares[1]
        lugares[1] = tempo_somado
        i3 = i2
        i2 = i        
    if tempo_somado < lugares[0] :
        lugares[2] = lugares[1]
        lugares[1] = lugares[0]
        lugares[0] = tempo_somado
        i3 = i2
        i2 = i1
        i1 = i     
print(i1)
print(i2)
print(i3)

    
            