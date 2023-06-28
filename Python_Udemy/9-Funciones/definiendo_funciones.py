# Sintaxis para definir una funcion
# def nombreDeMiFuncion(parametro 1, parametro 2...):
#   codigo a ejecutar por la funcion
#   return valorDeRetorno

def CalcularValorAlCuadrado(numero):
    numCuadrado = numero * numero
    return numCuadrado

def ImprimirPalomitas():
    print("PALOMITAS")

print("Hola amigos inicio del programa: ")
miNumero = input("Introduce un numero: ")
miNumero = int(miNumero)

miNumeroAlCuadrado = CalcularValorAlCuadrado(miNumero)
print("Mi numero al cuadrado es:",miNumeroAlCuadrado)

ImprimirPalomitas()