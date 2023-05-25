#import
import random

#Implementar una función que permita ubicar la cantidad de enemigos recibidos por parámetro. 
def ubicacion_enemigos(cordenadas_enemigos_x,cordenadas_enemigos_y):
    print (cordenadas_enemigos_x)
    print (cordenadas_enemigos_y)
#fin def ubicacion

#Creacion de tablero
def tablero(linea,cantidad,cordenada_letra):
    cantidad +=1
    for e in range (cantidad):
        for i in range (cantidad):
            linea += (cordenada_letra[e][i])+""
        print (linea)
        linea =""
#fin def tablero

#DISPAROS
def disparos(cantidad_disparos,cordenadas_disparo_x,cordenadas_disparo_y,cordenadas_enemigos_x,cordenadas_enemigos_y,cordenada_letra,cordenadas_disparo):

        cordenadas_disparo_x = (int(cordenada_letra[0].index(" "+ cordenadas_disparo[0] + " ")))
        cordenadas_disparo_y = (int(cordenadas_disparo[1]))
        
        print(cordenadas_disparo_x)
        print(cordenadas_disparo_y)
        
        for e in range (cantidad_disparos):
            if (cordenadas_disparo_x == cordenadas_enemigos_x[e]) and (cordenadas_disparo_y == cordenadas_enemigos_y[e]):
                return True
#FIN DISPAROS

#tablero
cordenada_letra =[[" "," A "," B "," C "," D "," E "," F "," G "," H "," I "," J "],["1"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["2"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["3"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["4"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["5"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["6"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["7"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["8"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["9"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["10"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "]]
linea =""
cantidad = int(input("Ingrese el tamaño del tablero:"))
#ubicacion
cantidad_de_enemigos= int(input("Ingrese la cantidad de enemigos a elección"))
cordenadas_enemigos_x=[]
cordenadas_enemigos_y=[]
for i in range (cantidad_de_enemigos):
    x=random.randint(1,cantidad)
    y=random.randint(1,cantidad)
    cordenadas_enemigos_x.append(x)
    cordenadas_enemigos_y.append(y)
#Disparos
cantidad_disparos=2
cordenadas_disparo_x=0
cordenadas_disparo_y=0

#LLAMAR FUNCIONES
for i in range (cantidad_disparos):
    tablero(linea,cantidad,cordenada_letra) 
    ubicacion_enemigos(cordenadas_enemigos_x,cordenadas_enemigos_y)
    cordenadas_disparo = str(input("Ingrese una cordenada de la siguiente manera (LETRA,NUMERO)"))
    disparos(cantidad_disparos,cordenadas_disparo_x,cordenadas_disparo_y,cordenadas_enemigos_x,cordenadas_enemigos_y,cordenada_letra,cordenadas_disparo)
    
tablero(linea,cantidad,cordenada_letra) 
ubicacion_enemigos(cordenadas_enemigos_x,cordenadas_enemigos_y)
