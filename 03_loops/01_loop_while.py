## 01 BUCLES (WHILE)
## PERMITIR REALIZAR ACCIONES MIENTRAS UNA CONDICION SE VAYA CUMPLIENDO 

import os

print("\n Bucle while")

contador = 0

while contador <= 5:
    print(contador)
    contador += 1 ##PARA EVITAR BUCLES INFINITOS

## break para romper el bucle
contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break ## para romper el bucle

##SALTARSE LA ITERACION PARA ROMPER EL BUCLE
print("\n Bucle con continue")

contador = 0
while contador <10:
    contador +=1
    if contador %2 == 0 :
        continue

    print(contador)


### ELSE  EN BUCLES 

print("\n Bucle while con else")

contador = 0

while contador < 5:
    print(contador)
    contador +=1
else:
    print("El bucle ha terminado")

contador = 0

while contador < 5:
    print(contador)
    contador += 1
    break ##SI PONGO EL BREAKE EL ELSE NO VA SERVIR
else:
    print("El bucle a terminado")

## PEDIR AL USUARIO QUE DEBE SER POSITIVO

# numero = -1
# while numero <= 0:
#     numero = int(input("Escribe un numero positivo\n"))
#     if numero < 0:
#         print("El numero debe ser positivio")

# print(f"El numero que haz introduciodo es {numero}")



##try except dalrle un limitante si no comenzara a fallar
# numero = -1
# while numero <= 0:
#     try:
#         numero = int(input("Escribe un numero positivo\n"))
#         if numero < 0:
#             print("El numero debe ser positivio")
#     except:
#         print("El numero debe ser un numero sino no es valido")
    
# print(f"El numero que haz introduciodo es {numero}")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
contador = 10
while contador >= 1:
    print(contador)
    contador -=1
   


# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
numero =1 
suma = 0 
while numero <=20:
    if numero % 2 == 0:
        suma += numero
    numero += 1

print(f"La suma de numeros pares es {suma}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

valor = int(input('Introduzca un numero entero positivo'))
factorial = 1
contador = 1

while contador <= valor:
    factorial *= contador
    contador += 1

print(f"El factorial del numero {valor} es {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
password = ""
caracteres = 8
contador = 0

while len(password) < 8:
    password = input("Ingrese una contrasena de 8 caracteres \n")
    if len(password)< 8 :
        input("La contrasena debe tener como minimo 8 caracteres\n")

print('Contrasena Valida')

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
contador = 1

numero = int(input("Ingrese un numero entero"))
while contador < 10:
    resultado = contador * numero
    print(f"{numero} x {contador} = {resultado}")
    contador +=1


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1
  if es_primo:
    print(numero)

  numero += 1