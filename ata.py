import itertools
import time

def crear_pin():
    """Permite al usuario establecer un PIN manualmente."""
    while True:
        pin = input("\n🔑 Crea tu PIN (4-8 dígitos numéricos): ").strip()
        
        if pin.isdigit() and 4 <= len(pin) <= 8:
            with open("pin_usuario.txt", "w") as file:
                file.write(pin)
            print(f"✅ PIN guardado correctamente.")
            return pin
        else:
            print("❌ El PIN debe ser numérico y tener entre 4 y 8 dígitos.")

def ataque_fuerza_bruta():
    """Simula un ataque de fuerza bruta para descubrir el PIN."""
    try:
        with open("pin_usuario.txt", "r") as file:
            pin_objetivo = file.read().strip()
    except FileNotFoundError:
        print("❌ No hay PIN guardado. Crea uno primero.")
        return
    
    print("\n🚀 Iniciando ataque de fuerza bruta...")

    longitud = len(pin_objetivo)
    intentos = 0
    inicio = time.time()

    pines_comunes = [
        "0000", "1234", "1111", "2222", "5555", "9999", "1212", "6969", "1004", "2000", 
        "4444", "3333", "7777", "6666", "8888", "2580", "0852", "1998", "2024", "2010"
    ]

    for pin in pines_comunes:
        intentos += 1
        if pin == pin_objetivo:
            print(f"\n🎯 PIN encontrado: {pin} en {intentos} intentos ({time.time() - inicio:.2f} segundos)")
            return

    for pin in itertools.product("0123456789", repeat=longitud):
        intento = "".join(pin)
        intentos += 1
        if intento == pin_objetivo:
            print(f"\n🎯 PIN encontrado: {intento} en {intentos} intentos ({time.time() - inicio:.2f} segundos)")
            return

    print("\n❌ No se pudo encontrar el PIN (esto no debería pasar).")

def menu():
    """Muestra el menú principal del programa."""
    while True:
        print("\n🔒 Sistema de Seguridad con PIN 🔒")
        print("1. Crear un PIN")
        print("2. Atacar un PIN con fuerza bruta")
        print("3. Salir")

        opcion = input("\nElige una opción (1/2/3): ").strip()

        if opcion == "1":
            crear_pin()
        elif opcion == "2":
            ataque_fuerza_bruta()
        elif opcion == "3":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
