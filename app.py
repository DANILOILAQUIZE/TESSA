from flask import Flask, send_file
from config import Config
from controller import FloresController

app = Flask(__name__)
flores_controller = FloresController()

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/flores', methods=['POST'])
def crear_flor():
    return flores_controller.crear_flor()

@app.route('/flores', methods=['GET'])
def listar_flores():
    return flores_controller.listar_flores()

@app.errorhandler(404)
def not_found(error):
    return {'error': 'Ruta no encontrada'}, 404

@app.errorhandler(500)
def internal_error(error):
    return {'error': 'Error interno del servidor'}, 500

if __name__ == '__main__':
    app.run(
        debug=(Config.FLASK_ENV == 'development'),
        host='0.0.0.0',
        port=Config.PORT
    )