num = int(input())

indicemaisprox = None

diferencaminima = float('inf')

for _ in range(num):##qnt de casos de teste
    qntalunos, nsorteado = [int(x) for x in input().split()]
    numeros = [int(x) for x in input().split()]
    if nsorteado in numeros:
        indice = numeros.index(nsorteado)
        print(indice + 1)
    else:
        
        
        
        
        
        #????
        for i, elemento in enumerate(numeros):
            diferenca = abs(nsorteado - nsorteado)
            if diferenca < diferencaminima:
                diferencaminima = diferenca
                indicemaisprox = i
        print(indicemaisprox)