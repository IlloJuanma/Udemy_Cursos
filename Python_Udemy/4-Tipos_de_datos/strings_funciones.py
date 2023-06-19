miString = "Hola me llamo Juanma"
print("Mi string inicial:",miString)

# Poner una frase en mayuscula
miStringMayus = miString.upper()
print(miStringMayus)

# Poner una frase en minusculas
print("String minus:", miString.lower()) # esto no modifica el string original

# Funcion replace - reemplaza caracteres de nuestro string
print("Reemplazamos las o por las i: ", miString.replace("o", "i")) # no modifica string original

# Reemplazar palabras enteras
print("Reemplazamos Juanma por Pedro:",miString.replace("Juanma", "Pedro"))

# Reemplazar la primera o por i
print("Reemplazamos la primera o por las i: ", miString.replace("o", "i",1))

# Pasar una frase de una linea a multiples lineas
print("Pasar a multiples lineas: ",miString.replace(" ","\n"))