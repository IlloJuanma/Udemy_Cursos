# Objetivo: generar la serie de Fibonacci, imprimiendo el numero de elementos
# que el usuario quiera
# Serie de Fiboncci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55... El siguiente es
# la suma de los anteriores
# Cosas que cumplir:
# - Pedir al usuario que introduzca un numero de elementos
# - Si el usuario introduce cualquier cosa que no es convertible a int, volver a
# pedirle que introduzca un numero
# - Imprimir los X primeros terminos de la serie, siendo X el numero introducido por el usuario
# - El numero de elementos tiene que ser mayor a 1.

# Pedir al usuario el numero de elementos hasta que sea correcto
while(True):
    numeroElementos = input("Introduce el numero de elementos (min. 2):")
    try:
        numeroElementos = int(numeroElementos)
        if(numeroElementos >= 2):
            break
        else:
            print("El numero de elementos tiene que ser mayor o igual que 2")
            continue # vuelve al inicio del bucle  
    except:
        print("Entrada no valida, por favor introduce un numero")

print("Los primeros", numeroElementos, "de la serie de Fibonacci son:")
num1=0
num2=1
# Crear un contador para nuestro loop:
contador = 0
while (contador < numeroElementos):
    print(num1)
    # Calcular el siguiente numero
    numSiguiente = num1 + num2
    # Actualizar los valores para la siguiente vuelta
    num1 = num2
    num2 = numSiguiente
    contador += 1
print("--- Fin de la serie ---")