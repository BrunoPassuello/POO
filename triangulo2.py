a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(f"equilátero") 
if a == c and a != b and b != c or a != c and a != b and b == c or a == b and b != c and a != c:
    print(f"isósceles")
if a != b and a!= c and b!=c:
    print(f"escaleno")
        