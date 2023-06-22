# Declaro mi lista de usuarios:
nombreUsuarios = ["Juan", "Marta", "Miguel", "Elisa", "Claudia", "Jose"]

# Imprimir todos los nombres dentro de nombreUsuarios
for nombre in nombreUsuarios:  # la variable nombre puede ser de otro nombre cualquiera
    print(nombre)

# Crear una variable
indice = 1
for nombre in nombreUsuarios:
    print("El usuario", indice, "es", nombre)
    indice += 1

# Iterar a traves de las letras de un String
miString = "abcdefghijk"
for letra in miString:
    print(letra)

# Sintaxis bucle for:
# for elemento in listaElementos:
#       acceder al elemento individualmente con "elemento"