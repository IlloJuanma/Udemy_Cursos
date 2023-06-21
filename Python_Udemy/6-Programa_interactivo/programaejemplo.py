miNombre = input("Introduce tu nombre: ")
miEdad = input("Introduce tu edad: ")
print("Hola, me llamo",miNombre, "y tengo", miEdad, "años.")

# La funcion input es la nueva en esta clase. Como podemos intuir, la funcion input espera la entrada
# del usuario en la consola. Una vez el usuario introduce algo y pulsa "enter", lo que ha introducido
# el usuario se almacena en nuestra variable. En el caso anterio, hemos llamado a la funcion dos veces,
# una para el nombre y otra para la edad.
# Importante, la entrada de input() siempre es una string :  no nos servirá, en caso de ser un número,
# para realizar la operacion. Si esto es lo que queremos, tendremos que hacer un cast a entero o float.

print("El año que viene tendrás:",int(miEdad) + 1, "años")