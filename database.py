import sqlite3
from typing import List, Dict, Optional
from config import Config

class FloresDB:
    def __init__(self):
        self.db_path = Config.DATABASE_URL
    
    def get_connection(self):
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            return conn
        except Exception as e:
            raise Exception(f"Error conectando a la base de datos: {str(e)}")
    
    def get_all_flores(self) -> List[Dict]:
        try:
            conn = self.get_connection()
            flores = conn.execute('SELECT * FROM VariedadFlor').fetchall()
            conn.close()
            
            return [dict(flor) for flor in flores]
        except Exception as e:
            raise Exception(f"Error obteniendo flores: {str(e)}")
    
    def create_flor(self, nombre: str, color: str, precio_tallo: float) -> bool:
        try:
            conn = self.get_connection()
            conn.execute(
                'INSERT INTO VariedadFlor (nombre, color, precio_tallo) VALUES (?, ?, ?)',
                (nombre, color, precio_tallo)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            raise Exception(f"Error creando flor: {str(e)}")