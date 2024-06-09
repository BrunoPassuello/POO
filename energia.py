energia = int(input())
valor = 0

if energia <= 30:
    valor += energia * 0.09556
else:
    valor += 30 * 0.09556
    energia = energia - 30
    if energia <= 70:
        valor += energia * 0.16698
    else:
        valor += 70 * 0.16698
        energia = energia - 70
        if energia <= 100:
            valor += energia * 0.25052
        else:
            valor += 100 * 0.25052
            energia = energia - 100
            if energia > 0:
                valor += energia * 0.27836

print(f"{valor:.2f}")

    
