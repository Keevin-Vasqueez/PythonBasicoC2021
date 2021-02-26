#EJERCICIO 1

numero =int(input("Por favor ingrese un número entero positivo para la altura del triangulo: "))
print("El número es {}".format(numero))
for i in range(numero):
    for j in range(i+1):
        print("*", end="")
    print("")   

print("")

#EJERCICIO 2

num =int(input("Por favor ingrese un número entero positivo: "))

if num>1:
    contador=0
    for i in range(2,num):
        resultado=num%i
        if resultado==0:
            contador+=1
    if contador == 0:
        print("El numero {} es un número Primo".format(num))
    else:
        print("El número {} no es un número Primo".format(num))    
else:
    print("El número {} no es un número Primo".format(num))    
