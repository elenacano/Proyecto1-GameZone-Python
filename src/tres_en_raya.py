import random
from src import auxiliar

class jugada_tres_raya():
    def __init__(self):
        self.opciones_fichas = ["❌​", "⭕​"]
        self.ficha_jugador = "❌​"
        self.ficha_maquina = "⭕​"
        self.tablero = [-1,1,2,3,4,5,6,7,8,9]

    def dibujar_tablero(self):
        """
        Dibuja el tablero en su estado actual.

        Returns:
            list: la lista donde se almacena lo que hay en cada posición del tablero.
        """
        self.tablero[0]=-1
        print("   "+str(self.tablero[1])+"   |   "+str(self.tablero[2])+"   |   "+str(self.tablero[3])+"   ")
        print("-------------------------")
        print("   "+str(self.tablero[4])+"   |   "+str(self.tablero[5])+"   |   "+str(self.tablero[6])+"   ")
        print("-------------------------")
        print("   "+str(self.tablero[7])+"   |   "+str(self.tablero[8])+"   |   "+str(self.tablero[9])+"   ")
        print("-------------------------")
        return self.tablero

    def jugada_maquina(self):
        """Genera la posición de la ficha de la máquina y la añade al tablero

        Returns: 
            None
        """
        movimientos_posibles = []
        esquinas_disponibles=[]
        available_edges=[]
        centro_disponible=[]
        posicion = -1

        #Todas las opciones donde podemos poner ficha
        for i in range(1,len(self.tablero)):
            if self.tablero[i] not in self.opciones_fichas:
                movimientos_posibles.append(i)

        # Comprobamos si en alguna posición gana la maquina o gana el contrincante
        for ficha in self.opciones_fichas:
            for i in movimientos_posibles:
                copia_tablero = self.tablero[:]
                copia_tablero[i] = ficha
                if self.es_ganador(copia_tablero, ficha):
                    posicion = i

        # Si no hay movimiento ganador o que arruine la victoria del usuario
        # se elige una posición aleatoria empezando por las esquinas disponibles
        # luego el centro y los laterales
        if posicion == -1:
            for i in range(len(self.tablero)):
                if self.tablero[i] not in self.opciones_fichas:
                    if i in [1,3,7,9]:
                        esquinas_disponibles.append(i)
                    if i == 5:
                        centro_disponible.append(i)
                    if i in [2,4,6,8]:
                        available_edges.append(i)

            if len(esquinas_disponibles)>0:
                posicion=random.choice(esquinas_disponibles)
            
            elif len(centro_disponible)>0:
                posicion=centro_disponible[0]
            
            elif len(available_edges)>0:
                posicion=random.choice(available_edges)

        self.tablero[posicion]=self.ficha_maquina
        return

    def es_ganador(self, tablero = None, ficha = None):
        """Compruba si dado un tablero y una ficha, el usuario de dicha ficha ha hecho una jugada ganadora

        Args:
            tablero (list): lista de 10 elemetos que representa el tablero
            ficha (str): ficha del jugador del cual revisamos si hay una jugada ganadora

        Returns:
            bool: devuelve True si hay una jugada ganadora para la ficha dada y si no False
        """
        if tablero is None:
            tablero = self.tablero
        if ficha is None:
            ficha = self.ficha_jugador
        return (tablero[1] == ficha and tablero[2] == ficha and tablero[3] == ficha) or \
        (tablero[4] == ficha and tablero[5] == ficha and tablero[6] == ficha) or \
        (tablero[7] == ficha and tablero[8] == ficha and tablero[9] == ficha) or \
        (tablero[1] == ficha and tablero[4] == ficha and tablero[7] == ficha) or \
        (tablero[2] == ficha and tablero[5] == ficha and tablero[8] == ficha) or \
        (tablero[3] == ficha and tablero[6] == ficha and tablero[9] == ficha) or \
        (tablero[1] == ficha and tablero[5] == ficha and tablero[9] == ficha) or \
        (tablero[3] == ficha and tablero[5] == ficha and tablero[7] == ficha)

    def posicion_ocupada(self, position):
        """Comprueba si para la posición dada se puede poner ahí una ficha o esa posición ya tiene una ficha.

        Args:
            position (int): entero entre 1 y 9 cuya posición en la lista veremos si esta ocupada por una de las posibles fichas.

        Returns:
            bool: True si está ocupada la posición, False de lo contrario.
        """
        if type(self.tablero[position]) == int:
                return False
        return True

    def tablero_lleno(self):
        """Compueba si el tablero ya tiene todas las posiciones ocupadas.

        Returns:
            bool: True si el tablero ya está lleno, False de lo contrario.
        """
        for i in range(1,len(self.tablero)):
            if self.posicion_ocupada(i) == False:
                return False
        return True

    def colocar_ficha(self, pos):
        self.tablero[pos]=self.ficha_jugador


def bienvenida_tres_en_raya():
    """
        Imprime un bienvenida y las instrucciones del juego.
    """
    print("\n\n╔══════════════════════════════════════════════╗")
    print("║                                              ║")
    print("║ 🎮  BIENVENIDO AL RETO DEL TRES EN RAYA  🎮  ║")
    print("║                                              ║")
    print("╠══════════════════════════════════════════════╣")
    print("║                                              ║")
    print("║      ⚔️   ¡Prepárate para la batalla!  ⚔️      ║")
    print("║                                              ║")
    print("║  🧠 Pon a prueba tu estrategia y astucia 🧠  ║")
    print("║                                              ║")
    print("║       Logra una línea antes que tu rival!    ║")
    print("║                                              ║")
    print("║      Haz que tus ❌'s dominen el tablero!    ║")
    print("║                                              ║")
    print("╚══════════════════════════════════════════════╝")

    print("\n\n--------------------------------------------------------------------------------------------------------------")
    print("                                          INSTRUCCIONES                                                           ")
    print("--------------------------------------------------------------------------------------------------------------")
    print(" 1- Comienza usted introduciendo en que posición del tablero quiere poner su ficha, que es la ❌               ")
    print(" 2- La posición de la ficha de la máquina se generará automáticamente.")
    print(" 3- Se imprimirá la situación actual del tablero con la posición de su ficha y la posición seleccionada por la máquina.")
    print("--------------------------------------------------------------------------------------------------------------\n\n")
    return


def inicio_tres_raya():
    """Inicializa el juego del tres en raya y gestiona toda la partida.

    Returns:
        int: devolverá un 2 para volver al menú principal y un 3 para salir.
    """

    bienvenida_tres_en_raya()

    while True:
        jugada = jugada_tres_raya()
        jugada.dibujar_tablero()
        flag = 0

        while jugada.tablero_lleno() == False:
            while True:
                try:
                    position=int(input("Seleccione una posición entre 1-9 para colocar su ficha ❌: " ))
                    if position not in range(1,10):
                        position=print("Por favor, el número debe estar entre 1 y 9.")

                    elif jugada.posicion_ocupada(position):
                        position=print("La posición seleccionada está ocupada, eliga otra.")
                    else:
                        break

                except:
                    position=print("Debe introducir un número por teclado.")

            jugada.colocar_ficha(position)
            jugada.jugada_maquina()
            jugada.dibujar_tablero()

            if jugada.es_ganador(ficha = jugada.ficha_jugador):
                print("HAS SIDO EL GANADOR 🏆")
                flag = 1
                break
            elif jugada.es_ganador(ficha = jugada.ficha_maquina):
                print("HAS PERDIDO CONTRA UNA MAQUINA 😘​​")
                flag = 1
                break

        if jugada.tablero_lleno() and flag == 0:
            print("EMPATE! 💩")

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
