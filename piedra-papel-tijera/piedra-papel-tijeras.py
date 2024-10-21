print("Bienvenido al Piedra, Papel y Tijeras!!!")

selec_usuario1 = str(input("Elija la opcion Usuario 1: ")).capitalize()
selec_usuario2 = str(input("Elija la opcion Usuario 2: ")).capitalize()

if selec_usuario1 == selec_usuario2:
    print("Es un empate")
elif (selec_usuario1 == "Piedra" and selec_usuario2 == "Tijeras") or (selec_usuario1 == "Papel" and selec_usuario2 == "Piedra") or (selec_usuario1 == "Tijeras" and selec_usuario2 == "Papel"):
    print("Gana Usuario 1")
elif (selec_usuario2 == "Piedra" and selec_usuario1 == "Tijeras") or (selec_usuario2 == "Papel" and selec_usuario1 == "Piedra") or (selec_usuario2 == "Tijeras" and selec_usuario1 == "Papel"):
    print("Ha ganado el Usuario 2")