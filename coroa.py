qnt = int(input())
##MARIA CARA = 0
##JOAO COROA = 1
resultado = [int(w) for w in input().split()]
print(f"Mary won {resultado.count(0)} and John win {qnt-resultado.count(0)} times")
while True:
    qnt = int(input())
    if qnt != 0:
        resultado = [int(w) for w in input().split()]
        print(f"Mary won {resultado.count(0)} and John win {qnt-resultado.count(0)} times")
       

