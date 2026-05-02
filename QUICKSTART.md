# 🚀 GUÍA RÁPIDA DE INICIO

## Instalación Rápida (Linux/Mac)

```bash
# 1. Navegar a la carpeta del proyecto
cd /ruta/al/proyecto

# 2. Ejecutar script de instalación
chmod +x setup.sh
./setup.sh

# 3. Crear base de datos
mysql -u root -p < database.sql

# 4. Activar entorno virtual
source venv/bin/activate

# 5. Ejecutar aplicación
python app.py
```

## Instalación Rápida (Windows)

```cmd
# 1. Navegar a la carpeta del proyecto
cd C:\ruta\al\proyecto

# 2. Ejecutar script de instalación
setup.bat

# 3. Crear base de datos
mysql -u root -p < database.sql

# 4. Activar entorno virtual
venv\Scripts\activate.bat

# 5. Ejecutar aplicación
python app.py
```

## Acceder a la Aplicación

- URL: http://localhost:5000
- Usuario Demo: `admin` / `password123`
- Usuario Regular: `usuario` / `password123`

## Código de Administrador

Si deseas registrarte como administrador:
- Código: `72168522`
- Ubicación: Campo "Código de Administrador" en el formulario de registro

## Estructura del Proyecto

```
TAREA3/
├── app.py ............................ Archivo principal
├── database.sql ...................... Script SQL
├── requirements.txt .................. Dependencias
├── README.md ......................... Documentación completa
├── QUICKSTART.md ..................... Este archivo
│
├── config/ ........................... Configuración
├── models/ ........................... Modelos de datos
├── repository/ ....................... Acceso a datos
├── services/ ......................... Lógica de negocio
├── controllers/ ...................... Controladores
├── routes/ ........................... Rutas
├── views/templates/ .................. Plantillas HTML
└── static/ ........................... CSS, JS, etc
```

## Troubleshooting

### ❌ Error: "No se puede conectar a MySQL"
```bash
# Verificar que MySQL esté corriendo
mysql -u root -p

# Si te pide contraseña, presiona Enter si está vacía
# En Windows, busca MySQL en servicios
```

### ❌ Error: "No module named flask"
```bash
# Instalar dependencias
pip install -r requirements.txt
```

### ❌ Error: "Base de datos no existe"
```bash
# Crear base de datos
mysql -u root -p < database.sql
```

### ❌ Puerto 5000 en uso
```bash
# Cambiar puerto en app.py
app.run(port=5001)
```

## Cambiar Configuración MySQL

Edita `config/config.py`:

```python
MYSQL_HOST = 'localhost'      # Servidor MySQL
MYSQL_USER = 'root'            # Usuario MySQL
MYSQL_PASSWORD = ''            # Contraseña (vacío por defecto)
MYSQL_DB = 'app_flask'         # Nombre de base de datos
MYSQL_PORT = 3306              # Puerto MySQL
```

## Comandos Útiles

```bash
# Activar entorno
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate.bat # Windows

# Desactivar entorno
deactivate

# Instalar paquete
pip install nombre-paquete

# Ver paquetes instalados
pip list

# Ejecutar aplicación
python app.py

# Ejecutar en puerto específico
FLASK_PORT=8000 python app.py
```

## Rutas Principales

- `/` - Redirige a dashboard
- `/auth/login` - Iniciar sesión
- `/auth/registro` - Registrarse
- `/dashboard` - Dashboard principal
- `/usuario/panel-admin` - Panel de administración
- `/usuario/mi-perfil` - Mi perfil
- `/nota/mis-notas` - Mis notas
- `/nota/crear` - Crear nota
- `/nota/editar/1` - Editar nota
- `/nota/ver/1` - Ver nota

## Usuarios de Prueba

**Administrador:**
- Usuario: `admin`
- Contraseña: `password123`

**Usuario Regular:**
- Usuario: `usuario`
- Contraseña: `password123`

## Siguiente: Ver README.md para documentación completa

Para más detalles sobre arquitectura, seguridad, despliegue y más,
lee el archivo README.md
