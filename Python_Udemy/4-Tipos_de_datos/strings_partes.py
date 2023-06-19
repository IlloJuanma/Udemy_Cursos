# Un parrafo es un conjunto de frases
# una frase es un grupo de palabras y signos de puntuacion
# una palabra es un grupo de letras

miFrase = "Hola amigos, ¿como estáis?"
print(miFrase)
# Imprimir la pimera letra:
print(miFrase[0])
# Imprimir un rango de letras
print(miFrase[2:7])
# Imprimir el inicio hasta la posicion 11
print(miFrase[:11])
# Imprimir desde una posicion hasta el final del string
print(miFrase[11:])
# Imprimir una frase dos veces
print(miFrase * 2)
# Unir dos strings
miContestacion = "Muy bien, gracias"
miConversacion = miFrase + "\n" + miContestacion
print(miConversacion)