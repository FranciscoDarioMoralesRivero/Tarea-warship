#import
import random
#Implementar una función que permita ubicar la cantidad de enemigos recibidos por parámetro. 
def ubicacion_enemigos(cantidad_de_enemigos,cordenadas_enemigos_x,cordenadas_enemigos_y,cantidad):
    for i in range (cantidad_de_enemigos):
        x=random.randint(1,cantidad)
        y=random.randint(1,cantidad)
        cordenadas_enemigos_x.append(x)
        cordenadas_enemigos_y.append(y)
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
def disparos(cantidad_disparos,cordenadas_disparo_x,cordenadas_disparo_y,cordenadas_enemigos_x,cordenadas_enemigos_y,cordenada_letra):
    for i in range (cantidad_disparos):
        cordenadas_disparo = str(input("Ingrese una cordenada de la siguiente manera (LETRA,NUMERO)"))

        cordenadas_disparo_x_simp = (cordenadas_disparo[0])

        cordenadas_disparo_x.append (int(cordenada_letra[0].index(" "+ cordenadas_disparo_x_simp + " ")))
        cordenadas_disparo_y.append (int(cordenadas_disparo[1]))
        
        print(cordenadas_disparo_x)
        print(cordenadas_disparo_y)
        
        for e in 
        if (cordenadas_disparo_x == cordenadas_enemigos_x) and (cordenadas_disparo_y == cordenadas_enemigos_y):
            return True

#ubicacion
cantidad_de_enemigos= int(input("Ingrese la cantidad de enemigos a elección"))
cordenadas_enemigos_x=[]
cordenadas_enemigos_y=[]
#tablero
cordenada_letra =[[" "," A "," B "," C "," D "," E "," F "," G "," H "," I "," J "],["1"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["2"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["3"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["4"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["5"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["6"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["7"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["8"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["9"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "],["10"," - "," - "," - "," - "," - "," - "," - "," - "," - "," - "]]
linea =""
cantidad = int(input("Ingrese el tamaño del tablero:"))
#Disparos
cantidad_disparos=5
cordenadas_disparo_x=[]
cordenadas_disparo_y=[]



#LLAMAR FUNCIONES
tablero(linea,cantidad,cordenada_letra) 
ubicacion_enemigos(cantidad_de_enemigos,cordenadas_enemigos_x,cordenadas_enemigos_y,cantidad)
disparos(cantidad_disparos,cordenadas_disparo_x,cordenadas_disparo_y,cordenadas_enemigos_x,cordenadas_enemigos_y,cordenada_letra)
