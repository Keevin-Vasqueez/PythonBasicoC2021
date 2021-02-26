#Ejercicio 1

contraseña =str(input("Por favor ingrese una contraseña: "))

contraseña1 =str(input("Por favor ingrese nuevamente su contraseña: "))

if contraseña!=contraseña1:
    print("contraseña incorrecta")
else:
    print("Contraseña aceptada")


#Ejercicio 2

genero =str(input("Por favor ingrese su genero hombre o mujer: "))

nombre =str(input("Por favor ingrese su nombre: "))

if genero == "mujer":
    if nombre.lower() < "m":
        print("Usted pertenece al grupo A")
    else:
        print("Usted pertenece al grupo B")
else:
    if nombre.lower() > "n":
       print("Usted pertenece al grupo A")
    else:
        print("Usted pertenece al grupo B")
