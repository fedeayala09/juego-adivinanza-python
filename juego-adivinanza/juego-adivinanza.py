import random


numero_random = random.randint(0, 10)
print(numero_random)
cant_intentos = 5
adivinado = False

print(">>>>> Bienvenido al juego de adivinar el numero secreto <<<<<<<")

numero_seleccionado = int(input("ingrese un numero del 0 al 10: "))

while not adivinado and cant_intentos != 0:
    if numero_random != numero_seleccionado:
        print("Numero equivocado, intentelo denuevo.")
        cant_intentos -= 1
        numero_seleccionado = int(input("ingrese un numero del 0 al 10: "))
    elif numero_random == numero_seleccionado:
        print("Numero CORRECTO. Usted gana!!!")
        adivinado = True

print("juego finalizado")
    