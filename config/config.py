import os
from datetime import timedelta

class Config:
    """Configuración base de la aplicación"""
    
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-change-in-production'
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
# Base de datos MySQL
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'flask_user'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or '123456'
    MYSQL_DB = os.environ.get('MYSQL_DB') or 'app_flask'
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT') or 3306)
    # Código de administrador
    ADMIN_CODE = '72168522'
    
    # Configuración de sesión
    SESSION_COOKIE_SECURE = False  # Cambiar a True en producción con HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'


class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True


class TestingConfig(Config):
    """Configuración para pruebas"""
    DEBUG = True
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(env=None):
    """Obtener configuración según el ambiente"""
    if env is None:
        env = os.environ.get('FLASK_ENV', 'development')
    return config.get(env, config['default'])
