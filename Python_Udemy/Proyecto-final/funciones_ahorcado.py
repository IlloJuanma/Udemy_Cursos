import random
def ElegirDificultad():
    vidasRestantes = 0
    while(True):
        dificultad = input("Introduzca su dificultad: F(Fácil), M(Medio), D(Difícil): ")
        if(dificultad.casefold() == "f"):
            print("Jugando en dificultad fácil")
            vidasRestantes = 9
            break
        elif(dificultad.casefold() == "m"):
            print("Jugando en dificultad media")
            vidasRestantes = 6
            break
        elif(dificultad.casefold() == "d"):
            print("Jugando en dificultad difícil")
            vidasRestantes = 3
            break
        else:
            print("Entrada invalida. Por favor, seleccione entre F,M,D")
    
    return vidasRestantes

def ConvertirPalabraEnHuecos(palabra, letrasAcertadas):
    palabraConvertida = ""
    for letra in palabra:
        if(letra in letrasAcertadas):
            palabraConvertida += letra + " "
        else:
            palabraConvertida +="_ "

    return palabraConvertida

def PalabraCompleta(palabra, letrasAcertadas):
    for letra in palabra:
            if(letra in letrasAcertadas):
                continue
            else:
                return False              
    return True

def EvaluarSeguirJugando():
    jugarOtraVez = input("¿Quieres jugar otra partida? S/N: ")

    seguirJugando = False
    while(True):
        if(jugarOtraVez.casefold() == "s"):
            seguirJugando = True
            break
        elif(jugarOtraVez.casefold() == "n"):
            seguirJugando = False
            break
        else:
            print("Entrada invalida. Por favor, introduce S/N")

    return seguirJugando

def PalabraAleatoria():
    ficheroPalabras = open("mispalabras.txt", "r")

    listaPalabras = []

    for linea in ficheroPalabras:
        linea = linea.replace('\n', '') # Sustituir el ultimo \n por nada, sino es una "letra" mas
        listaPalabras.append(linea)

    ficheroPalabras.close()

    posicionDeLaLista = random.randint(0, len(listaPalabras) - 1)

    return listaPalabras[posicionDeLaLista]