import re
from werkzeug.security import generate_password_hash, check_password_hash
from repository.usuario_repository import UsuarioRepository
from config.config import Config


class AuthService:
    """Servicio de autenticación"""
    
    @staticmethod
    def validar_email(email):
        """Validar formato de email"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    @staticmethod
    def validar_usuario(usuario):
        """Validar nombre de usuario"""
        # Mínimo 3 caracteres, máximo 20
        # Solo letras, números y guiones bajos
        patron = r'^[a-zA-Z0-9_]{3,20}$'
        return re.match(patron, usuario) is not None
    
    @staticmethod
    def validar_contraseña(contraseña):
        """Validar contraseña"""
        # Mínimo 6 caracteres
        return len(contraseña) >= 6
    
    @staticmethod
    def validar_registro(nombre, email, usuario, contraseña, confirmar_contraseña):
        """Validar datos de registro"""
        errores = []
        
        if not nombre or len(nombre.strip()) < 2:
            errores.append("El nombre debe tener al menos 2 caracteres")
        
        if not email:
            errores.append("El email es obligatorio")
        elif not AuthService.validar_email(email):
            errores.append("El email no es válido")
        elif UsuarioRepository.email_existe(email):
            errores.append("Este email ya está registrado")
        
        if not usuario:
            errores.append("El usuario es obligatorio")
        elif not AuthService.validar_usuario(usuario):
            errores.append("El usuario debe tener 3-20 caracteres (letras, números y _)")
        elif UsuarioRepository.usuario_existe(usuario):
            errores.append("Este usuario ya está registrado")
        
        if not contraseña:
            errores.append("La contraseña es obligatoria")
        elif not AuthService.validar_contraseña(contraseña):
            errores.append("La contraseña debe tener al menos 6 caracteres")
        
        if contraseña != confirmar_contraseña:
            errores.append("Las contraseñas no coinciden")
        
        return errores
    
    @staticmethod
    def registrar_usuario(nombre, email, usuario, contraseña, codigo_admin=''):
        """Registrar nuevo usuario"""
        errores = AuthService.validar_registro(
            nombre, email, usuario, contraseña, contraseña
        )
        
        if errores:
            return {'exito': False, 'errores': errores}
        
        # Determinar rol basado en código de administrador
        rol = 'usuario'
        if codigo_admin == Config.ADMIN_CODE:
            rol = 'admin'
        
        # Hash de contraseña
        contraseña_hash = generate_password_hash(contraseña)
        
        try:
            usuario_id = UsuarioRepository.crear_usuario(
                nombre, email, usuario, contraseña_hash, rol
            )
            if usuario_id:
                return {
                    'exito': True,
                    'mensaje': 'Usuario registrado exitosamente',
                    'usuario_id': usuario_id,
                    'rol': rol
                }
            else:
                return {
                    'exito': False,
                    'errores': ['Error al registrar el usuario']
                }
        except Exception as e:
            return {
                'exito': False,
                'errores': [str(e)]
            }
    
    @staticmethod
    def autenticar(usuario, contraseña):
        """Autenticar usuario"""
        if not usuario or not contraseña:
            return {'exito': False, 'mensaje': 'Usuario y contraseña son requeridos'}
        
        usuario_data = UsuarioRepository.obtener_usuario_por_usuario(usuario)
        
        if not usuario_data:
            return {'exito': False, 'mensaje': 'Usuario o contraseña incorrectos'}
        
        if not check_password_hash(usuario_data['contraseña'], contraseña):
            return {'exito': False, 'mensaje': 'Usuario o contraseña incorrectos'}
        
        return {
            'exito': True,
            'usuario_id': usuario_data['id'],
            'usuario': usuario_data['usuario'],
            'nombre': usuario_data['nombre'],
            'rol': usuario_data['rol']
        }
    
    @staticmethod
    def encriptar_contraseña(contraseña):
        """Encriptar contraseña"""
        return generate_password_hash(contraseña)
    
    @staticmethod
    def verificar_contraseña(contraseña, hash_contraseña):
        """Verificar contraseña contra su hash"""
        return check_password_hash(hash_contraseña, contraseña)
