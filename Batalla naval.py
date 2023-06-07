import math
import random

# Función para crear el tablero
def crear_tablero(cantidad, coordenadas_letras):
    for e in range(cantidad + 1):
        linea = ""
        for i in range(cantidad + 1):
            linea += coordenadas_letras[e][i] + " "
        print(linea)

# Función para imprimir la ubicación de los enemigos
def imprimir_ubicacion_enemigos(enemigos_x, enemigos_y,coordenadas_letras):
    print("Ubicación de los enemigos restantes:")
    for i in range(len(enemigos_x)):
        print("Enemigo", i+1, ":", coordenadas_letras[0][enemigos_x[i]],enemigos_y[i])

# Función para determinar la cantidad de disparos
def determinar_cantidad_disparos(cantidad, nivel):
    casillas = cantidad ** 2
    if nivel == 1:
        cantidad_disparos = math.ceil((70 * casillas) / 100)
    elif nivel == 2:
        cantidad_disparos = math.ceil((50 * casillas) / 100)
    elif nivel == 3:
        cantidad_disparos = math.ceil((30 * casillas) / 100)
    return cantidad_disparos

# Función para manejar los disparos
def realizar_disparo(enemigos_x, enemigos_y, coordenadas_letras, coordenadas_disparo):
    disparo_x = coordenadas_letras[0].index(" " + coordenadas_disparo[0] + " ")
    disparo_y = int(coordenadas_disparo[1])
    for i in range(len(enemigos_x)):
        if disparo_x == enemigos_x[i] and disparo_y == enemigos_y[i]:
            coordenadas_letras[disparo_y][disparo_x] = " x "
            enemigos_x.pop(i)
            enemigos_y.pop(i)
            print("Hundido, quedan", len(enemigos_x), "enemigos")
            return True
    print("Agua, quedan", len(enemigos_x), "enemigos")
    coordenadas_letras[disparo_y][disparo_x] = " o "
    return False

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

cantidad = int(input("Ingrese el tamaño del tablero (De entre 3 y 10): "))
while cantidad < 3 or cantidad > 10:
    print("Tamaño inválido. Intente nuevamente.")
    cantidad = int(input("Ingrese el tamaño del tablero (De entre 3 y 10): "))

# Dificultad
nivel = int(input("Ingrese la dificultad (1 = fácil, 2 = medio, 3 = difícil): "))
while nivel < 1 or nivel > 3:
    print("Dificultad inválida. Intente nuevamente.")
    nivel = int(input("Ingrese la dificultad (1 = fácil, 2 = medio, 3 = difícil): "))

# Ubicación de los enemigos
cantidad_de_enemigos = int(input("Ingrese la cantidad de enemigos (máx. {}): ".format(cantidad)))
while cantidad_de_enemigos > cantidad:
    print("Límite de enemigos superado. Intente con un valor menor.")
    cantidad_de_enemigos = int(input("Ingrese la cantidad de enemigos (máx. {}): ".format(cantidad)))

enemigos_x = random.sample(range(1, cantidad + 1), cantidad_de_enemigos)
enemigos_y = random.sample(range(1, cantidad + 1), cantidad_de_enemigos)

# Disparos
cantidad_disparos = determinar_cantidad_disparos(cantidad, nivel)
print("Cantidad de disparos disponibles:", cantidad_disparos)

# Lista para almacenar los disparos realizados
disparos_realizados = []

# Llamada a las funciones
disparos_efectuados = 0
for i in range(cantidad_disparos):
    print("Disparo", i+1)
    crear_tablero(cantidad, coordenadas_letras)
    #imprimir_ubicacion_enemigos(enemigos_x, enemigos_y, coordenadas_letras)
    coordenadas_disparo = input("Ingrese una coordenada de la siguiente manera (LETRA, NUMERO): ").upper()
    while len(coordenadas_disparo) != 2 or not coordenadas_disparo[0].isalpha() or not coordenadas_disparo[1].isdigit():
        print("Coordenadas inválidas. Vuelva a intentarlo.")
        coordenadas_disparo = input("Ingrese una coordenada de la siguiente manera (LETRA, NUMERO): ").upper()
    print("------------------------------------------------------------------")
    disparo_acertado = realizar_disparo(enemigos_x, enemigos_y, coordenadas_letras, coordenadas_disparo)
    disparos_realizados.append(coordenadas_disparo)
    disparos_efectuados += 1
    if disparo_acertado:
        print("¡Enemigo acertado!")
        if len(enemigos_x) == 0:
            print("¡Has destruido a todos los enemigos!")
            break

# Mostrar el tablero final
print("Tablero final:")
crear_tablero(cantidad, coordenadas_letras)
imprimir_ubicacion_enemigos(enemigos_x, enemigos_y,coordenadas_letras)

# Mostrar estadísticas de la partida
print("Cantidad de disparos efectuados:", disparos_efectuados)
print("Cantidad de enemigos acertados:", cantidad_de_enemigos - len(enemigos_x))
print("Secuencia de disparos realizados:", disparos_realizados)
