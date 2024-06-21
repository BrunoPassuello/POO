while True:
    tautograma = True
    palavra = input()
    if palavra == "*":
        break
    else:
        palavra = palavra.lower()
        letra = palavra[0]
        for i in range(len(palavra)):
            
            if palavra[i] == ' ':
                if palavra[i+1] != letra:
                    tautograma = False
                    break
            i += 1
        if tautograma == True:
            print('Y')
        else:
            print('N')
