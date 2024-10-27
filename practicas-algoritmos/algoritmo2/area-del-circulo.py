# 1. Solicitar al usuario que ingrese el radio del circulo que quiere calcular
from math import pi


radio = float(input("Por favor ingrese el radio del circulo: "))

# 2. Calcular el área del circulo utilizando la formula area = 𝜋  * radio^2
area = pi  * (radio*2)

# 3. Mostrar al usuario el área calculada
print("El área del círculo con radio", radio, "es: ", area)