## PERMITE CREAR UNA SECUENCIA PARA UN RANGO DE NUMEROS 

print("\nrange():")

nums = range(10)

##GENERA UN SECUENCIA DE NUMEROS DEL 0 AL 10
for num in nums:
    print(num)

## RANGE(INICIO,FIN)

for num in range(5,10):
    print(num)

##range(inicio,fin,paso)
for num in range(0,10,5):
    print(num)

## numeros negativos en rango 
for num in range(-5,10):
    print(num)

for num in range(10,0-1):
    print(num)

## CREAR UNA lista en range

num = range(10)
list_of_nums = list(nums)
print(list_of_nums)

## SERIA PARA HACER 5 VCECES UNA ACCION 

contador = 0

while contador < 5:
    print('Hacer 5 veces una accion')
    contador += 1

## en range hacer una accion 5 veces

for _ in range(5):
    print("hacer 5 veces una cosa con range")


    ###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

for n in range(1,11):
    print(n)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
for n in range(1,21,2):
    print(n)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")

for n in range(5,51,5):
    print(n)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")

for n in range(10,0,-1):
    print(n)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
suma = 0
for n in range (1,101):
    suma += n
print(suma)





# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
numero = int(input("ingrese un numero\n"))

for n in range(1,11):
   print(f" {numero} x {n} = {numero * n}")