# Trabajar con ficheros en Python
# open(nombreDelFichero, modoDeApertura)
# r -> Read - Leer
# w -> Write - Escribir
# a -> Append - Añadir
# r+ -> Read+ - Leer y escribir

miArchivo = open("mifichero.txt", "r")

# Leer las lineas de un fichero de texto: funcion readline

lineaLeida = miArchivo.readline()
print(lineaLeida)

# Leo una segunda linea
segundaLinea = miArchivo.readline() # Guarda el cursos por donde iba, no se reinicia
print(segundaLinea)

# Cerrar lector
miArchivo.close()

miArchivo = open("mifichero.txt", "r")
# Leer todo del tiron
for linea in miArchivo:
    print(linea, end="") # end elegimos como acabar la linea
miArchivo.close()

