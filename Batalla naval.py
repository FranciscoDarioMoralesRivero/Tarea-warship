
import random

# Función para crear el tablero
def crear_tablero(linea, cantidad, coordenadas_letras):
    cantidad += 1
    for e in range(cantidad):
        for i in range(cantidad):
            linea += coordenadas_letras[e][i] + " "
        print(linea)
        linea = ""

# Función para imprimir la ubicación de los enemigos
def imprimir_ubicacion_enemigos(enemigos_x, enemigos_y):
    print(enemigos_x)
    print(enemigos_y)

# Función para determinar la dificultad
def determinar_cantidad_disparos(cantidad, nivel):
    casillas = cantidad ** 2
    if nivel == 1:
        cantidad_disparos = int((70 * casillas) / 100)
    elif nivel == 2:
        cantidad_disparos = int((50 * casillas) / 100)
    elif nivel == 3:
        cantidad_disparos = int((30 * casillas) / 100)
    return cantidad_disparos

# Función para manejar los disparos
def realizar_disparo(disparo_x, disparo_y, enemigos_x, enemigos_y, coordenadas_letras, cordenadas_disparo):
    disparo_x = int(coordenadas_letras[0].index(" " + cordenadas_disparo[0] + " "))
    disparo_y = int(cordenadas_disparo[1])

    for e in range(cantidad_de_enemigos):
        if disparo_x == enemigos_x[e] and disparo_y == enemigos_y[e]:
            print("TRUE")
            coordenadas_letras[disparo_y][disparo_x] = " x "
            break
        if e == cantidad_de_enemigos - 1:
            print("FALSE")
            coordenadas_letras[disparo_y][disparo_x] = " o "

# Creación del tablero
coordenadas_letras = [["  ", " A ", " B ", " C ", " D ", " E ", " F ", " G ", " H ", " I ", " J "],
                      [" 1", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
                      [" 2", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
                      [" 3", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
                      [" 4", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
                      [" 5", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
                      [" 6", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
                      [" 7", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
                      [" 8", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
                      [" 9", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
                      ["10", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]]

linea = ""
cantidad = int(input("Ingrese el tamaño del tablero:"))

# Dificultad
nivel = int(input("Ingrese la dificultad (1 = fácil)(2 = medio)(3 = difícil):"))

# Ubicación de los enemigos
cantidad_de_enemigos = int(input("Ingrese la cantidad de enemigos a elección:"))
enemigos_x = []
enemigos_y = []

for i in range(cantidad_de_enemigos):
    x = random.randint(1, cantidad)
    y = random.randint(1, cantidad)
    enemigos_x.append(x)
    enemigos_y.append(y)

# Disparos
cantidad_disparos = determinar_cantidad_disparos(cantidad, nivel)
disparo_x = 0
disparo_y = 0

# Llamada a las funciones
for i in range(cantidad_disparos):
    crear_tablero(linea, cantidad, coordenadas_letras)
    imprimir_ubicacion_enemigos(enemigos_x, enemigos_y)
    coordenadas_disparo = str(input("Ingrese una coordenada de la siguiente manera (LETRA,NUMERO):"))
    while True:
        if len(coordenadas_disparo) != 2 or coordenadas_disparo[0].isalpha() == False or coordenadas_disparo[1].isdigit() == False:
            print("Coordenadas inválidas. Vuelva a intentarlo.")
            coordenadas_disparo = input("Ingrese una coordenada de la siguiente manera (LETRA,NUMERO):")
        else:
            break
    realizar_disparo(disparo_x, disparo_y, enemigos_x, enemigos_y, coordenadas_letras, coordenadas_disparo)

# Mostrar el tablero final
crear_tablero(linea, cantidad, coordenadas_letras)
imprimir_ubicacion_enemigos(enemigos_x, enemigos_y)
