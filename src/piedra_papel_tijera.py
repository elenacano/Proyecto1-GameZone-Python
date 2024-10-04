import random 

class juagada_ppt():
    def __init__(self, ):
        self.opciones_permitidas = ["piedra", "papel", "tijera"]
        self.rondas = 0
        self.victorias_jugador = 0
        self.victorias_maquina = 0

    def get_rondas(self):
        return self.rondas

    def get_opciones_permitidas(self):
        return self.opciones_permitidas
    
    def revisar_opciones_permitidas(self, opcion):
        self.opcion_juego = opcion
        if opcion == 2:
            self.opciones_permitidas.extend(["lagarto", "spock"])
        return
    
    def incrementar_rondas(self):
        self.rondas += 1
        return self.rondas
    
    def comprobar_seleccion(self, seleccion_usuario):
        if seleccion_usuario not in self.opciones_permitidas:
            return False
        else:
            return True
        
    def generar_opcion_maquina(self):
        return random.choice(self.opciones_permitidas)


    def batalla(self, seleccion_usuario, seleccion_maquina):
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
        if self.victorias_jugador < self.victorias_maquina:
            print("HAS PERDIDO 😘​​")

        elif self.victorias_jugador > self.victorias_maquina:
            print("HAS SIDO EL GANADOR 🏆")
        
        else:
            print("HA HABIDO UN EMPATE 💩​")



def inicio_ppt():
    while True:

        print("\nBuenas, bienvenido al juego PIEDRA, PAPEL, TIJERA, eliga modalidad de juego")
        print("1-Clásico")
        print("2-Piedra, papel, tijera, lagarto, spoke")

        try:
            opcion = 0
            num_rondas = 2
            jugada = juagada_ppt()

            # Le pedimo un número hasta que introduzca 1 o 2
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
                    seleccion_final = int(input("\nPulse: \n 1-Si desea volver a jugar \n 2-Si desea volver al menu principal \n 3-Si desea salir\n Su opción: "))
                    if seleccion_final == 1:
                        break
                    elif seleccion_final == 2 or seleccion_final == 3:
                        return seleccion_final
                except ValueError:
                    print("\nPor favor seleccione 1,2 o 3.")
    
        except ValueError:
            print("\nPor favor seleccione 1 o 2.")
