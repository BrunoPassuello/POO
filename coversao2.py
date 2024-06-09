origem = input()
valor = float(input())
saida = input()

elif origem == "c" and saida == "k":
    conversao = valor + 273.15
    print(conversao)
    
elif origem == "c" and saida == "f":
    conversao = valor * 1.8 + 32
    print(conversao)
    
elif origem == "c" and saida == "r":
    conversao = valor * 1.8 + 491.67
    print(conversao)
    
#K
elif origem == "k" and saida == "c":
    conversao = valor - 273.15
    print(conversao)
    
elif origem == "k" and saida == "f":
    conversao = (valor * 1.8) - 459.67
    print(conversao)
    
elif origem == "k" and saida == "r":
    conversao = valor * 1.8 
    print(conversao)
    
#f
elif origem == "f" and saida == "c":
    conversao = (valor - 32) / 1.8
    print(conversao)
    
elif origem == "f" and saida == "k":
    conversao = (valor + 459.67) / 1.8
    print(conversao)
    
elif origem == "f" and saida == "r":
    conversao = valor + 459.67
    print(conversao)
    
#r
elif origem == "r" and saida == "c":
    conversao = valor * 1.8 + 273.15
    print(conversao)
    
elif origem == "r" and saida == "k":
    conversao = valor / 1.8
    print(conversao)
    
elif origem == "r" and saida == "f":
    conversao = valor - 459.67
    print(conversao)