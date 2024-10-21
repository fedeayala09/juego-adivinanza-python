# 1. Solicitar el usuario que ingrese una palabra

palabra_ingresada = input("Por favor, ingrese una palabra: ")

# 2. Contaríamos la cantidad de letras en la palabra ingresada

cantidad_letras = len(palabra_ingresada.replace(" ", ""))

# 3. Mostraremos al usuario la cantidad de letras que tiene la palabra ingresada

print("La palabra ingresada tiene", cantidad_letras, "letras.")
