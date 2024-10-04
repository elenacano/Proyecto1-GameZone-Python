from src import piedra_papel_tijera as ppt

def mostrar_menu():
    print("\nBIENVENIDOS AL SALÓN DE JUEGOS MARAVILLA:")
    print("1-Piedra, papel, tijera")
    print("2-Ahorcado")
    print("3-Trivial")
    print("4-Tres en raya")
    print("5-Salir\n")



def main():
    
    while True:
        seleccion = 0
        mostrar_menu()
        try:
            juego_seleccionado = int(input("Seleccione el número del juego al que desea jugar: "))
        
            if juego_seleccionado == 5:
                print("Gracias por jugar con nosotros, hasta pronto.\n")
                break

            elif juego_seleccionado == 1:
                seleccion = ppt.inicio_ppt()

            else:
                print("\nPor favor ingrese un número entre 1 y 5.")

            if seleccion == 3:
                    print("Gracias por jugar con nosotros, hasta pronto.\n")
                    break

        except ValueError:
            print("Por favor ingrese un número entre 1 y 5.\n")
            main()



if __name__ == "__main__":
    main()

