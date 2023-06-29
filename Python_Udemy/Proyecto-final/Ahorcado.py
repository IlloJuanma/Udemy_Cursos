# Requisitos
# El usuario escoge el nivel de dificulta. F: 9 vidas, M: 6 vidas, D: 3vidas
# Las palabras se lean desde un archivo de texto
# La palabra elegida por el programa tiene que mostrarse en forma de huecos "_ _ _"
# El usuario siempre sabe cuantas vidas le quedan
# El usuario siempre sabe que letras ha fallado y acertado
# El usuario siempre sabe si ha introducido una letra repetida
# Si el usuario acierta todas las letras, gana
# Si el usuario pierde todas las vidas, pierde la partida
# Tras ganar o perder, se ofrece al usuario si quiere jugar otra partida o salir


# Importar modulo de funciones
import funciones_ahorcado as fa

# El programa elige una palabra aleatoria
palabra = fa.PalabraAleatoria()

# Pedir al usuario la dificultad en la que quiere jugar
vidasRestantes = fa.ElegirDificultad()

# Lista de letras usadas   
letrasAcertadas = []
letrasFalladas = []

seguirJugando = True
while(seguirJugando):

    # Mostrar la palabra con huecos al usuario
    palabraConvertida = fa.ConvertirPalabraEnHuecos(palabra, letrasAcertadas)
    print("----------")
    print("Palabra a adivinar:", palabraConvertida)
    print("Vidas restantes:", vidasRestantes)
    print("Letras falladas:", letrasFalladas)
    print("----------")

    # Esperamos a que el usuario introduzca una letra
    letraIntroducida = input("Introduce una letra: ")

    # --- Opcion 1: la letra ya esta usada
    if(letraIntroducida in letrasAcertadas or letraIntroducida in letrasFalladas):
        # ----- Notificar al usuario que la letra ya ha sido usada, no restar vidas y volver a pedir letra
        print("----------")
        print("Esta letra ya ha sido utilizada, por favor, elige otra letra")
        continue

    # --- Opcion 2: la letra no ha sido usada
    else:
        # ----- Comprobar si la letra está o no en nuestra palabra
        if(letraIntroducida in palabra):
            # -------- Opcion 1: la letra está en la palabra: Acierto -> Rellenar huecos de la palabra, volver al inicio
            print("----------")
            print("La letra", letraIntroducida, "está en la palabra")
            letrasAcertadas.append(letraIntroducida)
        else:
            # -------- Opcion 2: La letra no está en la palabra: Error -> Quitar una vida, añadir a la lista de letras falladas
            print("----------")
            print("La letra", letraIntroducida, "no está en la palabra")
            vidasRestantes -= 1
            letrasFalladas.append(letraIntroducida)
    # Comprobar si el usuario ha perdido todas las vidas:
    if(vidasRestantes == 0):
        # --- Si no tiene vidas, finalizar el juego y pedir al usuario que nos diga si quiere jugar otra vez o no
        print("----------")
        print("Has perdido todas las vidas. La palabra era:", palabra)
        seguirJugando = fa.EvaluarSeguirJugando()

    # --- Si aun tiene vidas, seguir jugando
    else:
        # Comprobar si la palabra esta completa:
        palabraCompleta = fa.PalabraCompleta(palabra, letrasAcertadas)
        
        if(palabraCompleta == True):
            # --- Si la palabra si está completa, el usuario no ha ganado y preguntar si quiere jugar otra partida    
            print("----------")
            print("Todas las letras han sido acertadas, ¡Has ganado!. La palabra era", palabra)
            seguirJugando = fa.EvaluarSeguirJugando()
    
    if(vidasRestantes == 0 and seguirJugando) or fa.PalabraCompleta(palabra, letrasAcertadas) and seguirJugando):
        letrasFalladas = []
        letrasAcertadas = []
        vidasRestantes = fa.ElegirDificultad()
        palabra = fa.PalabraAleatoria()


print("----------")
print("¡Gracias por jugar! Hasta la próxima!")
print("----------")