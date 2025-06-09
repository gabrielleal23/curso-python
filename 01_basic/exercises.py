###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("Mi nombre es Gabriel\nMi apellido es Leal")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print("El tipo de dato de la variable a es :",type(a))
print("El tipo de dato de la variable b es :",type(b))
print("El tipo de dato de la variable c es :",type(c))
print("El tipo de dato de la variable d es :",type(d))
print("El tipo de dato de la variable e es :",type(e))

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
a = "12345"
print(type(str("12345")))
print(int(12345))

print(type(int(12345)))
print(float(12345))

print(type(float(3.99)))
print(int(3.99))

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
nombre = input('Escribe tu nombre \n')
edad = int(input('Escribe tu edad \n'))
altura = float(input('Escribe tu altura \n'))

print(f"Hello! my names is {nombre} , i am {edad} years old, and my stature is {altura} cm  ")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

valor = int(round(3.1416)/2)
print(valor)