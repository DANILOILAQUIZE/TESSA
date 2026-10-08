import requests
from typing import Optional
from config import Config

class ExternalAPIService:
    def __init__(self):
        self.api_url = Config.EXTERNAL_API_URL
    
    def get_descripcion_agronomica(self) -> str:
        try:
            response = requests.get(self.api_url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                return data.get('body', 'Información no disponible')
            else:
                return "Información no disponible"
        except requests.RequestException as e:
            print(f"Error consultando API externa: {str(e)}")
            return "Información no disponible"
        except Exception as e:
            print(f"Error inesperado en API externa: {str(e)}")
            return "Información no disponible"