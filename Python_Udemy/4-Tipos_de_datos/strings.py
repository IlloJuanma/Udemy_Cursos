# Las variables de tipo String interpretan su contenido como texto
miString = 'Me llamo Juanma'
miSegundaString = "Me llamo Juanma"
print(miString)

# Imprimir mas de una linea dentro de un string tenemos el "retorno de carro" \n
miTerceraString = "Me\nllamo\nJuanma"
print(miTerceraString)

# Creacion de variable numero pero con forma de string: Tendremos un string y no un numero
miNumero = "30"
# Intentar sumar 1 a nuestro numero
miNumero += 1
print(miNumero)