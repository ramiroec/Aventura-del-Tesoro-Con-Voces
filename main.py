import os
import time
from gtts import gTTS
import pygame

def reproducir_audio(texto, nombre_archivo="temp.mp3"):
    """Convierte el texto a audio, lo guarda temporalmente y lo reproduce usando pygame."""
    try:
        # Convertir el texto a audio usando gTTS y guardar en un archivo temporal
        tts = gTTS(text=texto, lang='es')
        tts.save(nombre_archivo)

        # Inicializar el mixer de pygame
        pygame.mixer.init()

        # Cargar y reproducir el archivo de audio
        pygame.mixer.music.load(nombre_archivo)
        pygame.mixer.music.play()

        # Esperar hasta que termine la reproducción
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        # Detener el mixer y limpiar
        pygame.mixer.music.stop()
        pygame.mixer.quit()

    except Exception as e:
        print(f"Error al reproducir el audio: {e}")
    finally:
        # Eliminar el archivo temporal
        if os.path.exists(nombre_archivo):
            os.remove(nombre_archivo)

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def juego_de_trivia():
    # Definir las preguntas, opciones y respuestas
    preguntas = [
        {
            "pregunta": "El significado del parámetro de palabra clave es determinado por:",
            "opciones": ["a) El orden en el que se pasan los argumentos", "b) El nombre especificado del argumento junto con su valor", "c) El tipo de dato del argumento"],
            "respuesta": "b"
        },
        {
            "pregunta": "La función print() puede dar como salida.",
            "opciones": ["a) Cualquier número de argumentos (incluyendo cero)", "b) Un solo argumento", "c) Ningún argumento"],
            "respuesta": "a"
        },
        {
            "pregunta": "¿La \\n diagonal invertida obliga a la función print() a?:",
            "opciones": ["a) Imprimir un espacio en blanco", "b) No hacer nada", "c) Dar un salto de línea"],
            "respuesta": "c"
        },
        {
            "pregunta": "¿El carácter de escape le debe su nombre al hecho de que?:",
            "opciones": ["a) Se utiliza para eliminar caracteres", "b) Cambia el significado del carácter después de él", "c) Añade un carácter especial"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿El parámetro posicional está determinado por?",
            "opciones": ["a) Su posición", "b) Su valor", "c) Su tipo de dato"],
            "respuesta": "a"
        },
        {
            "pregunta": "¿Cuáles de los siguientes nombres de variables son ilegales?",
            "opciones": ["a) var_1", "b) True", "c) variableNombre"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿La diferencia más importante entre números enteros y flotantes es que?:",
            "opciones": ["a) Se almacenan de manera diferente en la memoria de la computadora", "b) Los enteros son más precisos", "c) Los flotantes ocupan más espacio"],
            "respuesta": "a"
        }
    ]

    puntaje = 0  # Variable para almacenar la puntuación del usuario

    reproducir_audio("¡Bienvenido al Juego de Trivia sobre Python!")

    for idx, pregunta in enumerate(preguntas, 1):
        limpiar_pantalla()
        texto_pregunta = f"Pregunta {idx}: {pregunta['pregunta']}"
        print(texto_pregunta)
        reproducir_audio(texto_pregunta)

        for opcion in pregunta['opciones']:
            print(opcion)
            reproducir_audio(opcion)

        # Solicitar la respuesta del usuario
        while True:
            respuesta_usuario = input("Tu respuesta (a/b/c): ").lower()
            if respuesta_usuario in ['a', 'b', 'c', 'd']:
                break
            else:
                mensaje_error = "Entrada inválida. Por favor, introduce a, b, c."
                print(mensaje_error)
                reproducir_audio(mensaje_error)

        # Verificar la respuesta
        if respuesta_usuario == pregunta['respuesta']:
            mensaje_correcto = "¡Correcto!"
            print(mensaje_correcto)
            reproducir_audio(mensaje_correcto)
            puntaje += 1
        else:
            # Obtener la letra de la opción correcta
            respuesta_letra = pregunta['respuesta']
            opciones_dict = {op[0]: op for op in pregunta['opciones']}
            respuesta_texto = opciones_dict[respuesta_letra][3:]  # Obtener el texto después de "x) "
            mensaje_incorrecto = f"Incorrecto. La respuesta correcta es la opción '{respuesta_letra}) {respuesta_texto}'."
            print(mensaje_incorrecto)
            reproducir_audio(mensaje_incorrecto)

        time.sleep(2)  # Pausar para que el usuario lea el mensaje

    # Mostrar el puntaje final
    mensaje_final = f"Has completado el juego. Tu puntaje es: {puntaje} de {len(preguntas)}"
    print(mensaje_final)
    reproducir_audio(mensaje_final)

    reproducir_audio("Gracias por jugar. ¡Hasta la próxima!")

if __name__ == "__main__":
    juego_de_trivia()
