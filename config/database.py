import mysql.connector
from mysql.connector import Error
from config.config import Config


class DatabaseConnection:
    """Gestor de conexiones a MySQL"""
    
    _connection = None
    
    @staticmethod
    def get_connection():
        """Obtener conexión a la base de datos"""
        try:
            if DatabaseConnection._connection is None or not DatabaseConnection._connection.is_connected():
                DatabaseConnection._connection = mysql.connector.connect(
                    host=Config.MYSQL_HOST,
                    user=Config.MYSQL_USER,
                    password=Config.MYSQL_PASSWORD,
                    database=Config.MYSQL_DB,
                    port=Config.MYSQL_PORT,
                    autocommit=True,
                    use_unicode=True,
                    charset='utf8mb4'
                )
            return DatabaseConnection._connection
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
    
    @staticmethod
    def close_connection():
        """Cerrar conexión a la base de datos"""
        if DatabaseConnection._connection is not None and DatabaseConnection._connection.is_connected():
            DatabaseConnection._connection.close()
            DatabaseConnection._connection = None
    
    @staticmethod
    def execute_query(query, params=None):
        """Ejecutar una consulta SELECT"""
        connection = DatabaseConnection.get_connection()
        if connection is None:
            return []
        
        cursor = connection.cursor(dictionary=True)
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error ejecutando consulta: {e}")
            return []
        finally:
            cursor.close()
    
    @staticmethod
    def execute_insert_update_delete(query, params=None):
        """Ejecutar INSERT, UPDATE o DELETE"""
        connection = DatabaseConnection.get_connection()
        if connection is None:
            return False
        
        cursor = connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            connection.commit()
            return True
        except Error as e:
            print(f"Error ejecutando consulta: {e}")
            connection.rollback()
            return False
        finally:
            cursor.close()
    
    @staticmethod
    def get_insert_id(query, params=None):
        """Ejecutar INSERT y obtener el ID generado"""
        connection = DatabaseConnection.get_connection()
        if connection is None:
            return None
        
        cursor = connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error ejecutando consulta: {e}")
            connection.rollback()
            return None
        finally:
            cursor.close()
