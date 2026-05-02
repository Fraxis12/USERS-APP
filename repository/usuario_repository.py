from config.database import DatabaseConnection
from models.user import Usuario


class UsuarioRepository:
    """Repository para operaciones con usuarios en base de datos"""
    
    @staticmethod
    def crear_usuario(nombre, email, usuario, contraseña_hash, rol='usuario'):
        """Crear un nuevo usuario"""
        query = """
            INSERT INTO usuarios (nombre, email, usuario, contraseña, rol)
            VALUES (%s, %s, %s, %s, %s)
        """
        usuario_id = DatabaseConnection.get_insert_id(
            query, 
            (nombre, email, usuario, contraseña_hash, rol)
        )
        return usuario_id
    
    @staticmethod
    def obtener_usuario_por_id(usuario_id):
        """Obtener usuario por ID"""
        query = "SELECT * FROM usuarios WHERE id = %s"
        resultado = DatabaseConnection.execute_query(query, (usuario_id,))
        if resultado:
            return Usuario.from_dict(resultado[0])
        return None
    
    @staticmethod
    def obtener_usuario_por_usuario(usuario):
        """Obtener usuario por nombre de usuario"""
        query = "SELECT * FROM usuarios WHERE usuario = %s"
        resultado = DatabaseConnection.execute_query(query, (usuario,))
        if resultado:
            return resultado[0]
        return None
    
    @staticmethod
    def obtener_usuario_por_email(email):
        """Obtener usuario por email"""
        query = "SELECT * FROM usuarios WHERE email = %s"
        resultado = DatabaseConnection.execute_query(query, (email,))
        if resultado:
            return resultado[0]
        return None
    
    @staticmethod
    def obtener_todos_los_usuarios():
        """Obtener todos los usuarios"""
        query = "SELECT id, nombre, email, usuario, rol FROM usuarios ORDER BY id DESC"
        return DatabaseConnection.execute_query(query)
    
    @staticmethod
    def actualizar_usuario(usuario_id, nombre=None, email=None, usuario=None, 
                          contraseña_hash=None, rol=None):
        """Actualizar datos de usuario"""
        campos = []
        parametros = []
        
        if nombre is not None:
            campos.append("nombre = %s")
            parametros.append(nombre)
        if email is not None:
            campos.append("email = %s")
            parametros.append(email)
        if usuario is not None:
            campos.append("usuario = %s")
            parametros.append(usuario)
        if contraseña_hash is not None:
            campos.append("contraseña = %s")
            parametros.append(contraseña_hash)
        if rol is not None:
            campos.append("rol = %s")
            parametros.append(rol)
        
        if not campos:
            return False
        
        parametros.append(usuario_id)
        query = f"UPDATE usuarios SET {', '.join(campos)} WHERE id = %s"
        
        return DatabaseConnection.execute_insert_update_delete(query, tuple(parametros))
    
    @staticmethod
    def eliminar_usuario(usuario_id):
        """Eliminar usuario"""
        # Primero eliminar sus notas
        query_notas = "DELETE FROM notas WHERE usuario_id = %s"
        DatabaseConnection.execute_insert_update_delete(query_notas, (usuario_id,))
        
        # Luego eliminar el usuario
        query = "DELETE FROM usuarios WHERE id = %s"
        return DatabaseConnection.execute_insert_update_delete(query, (usuario_id,))
    
    @staticmethod
    def usuario_existe(usuario):
        """Verificar si un usuario existe"""
        query = "SELECT id FROM usuarios WHERE usuario = %s"
        resultado = DatabaseConnection.execute_query(query, (usuario,))
        return len(resultado) > 0
    
    @staticmethod
    def email_existe(email):
        """Verificar si un email existe"""
        query = "SELECT id FROM usuarios WHERE email = %s"
        resultado = DatabaseConnection.execute_query(query, (email,))
        return len(resultado) > 0
    
    @staticmethod
    def contar_usuarios():
        """Contar total de usuarios"""
        query = "SELECT COUNT(*) as total FROM usuarios"
        resultado = DatabaseConnection.execute_query(query)
        if resultado:
            return resultado[0]['total']
        return 0
