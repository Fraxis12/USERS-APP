#!/usr/bin/env python3
"""
Script para mostrar información del proyecto
Ejecutar: python info.py
"""

import os
import json
from pathlib import Path

def contar_lineas(archivo):
    """Contar líneas de código en un archivo"""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except:
        return 0

def mostrar_estadisticas():
    """Mostrar estadísticas del proyecto"""
    print("\n" + "="*70)
    print("📊 ESTADÍSTICAS DEL PROYECTO - APLICACIÓN DE NOTAS FLASK MVC")
    print("="*70 + "\n")
    
    # Contar archivos
    py_files = list(Path('.').rglob('*.py'))
    html_files = list(Path('.').rglob('*.html'))
    css_files = list(Path('.').rglob('*.css'))
    js_files = list(Path('.').rglob('*.js'))
    
    # Lineas de código
    total_py = sum(contar_lineas(f) for f in py_files)
    total_html = sum(contar_lineas(f) for f in html_files)
    total_css = sum(contar_lineas(f) for f in css_files)
    total_js = sum(contar_lineas(f) for f in js_files)
    
    print("📁 ARCHIVOS")
    print("-" * 70)
    print(f"  Python (.py)        : {len(py_files):3d} archivos  ({total_py:4d} líneas)")
    print(f"  HTML (.html)        : {len(html_files):3d} archivos  ({total_html:4d} líneas)")
    print(f"  CSS (.css)          : {len(css_files):3d} archivos  ({total_css:4d} líneas)")
    print(f"  JavaScript (.js)    : {len(js_files):3d} archivos  ({total_js:4d} líneas)")
    print()
    
    # Carpetas
    folders = {
        'config': 'Configuración',
        'models': 'Modelos de datos',
        'repository': 'Acceso a datos',
        'services': 'Lógica de negocio',
        'controllers': 'Controladores',
        'routes': 'Rutas y endpoints',
        'views': 'Plantillas HTML',
        'static': 'Archivos estáticos',
    }
    
    print("📂 CARPETAS")
    print("-" * 70)
    for folder, desc in folders.items():
        if os.path.exists(folder):
            files_count = len(list(Path(folder).rglob('*')))
            print(f"  {folder:20s} : {desc:30s} ({files_count} elementos)")
    print()
    
    # Documentación
    docs = ['README.md', 'QUICKSTART.md', 'VERIFICACION.md', 'TECNICO.md']
    print("📚 DOCUMENTACIÓN")
    print("-" * 70)
    for doc in docs:
        if os.path.exists(doc):
            lines = contar_lineas(doc)
            print(f"  ✓ {doc:25s} ({lines:4d} líneas)")
        else:
            print(f"  ✗ {doc:25s}")
    print()
    
    # Base de datos
    print("🗄️ BASE DE DATOS")
    print("-" * 70)
    print(f"  Base de datos       : app_flask")
    print(f"  Tablas              : usuarios, notas")
    print(f"  Motor               : MySQL 8.0+")
    print()
    
    # Totales
    total_archivos = len(py_files) + len(html_files) + len(css_files) + len(js_files)
    total_lineas = total_py + total_html + total_css + total_js
    
    print("📈 TOTALES")
    print("-" * 70)
    print(f"  Total archivos      : {total_archivos:4d}")
    print(f"  Total líneas        : {total_lineas:4d}")
    print()
    
    # Tecnologías
    print("🛠️ TECNOLOGÍAS")
    print("-" * 70)
    techs = [
        ('Backend', 'Flask 2.3.2'),
        ('Base de Datos', 'MySQL 8.0+'),
        ('ORM', 'MySQL Connector Python'),
        ('Seguridad', 'Werkzeug (bcrypt)'),
        ('Frontend', 'HTML5, CSS3, JavaScript'),
        ('Patrón', 'MVC'),
        ('Templating', 'Jinja2'),
    ]
    for tech, version in techs:
        print(f"  {tech:20s} : {version}")
    print()
    
    # Características
    print("✨ CARACTERÍSTICAS")
    print("-" * 70)
    features = [
        'Autenticación segura',
        'Sistema de roles (admin/usuario)',
        'CRUD de usuarios',
        'CRUD de notas',
        'Panel de administración',
        'Validación de formularios',
        'Interfaz moderna y responsive',
        'Sesiones seguras',
        'Encriptación de contraseñas',
        'Control de acceso basado en roles',
    ]
    for i, feature in enumerate(features, 1):
        print(f"  {i:2d}. {feature}")
    print()
    
    # URLs principales
    print("🌐 RUTAS PRINCIPALES")
    print("-" * 70)
    routes = [
        ('/auth/login', 'GET/POST', 'Iniciar sesión'),
        ('/auth/registro', 'GET/POST', 'Registrarse'),
        ('/dashboard', 'GET', 'Dashboard principal'),
        ('/usuario/panel-admin', 'GET', 'Panel de admin'),
        ('/usuario/crear', 'GET/POST', 'Crear usuario'),
        ('/usuario/editar/<id>', 'GET/POST', 'Editar usuario'),
        ('/nota/mis-notas', 'GET', 'Ver mis notas'),
        ('/nota/crear', 'GET/POST', 'Crear nota'),
        ('/nota/editar/<id>', 'GET/POST', 'Editar nota'),
    ]
    for route, method, desc in routes:
        print(f"  {route:30s} [{method:9s}] {desc}")
    print()
    
    print("="*70)
    print("🚀 Para empezar: ejecuta 'python app.py' y abre http://localhost:5000")
    print("📖 Más info: lee README.md o QUICKSTART.md")
    print("="*70 + "\n")

