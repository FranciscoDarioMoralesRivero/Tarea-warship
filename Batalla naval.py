import random

# Función para imprimir la ubicación de los enemigos
def ubicacion_enemigos(cordenadas_enemigos_x, cordenadas_enemigos_y):
    print(cordenadas_enemigos_x)
    print(cordenadas_enemigos_y)

# Función para crear el tablero
def tablero(linea, cantidad, cordenada_letra):
    cantidad += 1
    for e in range(cantidad):
        for i in range(cantidad):
            linea += cordenada_letra[e][i] + " "
        print(linea)
        linea = ""

# Función para determinar la dificultad
def dificultad(cantidad, nivel):
    casillas = cantidad ** 2
    if nivel == 1:
        cantidad_disparos = int((70 * casillas) / 100)
    elif nivel == 2:
        cantidad_disparos = int((50 * casillas) / 100)
    elif nivel == 3:
        cantidad_disparos = int((30 * casillas) / 100)
    return cantidad_disparos

# Función para manejar los disparos
def disparos(cantidad_disparos, cordenadas_disparo_x, cordenadas_disparo_y, cordenadas_enemigos_x, cordenadas_enemigos_y, cordenada_letra, cordenadas_disparo):
    cordenadas_disparo_x = int(cordenada_letra[0].index(" " + cordenadas_disparo[0] + " "))
    cordenadas_disparo_y = int(cordenadas_disparo[1])

    for e in range(cantidad_de_enemigos):
        if cordenadas_disparo_x == cordenadas_enemigos_x[e] and cordenadas_disparo_y == cordenadas_enemigos_y[e]:
            print("TRUE")
            cordenada_letra[cordenadas_disparo_y][cordenadas_disparo_x] = " x "
            break
        if e == cantidad_de_enemigos - 1:
            print("FALSE")
            cordenada_letra[cordenadas_disparo_y][cordenadas_disparo_x] = " o "

# Creación del tablero
cordenada_letra = [["  ", " A ", " B ", " C ", " D ", " E ", " F ", " G ", " H ", " I ", " J "],
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
cordenadas_enemigos_x = []
cordenadas_enemigos_y = []

for i in range(cantidad_de_enemigos):
    x = random.randint(1, cantidad)
    y = random.randint(1, cantidad)
    cordenadas_enemigos_x.append(x)
    cordenadas_enemigos_y.append(y)

# Disparos
cantidad_disparos = dificultad(cantidad, nivel)
cordenadas_disparo_x = 0
cordenadas_disparo_y = 0

# Llamada a las funciones
for i in range(cantidad_disparos):
    tablero(linea, cantidad, cordenada_letra)
    ubicacion_enemigos(cordenadas_enemigos_x, cordenadas_enemigos_y)
    cordenadas_disparo = str(input("Ingrese una coordenada de la siguiente manera (LETRA,NUMERO):"))
    disparos(cantidad_disparos, cordenadas_disparo_x, cordenadas_disparo_y, cordenadas_enemigos_x, cordenadas_enemigos_y, cordenada_letra, cordenadas_disparo)

# Mostrar el tablero final
tablero(linea, cantidad, cordenada_letra)
ubicacion_enemigos(cordenadas_enemigos_x, cordenadas_enemigos_y)
