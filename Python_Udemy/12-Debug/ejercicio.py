# Que error tiene este programa??
print("Bienvenido al sistema de almacenamiento de usuarios.")
while(True):
    usuarios = ["Juan","Marta","Miguel","Elisa","Claudia","Jorge","Ana","Pedro"]
    print('''---
    Qué operacion deseas realizar?
    1 - Ver una lista de usuarios
    2 - Añadir un usuario
    3 - Eliminar un usuario
    X - Salir del programa''')

    opcion = input("Introduce la opcion: ")
    print("---")
    if(opcion == "1"):
        print("Lista de usuarios")
        for usuario in usuarios:
            print(usuario)
    elif(opcion == "2"):
        nuevoUsuario = input("Introduce el nombre del nuevo usuario: ")
        usuarios.append(nuevoUsuario)
        print(nuevoUsuario, " añadido")
    elif(opcion == "3"):
        usuarioAeliminar = input("Que usuario quieres eliminar?: ")
        usuarios.remove(usuarioAeliminar)
        print(usuarioAeliminar, " eliminado")
    elif(opcion == "X"):
        break
    else:
        print("Entrada invalida")