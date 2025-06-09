## SECUENENCIA MUTABLE DE ELEMENTOS

# CREACION DE LISTAS


import os

os.system("clear")

print("\nCrear una lista")
lista1 = [1,2,3,4,5,6]
lista2 = ["manzanas","peras","bananos"]
lista3 = [1,"hola",True,3.14]

lista_vacia = []
lista_de_listas = [[1,2],[3,4]]
matrix = [[1,2],[2,3],[4,5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

print("\nAcceso por indice")
print(lista2[0])
print(lista2[1])
print(lista2[-1])

print(lista_de_listas[1][0]) ##ACCEDER DENTRO DE UNA LISTA 


##CAMBIO DE ELEMENTOS 
##SLICING DE LISTAS
print(lista1[1:4])## EL INCIDE UNO QUE ES EL PRIMER VALOR HASTA EL INDICE 4 DE LA LISTA PERO NO INCORPORA EL ULTIMO VALOR 
print(lista1[:3]) ## que me de los primeros 3 valores
print(lista1[3:]) ## que me retorne los 2 ultimos valores
print(lista1[:]) ## para hacer copia de una lista


##MAS MAGIA 
#print(lista1[desde:hasta:paso])
lista1 = [1,2,3,4,5,6,7,8,9]
lista_copy = lista1[::2]## la copia de la lista que me la de saltando de 3 en 3 cada elemento
print(lista1[::-1])## para que me de la lista invertida

##MODIFICAR UNA LISTA
lista1[0] = 20 ## ASIGNARLE UN NUEVO VALOR A UN ELEMENTO DE LA LISTA DEBE EXISTIR LA POSICION
print(lista1)

##ADD ELEMENTS IN LIST THE LARGE FORM
lista1 = [1,3,5]
lista1 = lista1 + [4,5,6]
print(lista1)

## FORMA CORTA MAS EFICIENTE
lista1 += [7,8,9,3]
print(lista1)

##RECUPERAR LONGITUD DE UNA LISTA
print(len(lista1))

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
mensaje_nuevo = mensaje[7:]
print(mensaje_nuevo)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
numeros[0],numeros[-1] = numeros[-1] , numeros[0]
print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
sandwich = []
sandwich = pan + ingredientes + pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista += lista
print(lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
numeros = [7, 3, 5, 1, 9]
centro = len(numeros)//2
print(numeros[centro])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
lista = [1, 2, 3, 4, 5, 6]
centro = len(lista)//2
lista_invertidad = lista[:centro][::-1]+lista[centro:]
print(lista_invertidad)