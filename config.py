import sys

from icloud_service import localizar_icloud
from google_service import localizar_google

def menu():
    print("\n=== Localizador de Dispositivos ===")
    print("1. Localizar dispositivo con iCloud")
    print("2. Localizar dispositivo con Google")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")
    return opcion

def main():
    while True:
        opcion = menu()

        if opcion == "1":
            print("\nIniciando localización mediante iCloud...")
            try:
                localizar_icloud()
            except Exception as e:
                print(f"Error al localizar con iCloud: {e}")

        elif opcion == "2":
            print("\nIniciando localización mediante Google...")
            try:
                localizar_google()
            except Exception as e:
                print(f"Error al localizar con Google: {e}")

        elif opcion == "3":
            print("\nSaliendo del programa. ¡Hasta pronto!")
            sys.exit()

        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
