while True:
    t = 0
    n = int(input())
    if n == 0:
        break
    else:
        pessoas = [int(x) for x in input().split()]
        if len(pessoas) == 1:
            t = 10
        else:
            for i in range(len(pessoas)-1):
                if (pessoas[i] + 10) < pessoas[i+1]:
                    t += abs((pessoas[i] + 10) - (pessoas[i+1] + 10))
        print(t)