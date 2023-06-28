# Crear una funcion que nos diga si un numero es par o no
def ComprobarSiEsPar(numero):
    if(numero % 2 == 0):
        return True
    else:
        return False
    
    print("Fin de la ejecucion") # esto nunca se ejecutara pues "return" es como un break
    
miNum = input("Introduce un numero: ")
miNum = int(miNum)
resultado = ComprobarSiEsPar(miNum)
# print("Resultado: ", resultado)

if(resultado):
    print("El numero", miNum," es par, porque ComprobarSiEsPar retorno", resultado)
else:
    print("El numero", miNum," es impar, porque ComprobarSiEsPar retorno", resultado)