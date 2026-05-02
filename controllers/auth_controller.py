from flask import request, jsonify, session, redirect, url_for
from services.auth_service import AuthService


class AuthController:
    """Controlador de autenticación"""
    
    @staticmethod
    def registrar():
        """Manejar registro de usuario"""
        if request.method == 'POST':
            nombre = request.form.get('nombre', '').strip()
            email = request.form.get('email', '').strip()
            usuario = request.form.get('usuario', '').strip()
            contraseña = request.form.get('contraseña', '')
            confirmar_contraseña = request.form.get('confirmar_contraseña', '')
            codigo_admin = request.form.get('codigo_admin', '').strip()
            
            resultado = AuthService.registrar_usuario(
                nombre, email, usuario, contraseña, codigo_admin
            )
            
            return resultado
        
        return None
    
    @staticmethod
    def login():
        """Manejar login de usuario"""
        if request.method == 'POST':
            usuario = request.form.get('usuario', '').strip()
            contraseña = request.form.get('contraseña', '')
            
            resultado = AuthService.autenticar(usuario, contraseña)
            
            if resultado['exito']:
                session['usuario_id'] = resultado['usuario_id']
                session['usuario'] = resultado['usuario']
                session['nombre'] = resultado['nombre']
                session['rol'] = resultado['rol']
            
            return resultado
        
        return None
    
    @staticmethod
    def logout():
        """Cerrar sesión"""
        session.clear()
        return {'exito': True, 'mensaje': 'Sesión cerrada'}
