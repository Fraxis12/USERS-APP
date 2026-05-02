import os
import sys
from flask import Flask
from config.config import get_config
from config.database import DatabaseConnection
from routes.routes import registrar_rutas

def crear_app(config_name=None):
    """Factory para crear instancia de Flask"""
    
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__, template_folder='views/templates', static_folder='static')
    
    # Cargar configuración
    config = get_config(config_name)
    app.config.from_object(config)
    
    # Registrar rutas
    registrar_rutas(app)
    
    # Contexto de aplicación para la base de datos
    @app.before_request
    def before_request():
        pass
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        pass
    
    return app

if __name__ == '__main__':
    app = crear_app()
    
    # Verificar conexión a base de datos
    try:
        conexion = DatabaseConnection.get_connection()
        if conexion and conexion.is_connected():
            print("✓ Conexión a base de datos exitosa")
        else:
            print("✗ Error: No se pudo conectar a la base de datos")
            sys.exit(1)
    except Exception as e:
        print(f"✗ Error al conectar a la base de datos: {e}")
        sys.exit(1)
    
    # Ejecutar aplicación
    print("\n🚀 Iniciando aplicación...")
    print("📍 http://localhost:5000")
    print("💡 Presiona CTRL+C para detener\n")
    
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
        use_reloader=True
    )
