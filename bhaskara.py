import math
a = int(input("digite o valor de a:  "))
b = int(input("digite o valor de b:  "))
c = int(input("digite o valor de c:  "))

delta = b**2 - 4*a*c

x1 = (-b + math.sqrt(delta))/2*a
x2 = (-b - math.sqrt(delta))/2*a

print(x1, x2)