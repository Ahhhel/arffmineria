import re
from  tkinter import *
from tkinter import filedialog
import os
cwd = os.getcwd()#se detecta el directorio actual

#se preguntan por los archivos
root = Tk()
filename = ""
root.filename =  filedialog.askopenfilename(initialdir = cwd, title = "Archivo .names",filetypes = (("names files","*.names"),("all files","*.*")))
root.withdraw()
aname=root.filename
root = Tk()
filename = ""
root.filename =  filedialog.askopenfilename(initialdir = cwd, title = "Archivo .data",filetypes = (("data files","*.data"),("all files","*.*")))
root.withdraw()
adata=root.filename

#se abren los archivos .name y .data
names=open(aname,"tr")
archivoDatos =  open(adata,"tr")


#se leen todas las lineas de los archivos
lineas=names.readlines()
datos = archivoDatos.readlines()

#se detecta el nombre de la relacion
l1=lineas[0].split(": ") #se devide la primera linea del archivo para aislar el titulo
nombreRelacion = l1[1]
nombreRelacion =  nombreRelacion[:-1]
inicio= "@relation '"+ nombreRelacion+"'\n\n"

#se detectan los atributos
numAtributos = 0 #variable del numero de lineas que se recorren para encontrar los atributos
for i in lineas: #ciclo busca los atributos
    numAtributos+=1
    if (i[0] == "7"):
        break

#extracción de los atributos
atributos = {} #arreglo que almacenará los atributos sin formato
k=0 #contador
while True:
    if (lineas[numAtributos][0] == "8"):
        break
    if (lineas[numAtributos] != "\n"):
        k+=1
        atributos[k]=lineas[numAtributos].split(": ")
    numAtributos+=1
listaAtributos = {} #arreglo de arreglos que almacenará los atributos con formato
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
        
#detección de los datos
coleccionDatos = {}
g=0
for dato in datos:
    g+=1
    coleccionDatos[g] = re.split(",| |\n",dato)

#se crea el archivo arff
archivoarff = open(nombreRelacion+".arff","w")
#se escribe el encabezado
archivoarff.write(inicio)
#se escriben los atributos
for l in listaAtributos:
    archivoarff.write(listaAtributos[l])
    archivoarff.write("\n")
#se escribe el encabezado de los datos
archivoarff.write("\n@data\n")
#se escriben los datos
for l in coleccionDatos:
    for h in coleccionDatos[l]:
        if(h != ""):
            archivoarff.write(h+", ")
    pos=archivoarff.tell()
    archivoarff.seek(pos-2)
    archivoarff.write("\n")

#cierre de los dos archivos
archivoarff.close()
names.close()
############FIN DEL PROGRAMA##############