# Importando modulos: tenemos 3 opciones
# Opcion 1: importar todo un modulo
import random

# Llamar a funciones de random: nombreDelModulo.nombreDeLaFuncion
minumeroRandom = random.randint(1,100)
print(minumeroRandom)

# Opcion 2: importar el modulo pero con otro nombre que queramos
import random as r
#Llamar funciones:
miNuevoRandom = r.randint(1,100)
print(miNuevoRandom)

# Opcion 3: importar unicamente una funcion del modulo
from random import randint
# Llamar a la funcion
miUltimoRandom = randint(1,100)
print(miUltimoRandom)