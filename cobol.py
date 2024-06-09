while True:
    try:
        dict = {1: 'c', 2: 'o', 3: 'b', 4: 'o', 5: 'l'}
        i = 0
        pi = 1
        contagem = 0
        frase = input().replace('-', ' ').split()
        for letras in frase:
            if str(frase[i])[0] == dict[pi] or str(letras[-1]) == dict[pi]:
                contagem += 1
                if contagem == 5:
                    print("GRACE HOPPER")
                    break

            else:
                print("BUG")
                break    
            pi += 1
            i += 1
    except EOFError:
        break

