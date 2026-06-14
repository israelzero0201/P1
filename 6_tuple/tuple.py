"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""

# Creación de la tupla
coordenadas = (19.4326, -99.1332) # Coordenadas de la CDMX

# Acceder a sus elementos usando su índice [ ]
print(f"Latitud: {coordenadas[0]}")
print(f"Longitud: {coordenadas[1]}")

# Definición de colores fijos
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)

print(f"El valor RGB del blanco es: {COLOR_BLANCO}")

# Información fija de un videojuego (Título, Año de lanzamiento, ¿Está disponible?)
juego_info = ("Chrono Trigger", 1995, True)

# Recorrer la tupla con un ciclo
for dato in juego_info:
    print(dato)

# Tenemos una tupla con los datos de una persona
persona = ("Juan", 28, "México")

# Desempaquetamos la tupla
nombre, edad, pais = persona

# Ahora cada dato está en su propia variable
print(nombre)  # Imprime: Juan
print(edad)    # Imprime: 28