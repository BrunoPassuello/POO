valorinicial = float(input())
valorfinal = 0

if valorinicial >= 500:
    desconto = 0.7
    if valorinicial > 1000:
        valor = valorinicial - 1000
        descontofinal = valor * 0.15
        valorfinal -= descontofinal
else:
    desconto = 0.8
        
valorfinal += valorinicial * desconto
print(f"{valorfinal:.2f}")
        
    