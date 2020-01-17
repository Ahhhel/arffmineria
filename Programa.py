# names=open("shuttle-landing-control.names","tr")
names=open("servo.names","tr")

lineas=names.readlines()

l1=lineas[0].split(": ")
nombreRelacion = l1[1]
nombreRelacion =  nombreRelacion[:-1]


numAtributos = 0
for i in lineas:
    numAtributos+=1
    if (i[0] == "7"):
        break


k=0

atributos = {}

while True:
    if (lineas[numAtributos][0] == "8"):
        break
    if (lineas[numAtributos] != "\n"):
        k+=1
        atributos[k]=lineas[numAtributos].split(": ")
    numAtributos+=1


listaAtributos = {}

j=0

for atributo in atributos:
    j+=1
    nombre= atributos[atributo][0].split(". ")
    detalles = atributos[atributo][1]
    detalles = detalles[:-1]
    if (" " in detalles):
        listaAtributos[j]="@attribute "+nombre[1]+" NUMERIC"
    else:
        listaAtributos[j]="@attribute "+nombre[1]+" {"+detalles+"}"
    





inicio= "@relation '"+ nombreRelacion+"'\n\n"

for l in listaAtributos:
    print(listaAtributos[l])

archivoarff = open(nombreRelacion+".arff","w")

archivoarff.write(inicio)
for l in listaAtributos:
    archivoarff.write(listaAtributos[l])
    archivoarff.write("\n")
archivoarff.close()
    
names.close()