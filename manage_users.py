#!/usr/bin/env python3
"""
Script para generar y actualizar contraseñas encriptadas
Útil para crear usuarios de prueba en la base de datos
"""

import sys
import mysql.connector
from werkzeug.security import generate_password_hash

def generar_contraseña(contraseña):
    """Generar hash de contraseña"""
    return generate_password_hash(contraseña)

def actualizar_contraseña_usuario(usuario, nueva_contraseña, 
                                  host='localhost', user='root', 
                                  password='', database='app_flask'):
    """Actualizar contraseña de un usuario en la base de datos"""
    try:
        conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conexion.cursor()
        
        # Generar hash
        hash_contraseña = generate_password_hash(nueva_contraseña)
        
        # Actualizar base de datos
        query = "UPDATE usuarios SET contraseña = %s WHERE usuario = %s"
        cursor.execute(query, (hash_contraseña, usuario))
        conexion.commit()
        
        if cursor.rowcount > 0:
            print(f"✅ Contraseña actualizada para usuario: {usuario}")
            return True
        else:
            print(f"❌ Usuario no encontrado: {usuario}")
            return False
            
    except mysql.connector.Error as e:
        print(f"❌ Error de base de datos: {e}")
        return False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def crear_usuario_prueba(nombre, email, usuario, contraseña, rol='usuario',
                         host='localhost', user='root', 
                         password='', database='app_flask'):
    """Crear nuevo usuario de prueba en la base de datos"""
    try:
        conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conexion.cursor()
        
        # Generar hash
        hash_contraseña = generate_password_hash(contraseña)
        
        # Insertar usuario
        query = """INSERT INTO usuarios (nombre, email, usuario, contraseña, rol) 
                   VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (nombre, email, usuario, hash_contraseña, rol))
        conexion.commit()
        
        usuario_id = cursor.lastrowid
        print(f"✅ Usuario creado exitosamente")
        print(f"   ID: {usuario_id}")
        print(f"   Nombre: {nombre}")
        print(f"   Usuario: {usuario}")
        print(f"   Email: {email}")
        print(f"   Rol: {rol}")
        return True
        
    except mysql.connector.Error as e:
        if "Duplicate entry" in str(e):
            print(f"❌ Usuario o email ya existe")
        else:
            print(f"❌ Error de base de datos: {e}")
        return False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

if __name__ == '__main__':
    print("🔐 Herramienta de Gestión de Contraseñas")
    print("=" * 50)
    print()
    
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python manage_users.py generar <contraseña>")
        print("      - Genera el hash de una contraseña")
        print()
        print("  python manage_users.py cambiar <usuario> <nueva_contraseña>")
        print("      - Cambia la contraseña de un usuario existente")
        print()
        print("  python manage_users.py crear <nombre> <email> <usuario> <contraseña> [rol]")
        print("      - Crea un nuevo usuario (rol por defecto: usuario)")
        print()
        print("Ejemplos:")
        print("  python manage_users.py generar 123456")
        print("  python manage_users.py cambiar admin nuevacontraseña")
        print("  python manage_users.py crear 'Juan Pérez' juan@example.com juan 123456")
        print("  python manage_users.py crear 'Admin Test' admin2@example.com admin2 123456 admin")
        sys.exit(1)
    
    comando = sys.argv[1].lower()
    
    if comando == 'generar':
        if len(sys.argv) < 3:
            print("❌ Debes proporcionar una contraseña")
            sys.exit(1)
        
        contraseña = sys.argv[2]
        hash_contraseña = generar_contraseña(contraseña)
        print(f"Contraseña: {contraseña}")
        print(f"Hash: {hash_contraseña}")
        print()
        print("Usa este hash en tu base de datos:")
        print(f"UPDATE usuarios SET contraseña = '{hash_contraseña}' WHERE usuario = 'usuario_name';")
        
    elif comando == 'cambiar':
        if len(sys.argv) < 4:
            print("❌ Debes proporcionar usuario y nueva contraseña")
            sys.exit(1)
        
        usuario = sys.argv[2]
        nueva_contraseña = sys.argv[3]
        actualizar_contraseña_usuario(usuario, nueva_contraseña)
        
    elif comando == 'crear':
        if len(sys.argv) < 6:
            print("❌ Debes proporcionar: nombre, email, usuario, contraseña")
            sys.exit(1)
        
        nombre = sys.argv[2]
        email = sys.argv[3]
        usuario = sys.argv[4]
        contraseña = sys.argv[5]
        rol = sys.argv[6] if len(sys.argv) > 6 else 'usuario'
        
        crear_usuario_prueba(nombre, email, usuario, contraseña, rol)
        
    else:
        print(f"❌ Comando desconocido: {comando}")
        sys.exit(1)
