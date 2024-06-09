numero = 2

fatorial = numero
potencia = numero
def calculofatorial(numero):
    
    for i in range(1, numero+1):
        
        fatorial *= i
        
    return fatorial 
    
def calculopotencia(numero):
    potencia = numero**10
    return potencia
while fatorial == potencia:
    fatorial = calculofatorial(numero)
    potencia = calculopotencia(numero)
    numero += 1    
print(fatorial)