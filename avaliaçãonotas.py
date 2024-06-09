a = float(input())
b = float(input())
c = float(input())

media = (a + b + c) / 3

if media >= 9:
    print(f"Ótimo")
    
if 9 > media >= 7.5:
    print(f"Bom")
    
if 7.5 > media >= 6:
    print(f"Satisfatório")
    
if 6 > media >=0:
    print(f"Insuficiente")