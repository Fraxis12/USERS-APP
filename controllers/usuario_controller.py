from flask import request
from services.usuario_service import UsuarioService


class UsuarioController:
    """Controlador para manejo de usuarios"""
    
    @staticmethod
    def obtener_usuario(usuario_id):
        """Obtener usuario por ID"""
        usuario = UsuarioService.obtener_usuario(usuario_id)
        if usuario:
            return {'exito': True, 'usuario': usuario.to_dict()}
        return {'exito': False, 'mensaje': 'Usuario no encontrado'}
    
    @staticmethod
    def obtener_todos_usuarios():
        """Obtener todos los usuarios"""
        usuarios = UsuarioService.obtener_todos_usuarios()
        return {
            'exito': True,
            'usuarios': usuarios,
            'total': len(usuarios)
        }
    
    @staticmethod
    def crear_usuario():
        """Crear nuevo usuario"""
        if request.method == 'POST':
            nombre = request.form.get('nombre', '').strip()
            email = request.form.get('email', '').strip()
            usuario = request.form.get('usuario', '').strip()
            contraseña = request.form.get('contraseña', '')
            rol = request.form.get('rol', 'usuario')
            
            resultado = UsuarioService.crear_usuario(
                nombre, email, usuario, contraseña, rol
            )
            
            return resultado
        
        return {'exito': False, 'mensaje': 'Método no permitido'}
    
    @staticmethod
    def actualizar_usuario(usuario_id):
        """Actualizar usuario"""
        if request.method == 'POST':
            nombre = request.form.get('nombre')
            email = request.form.get('email')
            usuario = request.form.get('usuario')
            contraseña = request.form.get('contraseña', '').strip() or None
            rol = request.form.get('rol')
            
            resultado = UsuarioService.actualizar_usuario(
                usuario_id,
                nombre=nombre if nombre else None,
                email=email if email else None,
                usuario=usuario if usuario else None,
                contraseña=contraseña,
                rol=rol if rol else None
            )
            
            return resultado
        
        return {'exito': False, 'mensaje': 'Método no permitido'}
    
    @staticmethod
    def eliminar_usuario(usuario_id, usuario_actual_id):
        """Eliminar usuario"""
        resultado = UsuarioService.eliminar_usuario(usuario_id, usuario_actual_id)
        return resultado
    
    @staticmethod
    def cambiar_rol(usuario_id, usuario_actual_id):
        """Cambiar rol de usuario"""
        if request.method == 'POST':
            nuevo_rol = request.form.get('nuevo_rol')
            resultado = UsuarioService.cambiar_rol(usuario_id, nuevo_rol, usuario_actual_id)
            return resultado
        
        return {'exito': False, 'mensaje': 'Método no permitido'}
