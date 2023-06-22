# La funcion range() genera una lista de numeros con los siguientes parametros:
# range(start, end, step) -> Start: numero desde el que se iniciar
#                            End: numero maximo
#                            Step: "salto" entre un numero y otro

miRange = range(1,10,1)
for numero in miRange:
    print(numero)

# Solo 1 parametro: estamos pasando el parametro final (end)
for num in range(10):
    print(num)

# Con 2 parametros: de start a end
print("----2 parametros----")
for num in range(10,50):
    print(num)

# Con 3 parametros: start, end y step
print("----3 parametros----")
for num in range(0,100,20):
    print(num)