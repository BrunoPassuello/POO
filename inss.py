salario = float(input())

if salario <= 720:
    inss = salario * 0.0765
    print(inss)

if salario <= 1200:
    inss = salario * 0.09
    print(inss)

if salario <= 2400:
    inss = salario * 0.11
    print(inss)
    
if salario > 2400:
    inss = 2400 * 0.11
    print(inss)