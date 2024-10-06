import random
from src import auxiliar

class juagada_ppt():
    def __init__(self, ):
        self.opciones_permitidas = ["piedra", "papel", "tijera"]
        self.rondas = 0
        self.victorias_jugador = 0
        self.victorias_maquina = 0

    def get_rondas(self):
        """Devuelve el atributo rondas.

        Returns:
            int: número de rondas que se han jugado.
        """
        return self.rondas

    def get_opciones_permitidas(self):
        """Devuelve el atributo de opciones_permitidas.

        Returns:
            list: lista de las opciones permitidas.
        """
        return self.opciones_permitidas
    
    def revisar_opciones_permitidas(self, opcion):
        """Comprueba que modo de juego se está jugando y si es el lagarto, spock añade esas opciones a las opciones_permitidas.

        Args:
            opcion (int): un 1 si es el clásico, 2 si es con lagarto, spock.
        """
        self.opcion_juego = opcion
        if opcion == 2:
            self.opciones_permitidas.extend(["lagarto", "spock"])
        return
    
    def incrementar_rondas(self):
        """Aumenta las rondas jugadas.

        Returns:
            int: número de rondas jugadas.
        """
        self.rondas += 1
        return self.rondas
    
    def comprobar_seleccion(self, seleccion_usuario):
        """Comprueba si la seleccion del usuario está entre las opciones permitidas.

        Args:
            seleccion_usuario (str): elección que ha introducido el usuario

        Returns:
            bool: True si la elección del usuario está entre las permitidas, False de lo contrario.
        """
        if seleccion_usuario not in self.opciones_permitidas:
            return False
        else:
            return True
        
    def generar_opcion_maquina(self):
        """Genera de manera aleatoria la opción que va a sacar la máquina

        Returns:
            str: nombre de la opción elegida por la máquina
        """
        return random.choice(self.opciones_permitidas)


    def batalla(self, seleccion_usuario, seleccion_maquina):
        """Dada la selección del usuario y la de la máquina comprueba quien es el ganador o si ha habido empate y aumenta sus contadores de victorias.

        Args:
            seleccion_usuario (str): elección introducida por el usuario
            seleccion_maquina (str): elección generada para la máquina

        Returns:
            None
        """
        user_gana = "HAS GANADO! 🎉"
        user_pierde = "SO SORRY LOOOSER 👻​"

        if seleccion_usuario == seleccion_maquina:
            print('EMPATE!')

        elif seleccion_usuario == 'piedra':
            if seleccion_maquina in ['tijera', 'lagarto']:
                print(user_gana)
                self.victorias_jugador += 1
            else:
                print(user_pierde)
                self.victorias_maquina += 1

        elif seleccion_usuario == 'papel':
            if seleccion_maquina in ['piedra', 'spock']:
                print(user_gana)
                self.victorias_jugador += 1
            else:
                print(user_pierde)
                self.victorias_maquina += 1

        elif seleccion_usuario == 'tijera':
            if seleccion_maquina in ['papel', 'lagarto']:
                print(user_gana)
                self.victorias_jugador += 1
            else:
                print(user_pierde)
                self.victorias_maquina += 1

        elif seleccion_usuario == 'lagarto':
            if seleccion_maquina in ['spock', 'papel']:
                print(user_gana)
                self.victorias_jugador += 1
            else:
                print(user_pierde)
                self.victorias_maquina += 1

        elif seleccion_usuario == 'spock':
            if seleccion_maquina in ['tijera', 'piedra']:
                print(user_gana)
                self.victorias_jugador += 1
            else:
                print(user_pierde)
                self.victorias_maquina += 1
        return

    
    def ganador(self):
        """Muestra por pantalla quien ha sido el ganador o si ha habido empate después de jugar las rondas estipuladas.
        """
        if self.victorias_jugador < self.victorias_maquina:
            print("HAS PERDIDO 😘​​")

        elif self.victorias_jugador > self.victorias_maquina:
            print("HAS SIDO EL GANADOR 🏆")
        
        else:
            print("HA HABIDO UN EMPATE 💩​")
        return


def imprimir_bienvenida():
    print("\n")
    print("╔═══════════════════════════════════════════════════════╗")
    print("║        PIEDRA - PAPEL - TIJERA - LAGARTO - SPOCK      ║")
    print("╚═══════════════════════════════════════════════════════╝")
    print("\n           ¡Bienvenido a la Batalla Definitiva!          ")
    print("\n")
    print("       ⭐  Prepárate para un duelo de lógica y suerte ⭐   ")
    print("\n")


    print("╔════════════════════════════════════════════════════════╗")
    print("║  REGLAS DEL JUEGO:                                     ║")
    print("║  🪨 Piedra aplasta Tijera y Lagarto                     ║")
    print("║  ✋ Papel envuelve Piedra y refuta Spock               ║")
    print("║  ✂️  Tijera corta Papel y decapita Lagarto              ║")
    print("║  🦎 Lagarto envenena Spock y devora Papel              ║")
    print("║  🖖 Spock vaporiza Piedra y rompe Tijera               ║")
    print("╚════════════════════════════════════════════════════════╝")

    print("-------------------------------------------------------")
    print("                 ELIJE TU MODO DE JUEGO              ")
    print("-------------------------------------------------------")
    print("   1️⃣  Clásico (Piedra, Papel, Tijera)                ")
    print("   2️⃣  Extendido (Piedra, Papel, Tijera, Lagarto, Spock) ")
    print("-------------------------------------------------------")


def inicio_ppt():
    while True:
        imprimir_bienvenida()

        try:
            num_rondas = 2 #CAMBIAR ESTA VARIABLE PARA JUGAR MÁS RONDAS
            opcion = 0 # Inicializamos la variable para hacer la gestión de errorres en caso de que no introduzcan 1 o 2
            jugada = juagada_ppt()

            # Le pedimos un número hasta que introduzca 1 o 2
            while True:
                opcion = int(input("Seleccione la opción deseada: "))
                if opcion != 1 and opcion !=2:
                    print("\nPor favor seleccione 1 o 2.")
                else:
                    break
            
            # Si estamos jugando con lagarto y spock lo añade a las opciones
            jugada.revisar_opciones_permitidas(opcion)

            while jugada.get_rondas() != num_rondas:
                opciones_tirada = jugada.opciones_permitidas
                opciones_tirada_string = ', '.join(map(str, opciones_tirada))
                

                while True:
                    seleccion_usuario = input(f'\nEscriba su elección entre: {opciones_tirada_string} -> ')
                    seleccion_usuario = seleccion_usuario.strip().lower()
                    es_correcto = jugada.comprobar_seleccion(seleccion_usuario)
                    if es_correcto:
                        break
                
                seleccion_maquina = jugada.generar_opcion_maquina()
                print(f'La maquina ha elegido: {seleccion_maquina}')

                jugada.batalla(seleccion_usuario, seleccion_maquina)
                jugada.incrementar_rondas()

            print("\nLA PARTIDA HA TERMINADO")
            print(f'Tus puntos: {jugada.victorias_jugador}')
            print(f'Puntos de la máquina: {jugada.victorias_maquina}')
            jugada.ganador()

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
    
        except ValueError:
            print("\nPor favor seleccione 1 o 2.")
