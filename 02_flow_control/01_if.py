## SENTENCIAS CONDICIONALES IF ELIF ELSE 

import os

os.system("clear")

print("Sentencia simple condicionla")

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else :
    print("Eres menor de edad")


nota = 7

if nota >= 9 :
    print('Sobresaliente')
elif nota >= 7:
    print('notable')
elif nota >=6 :
    print('Aprobado')
else:
    print('No haz aprobado')

print("\n Condiciones Multiples")

edad=18
tiene_carnet = False

if edad >= 18 and tiene_carnet:
    print("Puedes Conducir")
else:
    print("La Poliziaaaaaaa")

## Un pueblo de isla margarita
if edad >= 19 or tiene_carnet:
    print("puede conducir en la isla")
else:
    print("Paga el policia y te deja conducir")
    

es_finde_semana = False

if not es_finde_semana:
    print("A trabajar")

print("\n Anidar condicionales")

edad = 17
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print('No puedes ir a la discoteca')


if edad < 18:
    print("No puedes entrar a la disco")
elif tiene_dinero:
    print("Puedes ir a la discoteca")
else:
    print("A dormir pa")

print("\n La condicion ternaria:")
## FORMA DE UN IF ELSE EN UNA LINEA DE CODIGO 
## 1.  CODIGO SI CUMPLE LA CONDICION 
## 2 . CONDICION IF Y LUEGO EL ELSE SINO CUMPLE

edad = 17
mensaje = "Es mayor de edad" if edad>= 18 else "Es menor de edad"
print(mensaje)