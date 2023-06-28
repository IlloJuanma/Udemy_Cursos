# 3 pasos a seguir para importar un modulo propio
# 1 - Tener el modulo localizado
# 2 - Hacer un import sys
# 3 - Añadir al path nuestro modulo

import sys # Nos da acceso a ciertas funciones del sistema

if ("C:/Users/Usuario/OneDrive/Escritorio/ModulosPython" not in sys.path):
    sys.path.append("C:/Users/Usuario/OneDrive/Escritorio/ModulosPython")

import funcionesmatematicas

miNumero = 28

miCuadrado = funcionesmatematicas.cuadrado(miNumero)
print(miCuadrado)
