# Objetivo: dividir las diferentes operaciones en funciones.
# Además, añadir:
# Una comprobacion que nos diga si el numero es par o impar
# Una comprobacion que nos diga si el numero es primo o no

miNumero = input("Hey! Introduce tu numero para que calcule cositas: ")
miNumero = int(miNumero)

def Cuadrado(miNumero):
    cuadrado = miNumero ** 2
    return cuadrado

def Cubo(miNumero):
    return (miNumero ** 3)

def Valor100(miNumero):
    return (miNumero * 100)

def ComprobarSiEsPar(miNumero):
    return (miNumero % 2 == 0)

def ComprobarSiEsPrimo(miNumero):
    # Crear un loop que compruebe todas las divisiones desde 2 hasta el numero
    for divisor in range(2,miNumero):
        # Compruebo si el resultado de mi numero entre el divisor es 0 o no
        if(miNumero % divisor == 0):
            # No es primo
            return False
    
    return True # Fuera del loop

def Calcular5Multiplos(miNumero):
    # Creamos lista vacia de multiplos
    multiplos = []
    for multiplicador in range (1,6): # Desde 0 al 5
        # Calculamos resultado
        miMultiplo = miNumero * multiplicador
        # Guardamos en la lista de multiplos
        multiplos.append(miMultiplo)
    return multiplos
  
print("Sus 5 primeros multiplos: ", Calcular5Multiplos(miNumero))
print("Su cuadrado y su cubo: ", Cuadrado(miNumero), Cubo(miNumero))
print("Su valor por 100: ", Valor100(miNumero))
print("Es par o impar?", ComprobarSiEsPar(miNumero))
print("Es primo o no?", ComprobarSiEsPrimo(miNumero))