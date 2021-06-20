#Ingrese un numero y diga si es par e impar
"""dotstring
1. pedir al usuario ingresar un numero
2. hacer el calculo para ver si es par o impar (variable % 2 == 0 es par
3. mostrar el mensaje
"""
numero = int(input("Ingrese el numero: \t"))

if(numero == 0): # si el numero es igual a cero
    print("Es cero")
elif(numero % 2 == 0): # caso contrario si el numero mod 2 es cero
    print("El numero es par")
else: # caso contrario
    print("El numero es impar")