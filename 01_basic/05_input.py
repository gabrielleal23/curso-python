## 05 ENTREADA INPUT 
## LA FUNCIUON INPUT PERMITE OBTERNER DATOS DEL USUARIO A TRAVES DE LA CONSOLA 

print("Hola como te llamas")
nombre =  input()

print(nombre)

print(f"Hola {nombre} encado de conocerte")


nombre = input("Hola como te llamas\n")
print(f"Hola {nombre} encado de conocerte")

age = input("Que edad tienes\n")

print(f"Coming twenty years you have {int(age)+20} years")

print("Para obtener varios valores")
country,city = input("En que pais y ciudad vives ? \n").split(',')

print(f"Vives en {country} ,  {city}")