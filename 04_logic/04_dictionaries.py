##

persona = {
    "nombre" : "midudev",
    "edad" : 25,
    "es_estudiante":True,
    "calificaciones" :[7,2,9],
    "socials" : {
        "twitter" : "@gabriel",
        "instagram" : "@gabriel",
        "facebook" : "gabriel"
    }
}

## PARA ACCEDER A LOS VALORES DE LOS DICCIONARIOS 
print(persona["nombre"]) 
print(persona["calificaciones"][2]) ## SE ACCEDE A LA PROPIEDAD PARA PODER MOSTRAR CON LA POSICION DE LA LISTA SI POSEE

##CAMBIAR VALORES AL ACCEDER
persona["nombre"] = "pepe"
persona["calificaciones"] [2] = 10
print(persona)

## PARA ELIMINAR UNA PROPIEDAD ES CON EL VALOR DEL
del persona["edad"]
print(persona)

es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")
print(persona)

## SOBREESCRIBIR UN DICCIONARIO CON OTRO DICCIONARIO 
a = {
    "name" : "midudev",
    "age": 25
}
b = {
    "name" :"juan carlos",
    "es_estudiante" : True
}

a.update(b)
print(a)

## comprobar si existe una propiedad
print("name" in persona)

## para obtener todas las claves
print(persona.keys())

## para obtener todos los valores}
print(persona.values())

## 
for key,value in persona.items():
    print(f"{key} : {value}")

    """
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""
def find_first_sum(nums, goal):
    seen = {
        
    }
    for index,value in enumerate(nums):
        missing = goal - value
        if missing in seen : return [seen[missing],index]
        seen[value] = index
        print(f"index: {index} value: {value}")

    return None


nums = [4, 5, 6, 2]
goal = 8
result = find_first_sum(nums,goal)
print(result)

##EJERCIO 2 

