cpf = input()
valido = True
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
n = 10
multiplos = 0
primeiro = 0
segundo = 0
for k in cpf:
    if n == 1:
        break
    else:
        multiplos += int(k) * n
        n += -1
primeiro = 11 - (multiplos % 11)
if primeiro == 1:
    primeiro = 0
cpf2 = cpf[1:]
cpf2 += str(primeiro)
multiplos = 0
n = 10

for k in cpf2:
    if n == 1:
        break
    else:
        multiplos += int(k) * n
        n += -1

segundo = 11 - (multiplos % 11)
if segundo == 1:
    segundo = 0
if str(primeiro) != cpf[-2] or str(segundo) != cpf[-1]:
    valido = False
print(valido)
    
