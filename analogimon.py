while True:
    try:
        matriz = []
        n, m = [int(x) for x in input().split()]
        soma = 0
        for _ in range(n):
            matriz.append([int(x) for x in input().split()])
        for i in range(n):
            for j in range(m):
                if matriz[i][j] == 2:
                    analogimonk = i
                    analogimonl = j
                elif matriz[i][j] == 1:
                    ashi = i
                    ashj = j
        if analogimonk < ashi:
            soma += ashi - analogimonk
        else:
            soma += analogimonk - ashi
        if analogimonl < ashj:
            soma += ashj - analogimonl
        else:
            soma += analogimonl - ashj
        print(soma)
        
    except EOFError:
        break