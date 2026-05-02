from config.database import DatabaseConnection
from models.nota import Nota
from datetime import datetime


class NotaRepository:
    """Repository para operaciones con notas en base de datos"""
    
    @staticmethod
    def crear_nota(titulo, contenido, usuario_id):
        """Crear una nueva nota"""
        query = """
            INSERT INTO notas (titulo, contenido, usuario_id, fecha_creacion)
            VALUES (%s, %s, %s, %s)
        """
        nota_id = DatabaseConnection.get_insert_id(
            query,
            (titulo, contenido, usuario_id, datetime.now())
        )
        return nota_id
    
    @staticmethod
    def obtener_nota_por_id(nota_id):
        """Obtener nota por ID"""
        query = "SELECT * FROM notas WHERE id = %s"
        resultado = DatabaseConnection.execute_query(query, (nota_id,))
        if resultado:
            return Nota.from_dict(resultado[0])
        return None
    
    @staticmethod
    def obtener_notas_usuario(usuario_id):
        """Obtener todas las notas de un usuario"""
        query = """
            SELECT * FROM notas 
            WHERE usuario_id = %s 
            ORDER BY fecha_creacion DESC
        """
        resultados = DatabaseConnection.execute_query(query, (usuario_id,))
        return [Nota.from_dict(nota) for nota in resultados]
    
    @staticmethod
    def obtener_todas_las_notas():
        """Obtener todas las notas"""
        query = "SELECT * FROM notas ORDER BY fecha_creacion DESC"
        resultados = DatabaseConnection.execute_query(query)
        return [Nota.from_dict(nota) for nota in resultados]
    
    @staticmethod
    def actualizar_nota(nota_id, titulo=None, contenido=None):
        """Actualizar nota"""
        campos = []
        parametros = []
        
        if titulo is not None:
            campos.append("titulo = %s")
            parametros.append(titulo)
        if contenido is not None:
            campos.append("contenido = %s")
            parametros.append(contenido)
        
        if not campos:
            return False
        
        parametros.append(nota_id)
        query = f"UPDATE notas SET {', '.join(campos)} WHERE id = %s"
        
        return DatabaseConnection.execute_insert_update_delete(query, tuple(parametros))
    
    @staticmethod
    def eliminar_nota(nota_id):
        """Eliminar nota"""
        query = "DELETE FROM notas WHERE id = %s"
        return DatabaseConnection.execute_insert_update_delete(query, (nota_id,))
    
    @staticmethod
    def contar_notas_usuario(usuario_id):
        """Contar notas de un usuario"""
        query = "SELECT COUNT(*) as total FROM notas WHERE usuario_id = %s"
        resultado = DatabaseConnection.execute_query(query, (usuario_id,))
        if resultado:
            return resultado[0]['total']
        return 0
    
    @staticmethod
    def obtener_nota_con_usuario(nota_id):
        """Obtener nota con información del usuario"""
        query = """
            SELECT n.*, u.nombre as usuario_nombre, u.usuario
            FROM notas n
            JOIN usuarios u ON n.usuario_id = u.id
            WHERE n.id = %s
        """
        resultado = DatabaseConnection.execute_query(query, (nota_id,))
        if resultado:
            return resultado[0]
        return None
