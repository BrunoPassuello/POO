while True:
    n, k = [int(x) for x in input().split()]
    if n == 0 and k == 0:   
        break
    else:
        numeros = [int(x) for x in input().split()]
        cont_perguntas = 0
        for id in set(numeros):
            if numeros.count(id) >= k:
                cont_perguntas += 1    
    print(cont_perguntas)