# Break y Continue
# Son dos palabras claves (keywords) que nos dan un control sobre los bucles y loops

nombreUsuarios = ["Juan", "Marta", "Miguel", "Elisa", "Claudia", "Jose"]

# Break: Interrumpe el loop y pasa a la siguiente instruccion fuera del loop
# Continue: interrumpe el loop y vuelve al inicio del mismo
for nombre in nombreUsuarios:
    print("Mi usuario es:", nombre)
    if(nombre == "Elisa"):
        continue
    print("Esto se ejecuta en cada loop")
print("Esto se ejecuta fuera del loop")