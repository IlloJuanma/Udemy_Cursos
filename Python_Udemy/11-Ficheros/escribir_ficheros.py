fichero = open("misegundofichero.txt", "a")

miTexto = "\nEstoy haciendo pruebas para escribir en ficheros de texto"

fichero.write(miTexto)
fichero.close()

# Lo mas importante
# Si abrimos el fichero con el modo "w" vamos a sobreescribir todos los datos que hubieses
# Si abrimos con el modo "a" vamos a añadir al final del archivo sin eliminar antes
# Si la ruta del archivo no existe, se crear un archivo nuevo