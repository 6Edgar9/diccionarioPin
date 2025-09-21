import itertools

def pedir_datos():
    """Solicita datos personales para generar un diccionario de PINs más completo."""
    print("\n🔍 Introduce los datos personales para generar el diccionario de PINs:")

    datos = {
        "nacimiento": input("📆 Año de nacimiento (Ej: 1998): ").strip(),
        "mes_dia_nac": input("📆 Mes y día de nacimiento (MMDD - Ej: 0523): ").strip(),
        "aniversario": input("💍 Fecha de aniversario (MMDD o YYYY): ").strip(),
        "matricula_auto": input("🚗 Últimos 4 dígitos de la matrícula del auto: ").strip(),
        "telefono": input("📞 Últimos 4 dígitos del número de teléfono: ").strip(),
        "dni": input("🆔 Últimos 4 dígitos del DNI/Cédula/Pasaporte: ").strip(),
        "casa": input("🏠 Número de casa o apartamento: ").strip(),
        "codigo_postal": input("📮 Código postal: ").strip(),
        "codigo_tarjeta": input("💳 Últimos 4 dígitos de una tarjeta bancaria: ").strip(),
        "numeros_favoritos": input("🔢 Números favoritos (separados por coma): ").strip().split(","),
        "extra": input("🔠 Otros números importantes (separados por coma): ").strip().split(","),
    }

    return datos

def generar_variaciones(datos):
    """Genera variaciones comunes con los datos ingresados."""
    combinaciones = set()

    for key, value in datos.items():
        if isinstance(value, list):
            combinaciones.update([num.strip() for num in value if num.strip()])
        elif value:
            combinaciones.add(value)

    patrones = [
        "{dato}", "{dato}123", "{dato}000", "{dato}111", "{dato}999",
        "{dato}2024", "123{dato}", "000{dato}", "{dato}{dato}", "{dato}78", "{dato}56",
        "{dato}9999", "{dato}1122", "{dato}2000", "88{dato}88", "00{dato}00"
    ]

    for dato in list(combinaciones):
        for patron in patrones:
            combinaciones.add(patron.format(dato=dato))

    return combinaciones

def generar_pins(nombre_archivo="diccionario_pins"):
    """Genera y guarda un diccionario de PINs con información personalizada."""
    
    datos_usuario = pedir_datos()
    combinaciones_usuario = generar_variaciones(datos_usuario)

    file_count = 1
    max_size = 50_000_000
    total_pins = 0

    with open(f"{nombre_archivo}_{file_count}.txt", "w", encoding="utf-8") as file:
        pines_comunes = [
            "0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999",
            "1234", "4321", "5678", "8765", "000000", "111111", "222222", "999999",
            "123456", "654321", "123123", "321321", "00000000", "11111111", "99999999",
            "2580", "0852", "159753", "753159", "101010", "121212",
            "1999", "2000", "2023", "2024", "6969", "8888", "2002", "2010",
            "0101", "0202", "0303", "0404", "0505", "0606", "0707", "0808", "0909",
            "1122", "1212", "1313", "1414", "1515", "1616", "1717", "1818", "1919"
        ]
        
        for pin in pines_comunes:
            file.write(pin + "\n")
            total_pins += 1

        for pin in combinaciones_usuario:
            file.write(pin + "\n")
            total_pins += 1

        for longitud in range(4, 9):  # Desde 4 hasta 8 dígitos
            for pin in itertools.product("0123456789", repeat=longitud):
                pin_str = "".join(pin)
                file.write(pin_str + "\n")
                total_pins += 1

                if file.tell() > max_size:
                    file.close()
                    file_count += 1
                    file = open(f"{nombre_archivo}_{file_count}.txt", "w", encoding="utf-8")

    print(f"✅ Diccionario de PINs guardado en {file_count} archivos con un total de {total_pins} combinaciones.")

def main():
    print("\n📲 Generador de diccionario de PINs para ataques de fuerza bruta en celulares")
    generar_pins()

if __name__ == "__main__":
    main()