def mostrar_estructura():
    """Mostrar estructura de carpetas"""
    print("\n" + "="*70)
    print("📁 ESTRUCTURA DEL PROYECTO")
    print("="*70 + "\n")
    
    estructura = """
TAREA3/
├── 🐍 Python Backend
│   ├── app.py                          ← Archivo principal
│   ├── manage_users.py                 ← Gestión de usuarios
│   ├── requirements.txt                ← Dependencias
│   ├── database.sql                    ← Script SQL
│   │
│   ├── 🔧 config/
│   │   ├── __init__.py
│   │   ├── config.py                  ← Configuración
│   │   └── database.py                ← Conexión MySQL
│   │
│   ├── 🎯 models/
│   │   ├── __init__.py
│   │   ├── user.py                    ← Modelo Usuario
│   │   └── nota.py                    ← Modelo Nota
│   │
│   ├── 💾 repository/
│   │   ├── __init__.py
│   │   ├── usuario_repository.py      ← Queries usuario
│   │   └── nota_repository.py         ← Queries nota
│   │
│   ├── ⚙️ services/
│   │   ├── __init__.py
│   │   ├── auth_service.py            ← Lógica autenticación
│   │   ├── usuario_service.py         ← Lógica usuario
│   │   └── nota_service.py            ← Lógica nota
│   │
│   ├── 🎮 controllers/
│   │   ├── __init__.py
│   │   ├── auth_controller.py         ← Control autenticación
│   │   ├── usuario_controller.py      ← Control usuario
│   │   └── nota_controller.py         ← Control nota
│   │
│   └── 🛣️ routes/
│       ├── __init__.py
│       └── routes.py                  ← Todas las rutas
│
├── 🎨 Frontend
│   ├── views/templates/
│   │   ├── base.html                  ← Template base
│   │   ├── dashboard.html             ← Dashboard
│   │   ├── acceso_denegado.html       ← Error 403
│   │   │
│   │   ├── auth/
│   │   │   ├── login.html             ← Login
│   │   │   └── registro.html          ← Registro
│   │   │
│   │   ├── admin/
│   │   │   ├── panel_admin.html       ← Panel admin
│   │   │   ├── crear_usuario.html     ← Crear usuario
│   │   │   ├── editar_usuario.html    ← Editar usuario
│   │   │   └── todas_notas.html       ← Ver todas notas
│   │   │
│   │   ├── usuario/
│   │   │   └── mi_perfil.html         ← Mi perfil
│   │   │
│   │   └── notas/
│   │       ├── mis_notas.html         ← Mis notas
│   │       ├── crear_nota.html        ← Crear nota
│   │       ├── editar_nota.html       ← Editar nota
│   │       └── ver_nota.html          ← Ver nota
│   │
│   └── static/
│       ├── css/
│       │   └── style.css              ← Estilos (2500+ líneas)
│       └── js/
│           └── main.js                ← JavaScript funcional
│
└── 📚 Documentación
    ├── README.md                      ← Documentación completa
    ├── QUICKSTART.md                  ← Guía rápida
    ├── VERIFICACION.md                ← Checklist
    ├── TECNICO.md                     ← Referencia técnica
    ├── .env.example                   ← Variables de entorno
    ├── setup.sh                       ← Instalación (Linux/Mac)
    ├── setup.bat                      ← Instalación (Windows)
    └── .gitignore                     ← Git ignore
    """
    
    print(estructura)
    print("="*70 + "\n")

if __name__ == '__main__':
    mostrar_estructura()
    mostrar_estadisticas()
    
    print("\n💡 TIPS:")
    print("  • Ejecutar: python app.py")
    print("  • Navegar a: http://localhost:5000")
    print("  • Usuario: admin / password123")
    print("  • Ver logs en consola para errores")
    print()
