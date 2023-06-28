# Para trabajar con archivos binarios, simplemente utilizamos los modos "rb" (read binary)
# o "wb" (write binary)

# Pasos para copiar una imagen
# 1 - Abrir el archivo original en modo lectura
# 2 - Crear un nuevo archivo (abrir un archivo que no existe en modo wb)
# 3 - Copiar la informacion
# 4 - Cerrar ficheros

imagen = open("lahabana.jpg", "rb")
imagenCopia = open("habanacopia.jpg", "wb")
informacion = imagen.read()
imagenCopia.write(informacion)

imagenCopia.close()
imagen.close()