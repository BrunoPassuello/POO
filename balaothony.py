while True:
    linha = 1
    lin, col, k = [int(x) for x in input().split()]
    if lin != 0 and col != 0 and k != 0:
        k -= 1
        for l in range(lin):
            compartimentos = [int(y) for y in input().split()]

            i = k
            while compartimentos[i] == 0:
                i -= 1
                
            j = k
            while compartimentos[j] == 0:
                j += 1

            resultante = compartimentos[i] - compartimentos[j]
            k += resultante

            estoura = k <= i or k >= j
            if estoura == True:
                print(f"BOOM {linha} {k+1}")
                break
            else:
                linha += 1
        if estoura == True:
                break
        else:
            print(f"OUT {k+1}")
    else:
        break