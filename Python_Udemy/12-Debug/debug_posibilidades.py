miVaribale = "patata"

miVaribale = input("Modifica tu variable: ")

if(miVaribale == "patata"):
    print("Tengo una PATATA")
else:
    print("No tengo una patata :(")

miLista = ["a", "b", "c", "d", "e"]

print(miLista)

for elemento in miLista:
    print(elemento)
    elemento = "a"
    print(elemento)

print(miLista)