from src import piedra_papel_tijera as ppt

def mostrar_menu():
    print("\nBIENVENIDOS AL SALÓN DE JUEGOS MARAVILLA:")
    print("1-Piedra, papel, tijera")
    print("2-Ahorcado")
    print("3-Trivial")
    print("4-Tres en raya")
    print("5-Salir\n")


def mostrar_menu_final():
    print("\n\n --------------JUEGO FINALIZADO-----------------")
    print("Desea:")
    print("1-Volver a jugar")
    print("2-Volver al menu principal")
    print("3-Salir")
    print("\n\n ------------------------------------------------")

def main():
    
    mostrar_menu()
    try:
        juego_seleccionado = int(input("Seleccione el número del juego al que desea jugar:"))
    
        if juego_seleccionado == 5:
            print("Gracias por jugar con nosotros, hasta pronto.")

        elif juego_seleccionado == 1:
            ppt.inicio_ppt()
            mostrar_menu_final()

        else:
            print("\nPor favor ingrese un número entre 1 y 5.")
            main()
            

    except ValueError:
        print("Por favor ingrese un número entre 1 y 5.")
        main()



if __name__ == "__main__":
    main()

