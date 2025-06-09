##METODOS DE LAS LISTAS

import os 
os.system('clear')

lista1 = [1,2,3,4,5]

lista1.append(6) ## es para añadir un elemento al final de la lista
print(lista1)

lista1.insert(1,5) ## SE INSERTAA UN ELEMENTO EN EL INDICE O POSICION UNO (INDICE,VALOR)
print(lista1)

lista1.extend([7,9,41,40,5,11]) ##AÑADIR VARIOS ELEMENTOS AL FINAL DE LA LISTA
print(lista1)

###ELIMINAR ELEMENTOS DE LA LISTA
lista1.remove(5)##ELIMINA EL PRIMER ELEMENTO DE LA LISTA QUE APAREZCA CON ESE PARAMETRO
print(lista1)

lista1.pop(-1) ## ELIMINA POR INDICE O POSICION MODIFICANDO LA LISTA SE LE PUEDE PASAR CUALQUIER INDICE
print(lista1)
 
lista1.pop(1) ## ELIMINA EL SEGUNDO ELEMENTO DE LA LISTA ES POR INDICE
print(lista1)

del lista1[-1]##ELIMINAR SIN MEDIDA 
print(lista1)

lista1.clear()##ELIMINA TODOS LOS ELEMENTOS DE LA LISTA
print(lista1)

lista1 = ["panda","koala", "hamster","perro","gato"] ##METODOS POR RANGO
del lista1[2:4]
print(lista1)


###MAS METODOS UTILES
print("Ordenar Listas modificando la original")
numbes = [3,4,6,8,5]
numbes.sort() ## para ordenar en orden
print(numbes)

print("Ordenar listas creando una nueva lista")
numbes = [3,4,6,2,5,77,33]
sorted_numbers = sorted(numbes) 
print(sorted_numbers)

print("Ordenar una lista cadena de texto en minusculas")
frutas = ['manzanas','peras','pepinos','limon']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista cadena de texto en minusculas y mayusculas")
frutas = ['Manzanas','peras','Pepinos','limon']
frutas.sort(key=str.lower) ##COMPARACION DE TEXTOS EN MINUSCULAS Y LA ORDENA
print(frutas)

##MAS METODOS
frutas = ['Manzanas','peras','Pepinos','limon','Manzanas']
print(len(frutas)) ##TAMAÑO DE LA LISTA
print(frutas.count("Manzanas")) ## VECES QUE APARECE EL ELEMENTO
print("ManzanaSs" in frutas) ### VERIFICAR SI ESTA EL ELEMENTOS CON TRUE O FALSE

