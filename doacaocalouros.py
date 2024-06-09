qntcalouros = int(input())

listacalouros = []
for _ in range(qntcalouros):
    nomescalouros = input()
    listacalouros.append(nomescalouros)
    
qntdoadores = int(input())

listadoadores = []
for _ in range(qntdoadores):
    nomesdoadores = input()
    listadoadores.append(nomesdoadores)
    
calourosdoadores = [item for item in listacalouros if item in listadoadores]


tamanhocalouros = len(listacalouros)
tamanhodoadores = len(calourosdoadores)

proporção = tamanhodoaodores / tamanhocalouros
