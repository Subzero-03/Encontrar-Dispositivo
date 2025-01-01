from google.oauth2 import service_account
from googleapiclient.discovery import build

def localizar_google():
    # Ruta al archivo de credenciales JSON
    credentials_path = input("Introduce la ruta al archivo de credenciales JSON de Google: ")

    try:
        # Autenticar con el archivo de credenciales
        credentials = service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=["https://www.googleapis.com/auth/geolocation"]
        )

        service = build("geolocation", "v1", credentials=credentials)

        # Solicitar datos de geolocalización (simulado)
        print("\nObteniendo ubicación...")
        body = {
            "considerIp": "true"  # Esto puede ajustarse dependiendo de la API
        }
        response = service.geolocate().geolocation().post(body=body).execute()

        # Mostrar la ubicación
        location = response.get("location")
        if location:
            print("\nUbicación del dispositivo:")
            print(f"Latitud: {location['lat']}")
            print(f"Longitud: {location['lng']}")
        else:
            print("\nNo se pudo obtener la ubicación.")

    except FileNotFoundError:
        print("\nEl archivo de credenciales no fue encontrado. Verifica la ruta e inténtalo nuevamente.")
    except Exception as e:
        print(f"Error al intentar localizar el dispositivo con Google: {e}")
