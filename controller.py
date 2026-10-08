from flask import request, jsonify
from typing import Dict, Any
from database import FloresDB
from external_api import ExternalAPIService

class FloresController:
    def __init__(self):
        self.db = FloresDB()
        self.api_service = ExternalAPIService()
    
    def crear_flor(self) -> Dict[str, Any]:
        try:
            if not request.is_json:
                return {'error': 'Content-Type debe ser application/json'}, 400
            
            data = request.get_json()
            
            required_fields = ['nombre', 'color', 'precio_tallo']
            for field in required_fields:
                if field not in data:
                    return {'error': f'Campo {field} es requerido'}, 400
            
            if not isinstance(data['nombre'], str) or not data['nombre'].strip():
                return {'error': 'Nombre debe ser un string no vacío'}, 400
            
            if not isinstance(data['color'], str) or not data['color'].strip():
                return {'error': 'Color debe ser un string no vacío'}, 400
            
            try:
                precio_tallo = float(data['precio_tallo'])
                if precio_tallo <= 0:
                    return {'error': 'Precio tallo debe ser mayor a 0'}, 400
            except (ValueError, TypeError):
                return {'error': 'Precio tallo debe ser un número válido'}, 400
            
            self.db.create_flor(data['nombre'], data['color'], precio_tallo)
            
            return {'message': 'Flor creada exitosamente'}, 201
            
        except Exception as e:
            return {'error': f'Error interno del servidor: {str(e)}'}, 500
    
    def listar_flores(self) -> Dict[str, Any]:
        try:
            flores = self.db.get_all_flores()
            descripcion_agronomica = self.api_service.get_descripcion_agronomica()
            
            for flor in flores:
                flor['descripcion_agronomica'] = descripcion_agronomica
            
            return flores, 200
            
        except Exception as e:
            return {'error': f'Error interno del servidor: {str(e)}'}, 500