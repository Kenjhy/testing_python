myArray = [1, 3, 4, 2, 7, 0]

a = 0
b = 0
b_ = False
for i, m in enumerate(myArray):
    #print("")
    for m2 in range(len(myArray)):
        if m2 + i + 1 < len(myArray):
            #print(m + myArray[m2 + i + 1])
            if m + myArray[m2 + i + 1] == 10:
                a = m
                b =  myArray[m2 + i + 1]
                b_ = True
                break
    if b_:
        break
print(a,b)

