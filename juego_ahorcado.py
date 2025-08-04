import random

def obtener_palabra_secreta() -> str:
    palabras = ['python','javascript','java','flask','react','angular','tensorflow','django','typescript','github']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta,letras_adivinadas):
    adivinado = ''
    
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += '_'
    return adivinado

def juego_ahorcado():
    reintentar = True
    while reintentar:
        
        palabra_secreta = obtener_palabra_secreta()
        letras_adivinadas = []
        intentos = 7
        juego_terminado = False
        
        print('Bienvenido al juego del ahorcado')
        print(f'Tienes {intentos} intentos para adivinar la palabra')
        print(mostrar_progreso(palabra_secreta,letras_adivinadas), "La cantidad de letras de la palabra es: ", len(palabra_secreta))
        
        while not juego_terminado and intentos > 0:
            adivinanza = input('Introduce una letra: ').lower()
            if len(adivinanza) != 1 or not adivinanza.isalpha():
                print('Por favor introduce una letra valida (sólo escribir una letra)')
            elif adivinanza in letras_adivinadas:
                print('Ya usaste esta letra, prueba con otra')
            else:
                letras_adivinadas.append(adivinanza)
                if adivinanza in palabra_secreta:
                    print(f'¡Muy bien has adivinado una letra!, "{adivinanza}" esta en la palabra secreta')
                else:
                    intentos -= 1
                    print(f'¡Lo siento mucho!, la letra "{adivinanza}" no esta en la palabra secreta')
                    print(f'Te quedan {intentos} intentos')
            progreso_actual = mostrar_progreso(palabra_secreta,letras_adivinadas)
            print(progreso_actual)
            
            if '_' not in progreso_actual:
                juego_terminado = True
                palabra_secreta = palabra_secreta.capitalize()
                print(f'¡Felicidades! has adivinado la palabra, que es: "{palabra_secreta}"')
        if intentos == 0:
            palabra_secreta = palabra_secreta.capitalize()
            print(f'Lo siento se te acabaron los intentos, la palabra secreta era: "{palabra_secreta}"')
        reintentar = volver_a_jugar()

def volver_a_jugar():
    while True:
        opcion = input('¿Deseas volver a jugar?\n1 Si\n2 No\nOpcion: ')
        if opcion == '1':
            return True
        elif opcion == '2':
            print('Fin del juego')
            return False
        else:
            print('Opcion Invalida, escribe 1 o 2')
juego_ahorcado()
