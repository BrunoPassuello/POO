x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())

pares = 0
impares = 0
positivos = 0
negativos = 0

if x1 % 2 == 0:
    pares += 1
else:
    impares += 1
    
    
if x2 % 2 == 0:
    pares += 1
else:
    impares += 1
    
    
if x3 % 2 == 0:
    pares += 1
else:
    impares += 1
    
    
if x4 % 2 == 0:
    pares += 1
else:
    impares += 1
    
    
if x5 % 2 == 0:
    pares += 1
else:
    impares += 1

if x1 > 0:
    positivos += 1
else:
    if x1 != 0:
        negativos += 1
    
if x2 > 0:
    positivos += 1
else:
    if x2 != 0:
        negativos += 1
    
if x3 > 0:
    positivos += 1
else:
    if x3 != 0:
        negativos += 1
    
if x4 > 0:
    positivos += 1
else:
    if x4 != 0:
        negativos += 1
    
if x5 > 0:
    positivos += 1
else:
    if x5 != 0:
        negativos += 1

    
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")
    