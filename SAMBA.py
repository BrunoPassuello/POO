soma = 0
notas = [float(x) for x in input().split()]
notas.sort()
notas.pop(0)
notas.pop(-1)
soma = sum(notas)
print(f"{soma:.1f}")