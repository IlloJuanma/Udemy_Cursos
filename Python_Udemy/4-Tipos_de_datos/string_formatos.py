# Formatear una string es introducir datos dentro de ellas

combustible = "Gasolina"
precioPorLitro = 1.3293
duracionPrecio = 5

# combinamos elementos
mensaje = "El precio por litro de %s en los proximos %d dias es de %f €/l" %(combustible, duracionPrecio, precioPorLitro)
print(mensaje)

# Explicaciones:
# - Las strings se formatean con %s
# - Los enteros se formatean con %d
# - Los floats se formatean con %f

# Para limitar el numero de decimales a mostar: %.2f (numero a elegir)
mensajeDePrueba = "Mi float: %.2f" %(precioPorLitro)

# Otra forma: funcion format()
print("-----------------")

mensajeDePrueba= "Mi entero: {0:d}".format(duracionPrecio)
print(mensajeDePrueba)

mensajeDePruebaDos = "Mi float: {0:f}. Mi float con 2 decimales {0:.2f}".format(precioPorLitro)
print(mensajeDePruebaDos)

ultimaPrueba = "Mi numero 1: {} y mi numero 2: {}".format(precioPorLitro, duracionPrecio)
print(ultimaPrueba)