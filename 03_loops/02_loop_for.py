### BUCLES FOR
### PERMITE EJECUTAR UN BLOQUE DE CODIGO

print("\n Bucle for")

##iterr una lista 

frutas = ["manzanas","pera","mandarina"]

for fruta in frutas:
    print(fruta)


## iterar sobre cualquier cosa

cadena = "midudev"

for caracter in cadena:
    print(caracter)

## RECUPERAR EL INDICE
##enumarate()
frutas = ["manzanas","pera","mandarina"]

for index, fruta in enumerate(frutas): ## primer valor es el indice y segundo es el valor
    print(f"El indice es {index} y la fruta es {fruta}")

## BUCLES ANIDADOS 
letras = ["a","b","c"]
numeros = [1,2,3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

##BREAKE aninales

animales = ["perro","gato","raton","loro","canario"]
for idx , animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"El loro esta escondido en el indice {idx}")
        break

##continue

print("\nContinue")
animales = ["perro","gato","raton","loro","canario"]

for idx, animal in enumerate(animales):
    if animal == "loro":
        continue

    print(animal)


## COMPRENSION DE LISTAS (LIST COMPREHENSION)

animales = ["perro","gato","raton","loro","canario"]
animales_mayusculas = [animal.upper() for animal in animales]
print(animales_mayusculas)

### MUESTRA LOS NUMEROS PARES DE UNA LISTA

pares = [num for num in [1,2,3,4,5,6,7,8,9,10] if num % 2 == 0]
print(pares)

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
numeros = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)

print(pares) 

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
suma = 0
contador = 0
for n in numeros :
    suma += n
    contador += 1
    media = suma//contador
print(f"La media de la lista numeros es {media}")
    

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numeros = [15, 5, 25, 10, 20]
alto = numeros[0]
for n in numeros:
    if n > alto:
        alto = n
print(f"El numero mas alto de la lista es {alto}")



# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabras_5 = [letras for letras in palabras if len(letras) >= 5]
print(palabras_5)



# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduzca una letra\n").lower()
contador = 0
primeros = []

for p in palabras:
    if p.lower().startswith(letra):
        contador +=1
print(contador)
