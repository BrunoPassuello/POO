def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input())
resultado = calcular_fatorial(numero)
print(resultado)