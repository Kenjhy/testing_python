m=[]
x=int(input("cuantas filas queris: "))
y=int(input("ctas columnas: "))
for f in range(x):
    m.append([]) #le agrego una fila
    for c in range(y):
        #llenado de la primera columna de la fila
        if c==0 and f % 2 == 0:
            m[f].append(1)
        elif c==0 and f % 2 != 0:
            m[f].append(0)
        #llenado de las filas considerando el valor del primer elemento
        elif m[f][c]==1:
            m[f].append(0)
        elif m[f][c]==0:
            m[f].append(1)

for i in range(x):
    for j in range(y):
        print(m[i][j])
    print()