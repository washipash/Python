import random

def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    victorias = 0
    derrotas = 0
    empates = 0
    
    while True:
        eleccion_usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
        if eleccion_usuario == "salir":
            break
        if eleccion_usuario not in opciones:
            print("Opción inválida. Inténtalo de nuevo.")
            continue
        
        eleccion_computadora = random.choice(opciones)
        print(f"Computadora eligió: {eleccion_computadora}")
        
        if eleccion_usuario == eleccion_computadora:
            print("Empate!")
            empates += 1
        elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
             (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
             (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
            print("¡Ganaste!")
            victorias += 1
        else:
            print("Perdiste!")
            derrotas += 1
    
    print(f"Resultados finales: {victorias} ganadas, {derrotas} perdidas, {empates} empates.")

def adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 5
    
    print("Adivina el número entre 1 y 100. Tienes 5 intentos.")
    for intento in range(intentos):
        try:
            usuario = int(input(f"Intento {intento + 1}: "))
            if usuario < 1 or usuario > 100:
                print("Número fuera de rango. Intenta nuevamente.")
                continue
            
            if usuario == numero_secreto:
                print("¡Felicidades ganaste!")
                return
            elif usuario < numero_secreto:
                print("Demasiado bajo.")
            else:
                print("Demasiado alto.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    print(f"Perdiste. El número era {numero_secreto}.")

# Menú principal
while True:
    print("\nMenú de Juegos:")
    print("1. Piedra, Papel o Tijera")
    print("2. Adivina el Número")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        jugar_piedra_papel_tijera()
    elif opcion == "2":
        adivinar_numero()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Inténtalo de nuevo.")