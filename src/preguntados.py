from src import auxiliar

class jugada_preguntados():
    def __init__(self):
        self.victorias = 0
    
    def get_pregunta(self):
        """ Genera la categoría y pregunta aleatoria y las guarda como atributos.

        Returns:
            None
        """
        categoria, pregunta_categoria = auxiliar.seleccion_pregunta_preguntados()
        self.categoria_actual = categoria
        self.pregunta_actual = pregunta_categoria
        return

    def mostar_pregunta(self):
        """Muestra la ronda actual, la categoría, la pregunta y las posibles respuestas.

        Returns:
            None
        """
        print("\n╔══════════════════════════════════════════╗")
        print(f'  RONDA {self.victorias+1}                   ')
        print(f'  Categoria: {self.categoria_actual}         ')
        print("╚══════════════════════════════════════════╝\n")
        print(f'{self.pregunta_actual["Pregunta"]}')

        resp_letra = ['A', 'B', 'C', 'D']
        i=0
        for respuesta, es_correcta in self.pregunta_actual["Respuestas"].items():
            print(f"  {resp_letra[i]}. {respuesta}")
            i+=1
        return

    def comprobar_respuesta(self, respuesta_seleccionada):
        """Comprueba si la respuesta seleccionada por el jugador el correcta o no y muestra un mensaje.

        Args:
            respuesta_seleccionada (str): la respuesta seleccionada por el usuario en formato: "A", "B", "C" o "D".

        Returns:
            bool: True si la respuesta seleccionada es la correcta, False de lo contrario.
        """
        mapeo = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3
        }
        indice = mapeo[respuesta_seleccionada]
        respuestas = list(self.pregunta_actual["Respuestas"].items())
        es_correcta = respuestas[indice][1]
        if es_correcta:
            self.victorias += 1
            print("\nCORRECTO ✅")
        else:
            print("\nINCORRECTO ❌")
            for resp in respuestas:
                if resp[1]:
                    print(f'La respuesta correcta es: {resp[0]}')
            print("\n═════════════════════════════════════")
            print("\n            FIN DEL JUEGO             ")
        return es_correcta




def bienvenida_preguntados():
    """
        Imprime una bienvenida y las instrucciones del juego Preguntados.
    """
    print("\n\n╔══════════════════════════════════════════════╗")
    print("║                                              ║")
    print("║  🎉 BIENVENIDO AL DESAFÍO DE PREGUNTADOS 🎉  ║")
    print("║                                              ║")
    print("╠══════════════════════════════════════════════╣")
    print("║                                              ║")
    print("║   🧠 ¡Demuestra tu conocimiento total! 🧠    ║")
    print("║                                              ║")
    print("║ 📚Cultura, historia, entretenimiento y más🎬 ║")
    print("║                                              ║")
    print("║  ¿Podrás responder correctamente 10 veces?🎯 ║")
    print("║                                              ║")
    print("║     ¡Responde bien o el juego termina! 😱    ║")
    print("║                                              ║")
    print("╚══════════════════════════════════════════════╝")

    print("\n\n--------------------------------------------------------------------------------------------------------------")
    print("                                          INSTRUCCIONES                                                           ")
    print("--------------------------------------------------------------------------------------------------------------")
    print(" 1- Se te harán preguntas de distintas categorías como: cultura, historia, entretenimiento, etc.")
    print(" 2- Debes responder correctamente a 10 preguntas consecutivas para ganar.")
    print(" 3- Si fallas una pregunta, el juego termina automáticamente.")
    print(" 4- ¡Pon a prueba tus conocimientos y diviértete aprendiendo!")
    print("--------------------------------------------------------------------------------------------------------------\n\n")


def inicio_preguntados():
    """Inicializa el juego preguntados y gestiona toda la partida.

    Returns:
        int: devolverá un 2 para volver al menú principal y un 3 para salir.
    """

    bienvenida_preguntados()

    while True:

        rondas = 2
        jugada = jugada_preguntados()

        while jugada.victorias != rondas:
            jugada.get_pregunta()
            jugada.mostar_pregunta()

            while True:
                respuesta = input("Introduzaca la lestra correspondiente A, B, C, D: ")
                respuesta = respuesta.strip().upper()
                if respuesta not in ["A", "B", "C", "D"]:
                    print("Por favor, introduzca A, B, C o D.")
                else: 
                    break

            es_correcta = jugada.comprobar_respuesta(respuesta)
            if es_correcta == False:
                break

        if jugada.victorias == rondas:
            print("\n═════════════════════════════════════")
            print(f"\n  🏆 ​HAS SUPERADO LAS {rondas} RONDAS 🏆​ ")

        seleccion_final = 0
        while True:
            try:
                seleccion_final = auxiliar.mostrar_final_juego()
                if seleccion_final == 1:
                    break
                elif seleccion_final == 2 or seleccion_final == 3:
                    return seleccion_final
            except ValueError:
                print("\nPor favor seleccione 1,2 o 3.")

