valor = float(input())
sexo = input()
idade = float(input())

bruto = valor * 0.1

if sexo == "M":
    if idade <= 24:
        print(bruto)
    
    if 25 <= idade <= 33:
        desconto = bruto * 0.1
        total = bruto - desconto
        print(total)
        
    if idade > 33:
        desconto = bruto * 0.2
        total = bruto - desconto
        print(total)
        
if sexo == "F":
    if idade <= 24:
        desconto = bruto * 0.05
        total = bruto - desconto
        print(total)
    
    if 25 <= idade <= 33:
        desconto = bruto * 0.2
        total = bruto - desconto
        print(total)
        
    if idade > 33:
        desconto = bruto * 0.35
        total = bruto - desconto
        print(total)
        