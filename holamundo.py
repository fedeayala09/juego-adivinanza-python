"""
texto = "Hola mundo!"

#El índice justamente indica el lugar o posición donde está un elemento en una estructura o grupo
print(texto[1])
print(len(texto))

#Las busquedas y la mayoria de los metodos son case sesitive
print("mundo" in texto)
print("casa" not in texto)

#Slicing ponemos desde un indice hasta un indice NO incluido
txt = "Seguimos trabajando con Strings"
print(txt[9:19])


txt2 = "   ESTE es Un TEXTO de todo TiPo_$     "
minuscula = txt2.lower()
mayuscula = txt2.upper()
txtCorregido = txt.strip()
"""

horas = 10
clases = 60
text = "El contenido de este curso va a durar: {1} horas y tendra {0} clases"

print(text.format(clases, horas))

#con la barra \ invertida podremos hacer un "escape de caracteres"
txt = "La mejor serie es \"Dragon Ball\""
print(txt)

#OPERADORES DE ASIGNACION

# =
# +=
# -=
# *=
# /=
# //=
# **=
