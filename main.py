n = 2
x = "X"
piso = "_"

if n < 1 or n > 10:
    n = 5

matriz = []

for f in range(n):
    for c in range(n):
        if f == c:
            if len(matriz) < f:
                matriz.append(x)
            else:
                matriz[c-1] = matriz[c-1]+x
        else:
            if f - c < 0:
                matriz.append(piso)
            else:
               matriz[f-c-1] = matriz[f-c-1] + piso
        #     if len(matriz) < f:
        #         matriz.append(piso)
        #     else:
        #         matriz[f] = matriz[f] + piso
        #     #matriz.append(piso)

print(matriz)
