from src import auxiliar
import time

class jugada_ahorcado():
    def __init__(self):
        self.intentos = 6
        self.lista_abecedario = list('abcdefghijklmnñopqrstuvwxyz')
        self.letras_descartadas = []
        self.letras_usadas_validas = []   
    
    def get_letras_descartadas(self):
        """Devuelve el valor del atributo letras_descartadas.

        Returns:
            list: letras introducidas que no se encuentran en la palabra.
        """
        return self.letras_descartadas
    
    def aniadir_letras_descartadas(self, letra):
        """Añade una nueva letra al atributo de letras_descartadas.

        Args:
            letra (str): letra introducida por el jugador.

        Returns:
            lista: lista de las letras descartadas una vez añadida la que se ha pasado como argumento.
        """
        return self.letras_descartadas.append(letra)
    
    def decrementar_intentos(self):
        """Reduce en uno los intentos restantes para adivinar la palabra.

        Returns:
            int: intentos restantes actualmente.
        """
        self.intentos -= 1
        return self.intentos
    
    def seleccion_palabra_oculta(self):
        """Llama al archivo auxiliar para generar la palabra oculta.

        Returns:
            None
        """
        self.palabra_original = auxiliar.selecccion_palabra()
        self.palabra = list(self.palabra_original)
        self.palabra_oculta = ['_']*len(self.palabra)
        return


    def mostrar_dibujo_ahorcado(self):
        """Muestra el dibujo del ahorcado correspondiente al número de rondas restantes.

        Returns:
            str: el elemento correspondiente de la lista dibujo_ahorcado.
        """
        dibujo_ahorcado = [
            '''
            +---+
            |   |
                |
                |
                |
                |
            =========
            ''', 
            '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========
            ''',
            '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========
            ''',
            '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========
            ''',
            '''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
            =========
            ''',
            '''
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            =========
            ''',
        ]
        return dibujo_ahorcado[6-self.intentos]


    def mostrar_estado(self):
        """Para cada ronda muestra los intentos restantes, las lestras descartadas, la palabra oculta con las letras adivinadas y el dibujo del ahorcado actual.
        
        Returns:
            None
        """
        print("\n═════════════════════════════════════")
        print(f'     Intentos restantes: {self.intentos}')
        print(f'     Letras descartadas: {", ".join(self.letras_descartadas)}\n')
        print(f'     Palabra: {" ".join(self.palabra_oculta)}\n')
        print(self.mostrar_dibujo_ahorcado())

    def letra_valida(self, letra):
        """Comprueba que la nueva letra introducida por el jugador sea una letra, no se haya introducido antes y no esté descartada ni acertada.

        Args:
            letra (str): letra introducida por el usuario.

        Returns:
            bool: True si la letra es válida y cumple todas las condiciones, False de lo contrario.
        """
        if len(letra) != 1 :
            print('Has puesto más de una letra, inténtalo de nuevo.')
            return False
        elif letra not in self.lista_abecedario:
            print('No has introducido una letra del abecedario')
            return False
        elif letra in self.palabra_oculta:
            print('La letra que has introducido ya la has acertado, inténtalo de nuevo.')
            return False
        elif letra in self.letras_descartadas:
            print('Esa letra ya la habías dicho, inténtalo de nuevo.')
            return False
        else:
            return True
    
    def gestion_letra(self, letra):
        """Comprueba en que posiciones de la palabra oculta está la letra introducida y desvela dichas posiciones.

        Args:
            letra (str): letra introducida por el jugador.

        Returns:
            None.
        """
        for i in range(len(self.palabra)):
            if self.palabra[i] == letra:
                self.palabra_oculta[i] = letra
                self.palabra[i] = '_'
        return

    def final_juego(self):
        """Comprueba si el jugador ha ganado o perdido y muestra los mensajes correspondientes.

        Resturns:
            None.
        """
        print("\n═════════════════════════════════════")
        if '_' not in self.palabra_oculta:
            print('\n🏆¡ENHORABUENA! ¡HAS GANADO EL JUEGO!🏆')
        else:
            print(f'\nOh!😞 Lo siento, ¡has perdido!'
                '''\n
            +---+
            |   |
           💀   |
           /|\  |
           / \  |
                |
            =========
            ''')
            print(f'La palabra oculta era : {(self.palabra_original).upper()}')


def bienvenida_ahorcado():
    """Imprime un mensaje de bienvenida al juego.

    Returns:
        None
    """
    print("\n\n╔══════════════════════════════════════════════╗")
    print("║                                              ║")
    print("║  🔮  BIENVENIDO AL DESAFÍO DEL AHORCADO  🔮  ║")
    print("║                                              ║")
    print("╠══════════════════════════════════════════════╣")
    print("║                                              ║")
    print("║      Prepárate para salvarte o caer...  ⚔️    ║")
    print("║                                              ║")
    print("║       👁️  Adivina la palabra oculta!  👁️       ║")
    print("║                                              ║")
    print("║      Cada error te acerca más al final...    ║")
    print("║                                              ║")
    print("║     ¿Podrás descubrir la palabra a tiempo?   ║")
    print("║                                              ║")
    print("╚══════════════════════════════════════════════╝")




def inicio_ahorcado():
    """Inicializa el juego del ahorcado y gestiona toda la partida.

    Returns:
        int: devolverá un 2 para volver al menú principal y un 3 para salir.
    """
    flag = 0
    while True:
        jugada = jugada_ahorcado()
        jugada.seleccion_palabra_oculta()
        
        if flag == 0:
            bienvenida_ahorcado()
            flag = 1

        while jugada.intentos > 0 and '_' in jugada.palabra_oculta:
            jugada.mostrar_estado()
            letra = input('INTRODUCE LETRA: ').lower()

            while not jugada.letra_valida(letra):
                letra = input('INTRODUCE OTRA LETRA: ').lower()

            if letra in jugada.palabra:
                jugada.gestion_letra(letra)
                print("\n✨ ¡Has acertado la letra! Sigue así.")
                time.sleep(1)

            else:
                print('❌ ¡Has fallado la letra!')
                jugada.aniadir_letras_descartadas(letra)
                jugada.decrementar_intentos()
                time.sleep(1)

        jugada.final_juego()
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