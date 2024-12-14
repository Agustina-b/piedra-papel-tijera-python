cant_intentos = 0
cant_max_intentos = 3

nombre1 = input("Cómo se quiere llamar el jugador 1? ")
nombre2 = input("Cómo se quiere llamar el jugador 2? ")

while cant_intentos < cant_max_intentos:

    jugador1 = input ("Hola "+ nombre1 + ' Que elegís? piedra, papel o tijera?: ')
    jugador1 = jugador1.lower()
    jugador2 = input ("Hola "+ nombre2 + ' Que elegís? piedra, papel o tijera?: ')
    jugador2 =jugador2.lower()
    cant_intentos += 1

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijera" and jugador2 == "papel"

if jugador1 == jugador2:
        print("¡Ha sido un empate!")
elif (condicion1) or (condicion2) or (condicion3):
        print("Ha ganado:",nombre1)
else:
        print("Ha ganado:",nombre2)

if not cant_intentos < cant_max_intentos:
    print ("Fin del juego")