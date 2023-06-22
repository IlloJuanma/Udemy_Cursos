num1 = input("Introduce el primer numero: ")
num2 = input("Introduce el primer numero: ")

""""
resultado = int(num1) / int(num2)
print("El resultado de la division es:", resultado)
print("---Fin---")
"""

# Try-except para manejar errores
""""
try:
    resultado = int(num1) / int(num2)
    print("El resultado de la division es:", resultado)

except:
    print("Algo no ha ido como esperaba: ERROR")

print("--- Fin del programa ----")
"""

# Para ver una documentacion con todos los errores tenemos la pag web oficial:
# https://docs.python.org/3/library/exceptions.html

# 

try:
    resultado = int(num1) / int(num2)
    print("El resultado de la division es:", resultado)
except ValueError: # Si uno de los valores no vale para la operacion - el programa recibe n tipo de datos que no es el esperado
    print("Error - quiza uno de los dos no era un numero?")
except ZeroDivisionError: # Division por cero
    print("Error - no se puede dividir por cero")
except Exception as e: # Tratar cualquier otro error
    print("Error - El siguiente error desconocido ha ocurrido", e)

print("--- Fin del programa ----")

# IndexError : Si intentamos acceder a una posicion de la lista o string que no existe:
miString = "012345"
try:
    print(miString[30])
except IndexError:
    print("Error - La posicion no existe.")

# KeyError : si intentamos acceder a una key de diccionario que no existe
miDiccionario = dict(Pedro = 7, Juan = 19)

try:
    print(miDiccionario["Jose"])
except KeyError:
    print("Error - El key para este diccionario no existe")