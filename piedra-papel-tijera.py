nombre1 = input("¿Cómo se llamará el jugador 1? \n-")
nombre2 = input("¿Cómo se llamará el jugador 2? \n-")

j1 = input("¡Hola jugador 1! ¿Qué eliges? ¿Pedra, papel o tijeras? \n-")
j2 = input("¡Hola jugador 2! ¿Qué eliges? ¿Pedra, papel o tijeras? \n-")

if j1 == j2:
    print("¡Ha sido un empate!")
elif (j1 == "piedra" and j2 == "tijera") or (j1 == "papel" and j2 == "piedra") or (j1 == "tijeras" and j2 == "papel"):
    print(f"¡El jugador {nombre1} ha ganado!")
else:
    print(f"¡El jugador {nombre2} ha ganado!")