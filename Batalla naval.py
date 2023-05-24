#Implementar una función que permita ubicar la cantidad de enemigos recibidos por parámetro. 
def ubicacion(x):
    x = int(input("deposite la cantidad de enemigos a elección"))
    for i in range (codenadas_letras):
        randint: ["A","B","C","D","E","F","G","H","I","J"],["1","2","3","","","",",","","","",",","",])

barco_j1_letra = ""
barco_j2_numero = ""

barco_j1_numero = ""
barco_j2_letra = ""
linea =""
cantidad = int(input("Ingrese el tamanio del tablero:"))
cordenada_letra =[[" ","A","B","C","D","E","F","G","H","I","J"],["1"," "," "," "," "," "," "," "," "," "," "],["2"," "," "," "," "," "," "," "," "," "," "],["3"," "," "," "," "," "," "," "," "," "," "],["4"," "," "," "," "," "," "," "," "," "," "],["5"," "," "," "," "," "," "," "," "," "," "],["6"," "," "," "," "," "," "," "," "," "," "],["7"," "," "," "," "," "," "," "," "," "," "],["8"," "," "," "," "," "," "," "," "," "," "],["9"," "," "," "," "," "," "," "," "," "," "],["10"," "," "," "," "," "," "," "," "," "," "]]
cantidad +=1
for e in range (cantidad):
    for i in range (cantidad):
        linea += (cordenada_letra[e][i])+" "
    print (linea)
    linea =""
