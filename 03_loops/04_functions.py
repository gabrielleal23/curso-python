## FUNCIONES BLOQUES DE CODIGO REUTILIZAFLE

"""
Definicio de una funcion
def nombre_de_la_funcion(parametro1,parametro2,...):
    #docstring
    #cuerpo de la funcion
    return valor_retorno ## opcional
 
"""

## ejemplo saludar 

def saludar():
    print('Hola')

saludar() ## se invoca la funcion

##ejemplo funcion con parametro

def saludar_a(nombre):
    print(f"Hola {nombre}")

saludar_a("pepe")
saludar_a("juan")

##FUNCIONES CON MAS PARAMETROS

def sumar(a,b):
    suma = a + b
    return suma

result = sumar(2,3)
print(result)

##DOCUMENTAR LAS FUNCIONES CON DOCSTRING

def restar(a,b):
    """Resta 2 numeros y devuelve un resultado"""
    resta = a - b
    return resta

print(restar.__doc__)
help(restar)

##PARAMETROS POR DEFECTO

def multiplicar(a,b = 2): ## marcar el parametro de esta forma puede ser opcional
    return a * b

print(multiplicar(2))

## ARGUMENTOS POR CLAVE

def describir_persona(nombre,edad,sexo):
    print(f"Soy {nombre} tengo {edad} ages y soy del sexo {sexo}")

## LOS PARAMETROS SON POSICIONALES
describir_persona('juna',21,'masculino')

## ARGUMENTOS POR CLVE aqui las posicion no interesa porque se les da un valor de organizacion dependiendo el parametro
describir_persona(sexo="Avion" , nombre= 'JUNA' , edad= 12)

##ARGUMENTOS DE LONGITUD DE VARIABLE
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma =+ numero
    return suma

print(sumar_numeros(4,5,6,3,32,4,6,34))

##ARGUMENTOS DE CLAVE VALOR VARIABLE

def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion(nombre = "mi dudev",edad = 25, red = "insta")
print("\n")
mostrar_informacion(nombre = "mi dudev2",edad = 253, red = "insta",sexo = "avion")

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

def num_1_10 ():
    for n in range(1,11):
        print(n)
num_1_10()

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")

def impares ():
    for n in range(1,21,2):
        print(n)

impares()

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")

def multiplos_cinco ():
     for n in range(5,51,5):
        print(n)

multiplos_cinco()

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")

def inverso (a,b):
    for n in range(a,b,-1):
        print(n)
        
inverso(50,10)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")

def suma_rangos (a,b):
    suma  = 0
    for n in range(a,b):
        suma += n
    print(f"La suma de los valores entre {a} y {b} es de {suma}")

suma_rangos(10,100)

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")

valor_user = int(input("ingrese un numero\n"))

def tabla_multiplicar(a):
    for n in range(1,11):
        print(f"{a} x {n} = {a * n}")

tabla_multiplicar(valor_user)