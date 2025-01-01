from pyicloud import PyiCloudService

def localizar_icloud():
    # Solicitar credenciales de iCloud
    icloud_email = input("Introduce tu correo de iCloud: ")
    icloud_password = input("Introduce tu contraseña de iCloud: ")

    try:
        # Autenticar al usuario
        icloud = PyiCloudService(icloud_email, icloud_password)

        if icloud.requires_2fa:
            print("Se requiere autenticación de dos factores.")
            code = input("Introduce el código enviado a tus dispositivos de confianza: ")
            result = icloud.validate_2fa_code(code)

            if not result:
                print("Código incorrecto. Inténtalo de nuevo.")
                return

        # Obtener dispositivos asociados a la cuenta
        devices = icloud.find_my_iphone
        print("\nDispositivos disponibles:")

        for index, device in enumerate(devices):
            print(f"{index + 1}. {device['name']} - {device['status']}")

        # Seleccionar un dispositivo
        seleccion = int(input("\nSelecciona el número del dispositivo que deseas localizar: ")) - 1
        if seleccion < 0 or seleccion >= len(devices):
            print("Selección no válida.")
            return

        dispositivo = devices[seleccion]
        ubicacion = dispositivo.location

        if ubicacion:
            print("\nUbicación del dispositivo:")
            print(f"Latitud: {ubicacion['latitude']}")
            print(f"Longitud: {ubicacion['longitude']}")
        else:
            print("\nNo se pudo obtener la ubicación del dispositivo. Puede estar apagado o sin conexión.")

    except Exception as e:
        print(f"Error al intentar localizar el dispositivo: {e}")
