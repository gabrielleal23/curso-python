print("Parque de Diversiones")

estatura = int(input("Ingrese la estatura del asistente \n"))
total = 0

if estatura >= 120:
    print("Can ride")
    age = int(input("Ingrese la edad del asistente \n"))
    if age < 12:
        total = 5
    elif age >= 12 or age <= 18 :
        total = 7
    else:
        total = 12
    fotos = input("Quieres tomarte fotos\n")
    if fotos == "si":
        total = total + 3
        print(f"El total de la entrada al parque es de ${total}")
    else:
        total = total
        print(f"El total de la entrada al parque es de ${total}")
else:
    print("Cant ride")
