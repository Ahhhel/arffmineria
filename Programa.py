names=open("servo.names","tr")

lineas=names.readlines()

l1=lineas[0].split(": ")
nombreRelacion = l1[1]
nombreRelacion =  nombreRelacion[:-1]
print("@relation '"+ nombreRelacion+"'\n")

numAtributosmin = 0
for i in lineas:
    numAtributosmin+=1
    if (i[0] == "7"):
        break
numAtributosmax = 0
for i in lineas:
    numAtributosmax+=1
    if (i[0] == "8"):
        break
print(numAtributosmin)
print(" ")
print(numAtributosmax)




names.close()