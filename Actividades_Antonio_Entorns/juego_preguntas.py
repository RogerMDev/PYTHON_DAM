

class Pregunta:
    def __init__(self, pregunta, opciones, respuesta_correcta):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta

class JuegoTrivia:
    def __init__(self):
        self.puntuacion = 0
        self.lista_preguntas = []

    def agregar_pregunta(self, pregunta):
        """Añade una pregunta a la lista."""
        self.lista_preguntas.append(pregunta)

    def comprobar_respuesta(self, pregunta):
        """Pide al usuario que ingrese una respuesta y verifica si es correcta."""
        try:
            respuesta_usuario = int(input("Tu respuesta (1-4): "))  # Convertimos a número
            if 1 <= respuesta_usuario <= 4:  # Verifica si está en el rango válido
                if pregunta.opciones[respuesta_usuario - 1] == pregunta.respuesta_correcta:
                    print("✅ Respuesta correcta!")
                    return True
                else:
                    print(f"❌ Respuesta incorrecta. La correcta era: {pregunta.respuesta_correcta}")
                    return False
            else:
                print("⚠️ Debes ingresar un número entre 1 y 4.")
                return False
        except ValueError:
            print("⚠️ Entrada no válida. Ingresa un número del 1 al 4.")
            return False

    def iniciar_juego(self):
        """Muestra las preguntas, recibe respuestas y actualiza la puntuación."""
        for pregunta in self.lista_preguntas:
            print(f"\n{pregunta.pregunta}")  # Muestra la pregunta
            for i, opcion in enumerate(pregunta.opciones, 1):
                print(f"{i}. {opcion}")  # Muestra opciones numeradas

            if self.comprobar_respuesta(pregunta):  # Verifica respuesta
                self.puntuacion += 1

        print(f"\n🎯 Juego terminado. Puntuación final: {self.puntuacion}/{len(self.lista_preguntas)}")


pregunta1 = Pregunta("¿Cuál es el nombre del fontanero más famoso de Nintendo?",
                     ["Luigi", "Wario", "Mario", "Toad"], "Mario")

pregunta2 = Pregunta("¿En qué juego se popularizó la frase 'The cake is a lie'?",
                     ["Half-Life", "Portal", "Bioshock", "Doom"], "Portal")

pregunta3 = Pregunta("¿Cómo se llama el personaje principal de la saga 'The Legend of Zelda'?",
                     ["Zelda", "Ganondorf", "Epona", "Link"], "Link")

pregunta4 = Pregunta("¿Cuál es el videojuego más vendido de todos los tiempos?",
                     ["Minecraft", "GTA V", "Tetris", "Fortnite"], "Minecraft")

pregunta5 = Pregunta("¿En qué año se lanzó el primer juego de 'Pokémon'?",
                     ["1996", "1998", "2000", "1994"], "1996")

pregunta6 = Pregunta("¿Cómo se llama el hermano de Mario en los videojuegos de Nintendo?",
                     ["Wario", "Luigi", "Bowser", "Toad"], "Luigi")

pregunta7 = Pregunta("¿Qué compañía desarrolló la saga 'The Elder Scrolls'?",
                     ["Ubisoft", "Bethesda", "CD Projekt Red", "EA"], "Bethesda")

pregunta8 = Pregunta("¿En qué juego apareció por primera vez el personaje de Sonic?",
                     ["Sonic the Hedgehog", "Sonic & Knuckles", "Sonic Adventure", "Sonic Boom"], "Sonic the Hedgehog")

pregunta9 = Pregunta("¿Cuál es el nombre del villano principal en 'Resident Evil'?",
                     ["Albert Wesker", "Nemesis", "Leon Kennedy", "Jill Valentine"], "Albert Wesker")

pregunta10 = Pregunta("¿Cómo se llama el mundo donde se desarrolla 'The Witcher'?",
                      ["Tamriel", "Hyrule", "The Continent", "Skyrim"], "The Continent")
juego = JuegoTrivia()
juego.agregar_pregunta(pregunta1)
juego.agregar_pregunta(pregunta2)
juego.agregar_pregunta(pregunta3)
juego.agregar_pregunta(pregunta4)
juego.agregar_pregunta(pregunta5)
juego.agregar_pregunta(pregunta6)
juego.agregar_pregunta(pregunta7)
juego.agregar_pregunta(pregunta8)
juego.agregar_pregunta(pregunta9)
juego.agregar_pregunta(pregunta10)

juego.iniciar_juego()





