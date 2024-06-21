from flask import Flask
from flask_cors import CORS
import logging
from api.usuario import usuario_bp
from api.checklist import checklist_bp
from api.maquinas import maquinas_bp 
from api.crear_maquinas import crear_maquinas_bp
from api.update_checklist import update_checklist_bp
from api.edit_checklist import edit_checklist_bp
from api.faenas import faenas_bp

app = Flask(__name__)

# Configuración de CORS para permitir solicitudes desde localhost:8100 y 127.0.0.1:5500
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:8100", "http://127.0.0.1:5500"]}})

# Configurar el registro básico
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Registrar los blueprints
app.register_blueprint(usuario_bp, url_prefix='/api')
app.register_blueprint(checklist_bp, url_prefix='/api')
app.register_blueprint(maquinas_bp, url_prefix='/api')
app.register_blueprint(crear_maquinas_bp, url_prefix='/api')
app.register_blueprint(update_checklist_bp, url_prefix='/api')
app.register_blueprint(edit_checklist_bp, url_prefix='/api')
app.register_blueprint(faenas_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True,port=5500)