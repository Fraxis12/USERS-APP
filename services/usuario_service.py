from repository.usuario_repository import UsuarioRepository
from services.auth_service import AuthService
from werkzeug.security import generate_password_hash


class UsuarioService:
    """Servicio de lógica de negocio para usuarios"""
    
    @staticmethod
    def obtener_usuario(usuario_id):
        """Obtener usuario por ID"""
        return UsuarioRepository.obtener_usuario_por_id(usuario_id)
    
    @staticmethod
    def obtener_todos_usuarios():
        """Obtener todos los usuarios"""
        return UsuarioRepository.obtener_todos_los_usuarios()
    
    @staticmethod
    def crear_usuario(nombre, email, usuario, contraseña, rol='usuario'):
        """Crear nuevo usuario"""
        errores = []
        
        if not nombre or len(nombre.strip()) < 2:
            errores.append("El nombre debe tener al menos 2 caracteres")
        
        if not email or not AuthService.validar_email(email):
            errores.append("Email no válido")
        elif UsuarioRepository.email_existe(email):
            errores.append("Este email ya está registrado")
        
        if not usuario or not AuthService.validar_usuario(usuario):
            errores.append("Usuario no válido (3-20 caracteres, letras, números y _)")
        elif UsuarioRepository.usuario_existe(usuario):
            errores.append("Este usuario ya está registrado")
        
        if not contraseña or not AuthService.validar_contraseña(contraseña):
            errores.append("Contraseña debe tener al menos 6 caracteres")
        
        if rol not in ['admin', 'usuario']:
            errores.append("Rol no válido")
        
        if errores:
            return {'exito': False, 'errores': errores}
        
        contraseña_hash = generate_password_hash(contraseña)
        usuario_id = UsuarioRepository.crear_usuario(
            nombre, email, usuario, contraseña_hash, rol
        )
        
        if usuario_id:
            return {
                'exito': True,
                'mensaje': 'Usuario creado exitosamente',
                'usuario_id': usuario_id
            }
        else:
            return {
                'exito': False,
                'errores': ['Error al crear el usuario']
            }
    
    @staticmethod
    def actualizar_usuario(usuario_id, nombre=None, email=None, usuario=None, 
                          contraseña=None, rol=None):
        """Actualizar usuario"""
        errores = []
        
        usuario_existente = UsuarioRepository.obtener_usuario_por_id(usuario_id)
        if not usuario_existente:
            return {'exito': False, 'errores': ['Usuario no encontrado']}
        
        if nombre is not None and len(nombre.strip()) < 2:
            errores.append("El nombre debe tener al menos 2 caracteres")
        
        if email is not None:
            if not AuthService.validar_email(email):
                errores.append("Email no válido")
            else:
                usuario_con_email = UsuarioRepository.obtener_usuario_por_email(email)
                if usuario_con_email and usuario_con_email['id'] != usuario_id:
                    errores.append("Este email ya está registrado")
        
        if usuario is not None:
            if not AuthService.validar_usuario(usuario):
                errores.append("Usuario no válido (3-20 caracteres, letras, números y _)")
            else:
                usuario_data = UsuarioRepository.obtener_usuario_por_usuario(usuario)
                if usuario_data and usuario_data['id'] != usuario_id:
                    errores.append("Este usuario ya está registrado")
        
        if contraseña is not None and contraseña.strip():
            if not AuthService.validar_contraseña(contraseña):
                errores.append("Contraseña debe tener al menos 6 caracteres")
        
        if rol is not None and rol not in ['admin', 'usuario']:
            errores.append("Rol no válido")
        
        if errores:
            return {'exito': False, 'errores': errores}
        
        contraseña_hash = generate_password_hash(contraseña) if contraseña else None
        
        if UsuarioRepository.actualizar_usuario(
            usuario_id, nombre, email, usuario, contraseña_hash, rol
        ):
            return {
                'exito': True,
                'mensaje': 'Usuario actualizado exitosamente'
            }
        else:
            return {
                'exito': False,
                'errores': ['Error al actualizar el usuario']
            }
    
    @staticmethod
    def eliminar_usuario(usuario_id, usuario_actual_id):
        """Eliminar usuario"""
        if usuario_id == usuario_actual_id:
            return {
                'exito': False,
                'errores': ['No puedes eliminar tu propia cuenta']
            }
        
        usuario = UsuarioRepository.obtener_usuario_por_id(usuario_id)
        if not usuario:
            return {
                'exito': False,
                'errores': ['Usuario no encontrado']
            }
        
        if UsuarioRepository.eliminar_usuario(usuario_id):
            return {
                'exito': True,
                'mensaje': 'Usuario eliminado exitosamente'
            }
        else:
            return {
                'exito': False,
                'errores': ['Error al eliminar el usuario']
            }
    
    @staticmethod
    def cambiar_rol(usuario_id, nuevo_rol, usuario_actual_id):
        """Cambiar rol de un usuario"""
        if usuario_id == usuario_actual_id:
            return {
                'exito': False,
                'errores': ['No puedes cambiar tu propio rol']
            }
        
        if nuevo_rol not in ['admin', 'usuario']:
            return {
                'exito': False,
                'errores': ['Rol no válido']
            }
        
        usuario = UsuarioRepository.obtener_usuario_por_id(usuario_id)
        if not usuario:
            return {
                'exito': False,
                'errores': ['Usuario no encontrado']
            }
        
        if UsuarioRepository.actualizar_usuario(usuario_id, rol=nuevo_rol):
            return {
                'exito': True,
                'mensaje': f'Rol cambiado a {nuevo_rol}'
            }
        else:
            return {
                'exito': False,
                'errores': ['Error al cambiar el rol']
            }
