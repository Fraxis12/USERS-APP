# 📝 Aplicación de Notas - Flask MVC

Una aplicación web moderna y profesional para gestionar notas personales con sistema de autenticación, roles de usuario (admin/usuario) y CRUD completo.

## 🌟 Características Principales

- ✅ **Sistema de Autenticación** - Login/Registro seguro con contraseñas encriptadas
- ✅ **Roles de Usuario** - Administrador y Usuario con permisos diferenciados
- ✅ **Código de Administrador** - Acceso exclusivo con código `72168522`
- ✅ **CRUD de Usuarios** - Crear, leer, editar, eliminar usuarios (solo admin)
- ✅ **CRUD de Notas** - Crear, editar, eliminar notas personales
- ✅ **Panel de Admin** - Dashboard con gestión completa de usuarios
- ✅ **Interfaz Moderna** - Diseño limpio, minimalista y responsivo
- ✅ **Base de Datos MySQL** - Almacenamiento persistente de datos

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3.8+, Flask 2.3.2
- **Base de Datos**: MySQL 8.0+
- **ORM/Queries**: MySQL Connector Python
- **Seguridad**: Werkzeug (password hashing)
- **Frontend**: HTML5, CSS3, JavaScript Vanilla
- **Patrón**: Arquitectura MVC

## 📁 Estructura del Proyecto

```
TAREA3/
├── app.py                          # Archivo principal
├── requirements.txt                # Dependencias Python
├── database.sql                    # Script SQL
├── README.md                       # Este archivo
│
├── config/                         # Configuración
│   ├── __init__.py
│   ├── config.py                  # Variables de entorno
│   └── database.py                # Conexión MySQL
│
├── models/                         # Modelos de datos
│   ├── __init__.py
│   ├── user.py                    # Modelo Usuario
│   └── nota.py                    # Modelo Nota
│
├── repository/                     # Acceso a datos
│   ├── __init__.py
│   ├── usuario_repository.py      # Queries de usuario
│   └── nota_repository.py         # Queries de nota
│
├── services/                       # Lógica de negocio
│   ├── __init__.py
│   ├── auth_service.py            # Autenticación
│   ├── usuario_service.py         # Lógica de usuarios
│   └── nota_service.py            # Lógica de notas
│
├── controllers/                    # Controladores
│   ├── __init__.py
│   ├── auth_controller.py         # Control de auth
│   ├── usuario_controller.py      # Control de usuarios
│   └── nota_controller.py         # Control de notas
│
├── routes/                         # Definición de rutas
│   ├── __init__.py
│   └── routes.py                  # Todas las rutas
│
├── views/
│   └── templates/                 # Plantillas Jinja2
│       ├── base.html              # Template base
│       ├── dashboard.html         # Dashboard principal
│       ├── acceso_denegado.html   # Página 403
│       ├── auth/
│       │   ├── login.html
│       │   └── registro.html
│       ├── admin/
│       │   ├── panel_admin.html
│       │   ├── crear_usuario.html
│       │   ├── editar_usuario.html
│       │   └── todas_notas.html
│       ├── usuario/
│       │   └── mi_perfil.html
│       └── notas/
│           ├── mis_notas.html
│           ├── crear_nota.html
│           ├── editar_nota.html
│           └── ver_nota.html
│
└── static/                        # Archivos estáticos
    ├── css/
    │   └── style.css              # Estilos CSS
    └── js/
        └── main.js                # JavaScript
```

## 🚀 Requisitos Previos

- **Python 3.8+** instalado
- **MySQL Server 8.0+** en ejecución
- **pip** (gestor de paquetes Python)

### Verificar Python:
```bash
python --version
# o
python3 --version
```

### Verificar MySQL:
```bash
mysql --version
```

## 📦 Instalación

### 1. Clonar o descargar el proyecto

```bash
cd /ruta/al/proyecto
```

### 2. Crear entorno virtual

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos

#### Opción A: Usando script SQL
```bash
# Linux/Mac
mysql -u root -p < database.sql

# Windows (asegúrate de estar en la carpeta del proyecto)
mysql -u root -p < database.sql
```

#### Opción B: Manualmente
```bash
# Conectarse a MySQL
mysql -u root -p

# Ejecutar los comandos del archivo database.sql
CREATE DATABASE IF NOT EXISTS app_flask CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'flask_user'@'localhost' IDENTIFIED BY '123456';

GRANT ALL PRIVILEGES ON app_flask.* TO 'flask_user'@'localhost';

FLUSH PRIVILEGES;

EXIT;
# ... (copiar el contenido de database.sql)
```

### 5. Configurar variables de entorno

Edita `config/config.py` si es necesario:

```python
# Valores por defecto (si MySQL está en localhost)
MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
MYSQL_USER = os.environ.get('MYSQL_USER') or 'flask_user'
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or '123456'
MYSQL_DB = os.environ.get('MYSQL_DB') or 'app_flask'
MYSQL_PORT = int(os.environ.get('MYSQL_PORT') or 3306)
```

### 6. Ejecutar la aplicación

```bash
python app.py
```

La aplicación estará disponible en: **http://localhost:5000**

## 🔐 Credenciales de Acceso

### Usuario Admin (por defecto):
- **Usuario**: `admin`
- **Contraseña**: `password123`
- **Rol**: Administrador

### Usuario Regular (por defecto):
- **Usuario**: `usuario`
- **Contraseña**: `password123`
- **Rol**: Usuario

### Código de Administrador:
- **Código**: `72168522`
- **Ubicación**: Formulario de registro
- Si lo ingresas al registrarte, te registrarás como admin

## 📋 Guía de Uso

### Para Usuarios Regulares

1. **Registrarse**: Crear nueva cuenta en `/auth/registro`
2. **Login**: Iniciar sesión con tu usuario
3. **Dashboard**: Ver panel principal con opciones
4. **Mis Notas**: Ver, crear, editar y eliminar tus notas
5. **Mi Perfil**: Actualizar información personal y contraseña

### Para Administradores

Además de funciones de usuario regular:

1. **Panel Admin**: Gestión completa de usuarios
2. **Crear Usuario**: Agregar nuevos usuarios manualmente
3. **Editar Usuario**: Modificar datos y cambiar roles
4. **Eliminar Usuario**: Remover usuarios (no permite autoeliminación)
5. **Ver Todas las Notas**: Visualizar notas de todos los usuarios

## 🏗️ Arquitectura MVC

### Models
- **Usuario**: Representa entidad usuario con propiedades
- **Nota**: Representa entidad nota con propiedades
- Métodos para convertir a/desde diccionarios

### Repository (Acceso a Datos)
- **UsuarioRepository**: Todas las queries de usuarios
  - `crear_usuario()`, `obtener_usuario_por_id()`, `obtener_todos_los_usuarios()`
  - `actualizar_usuario()`, `eliminar_usuario()`, etc.
- **NotaRepository**: Todas las queries de notas
  - `crear_nota()`, `obtener_nota_por_id()`, `obtener_notas_usuario()`
  - `actualizar_nota()`, `eliminar_nota()`, etc.

### Services (Lógica de Negocio)
- **AuthService**: Autenticación y registro
  - Validación de datos
  - Hash de contraseñas
  - Autenticación de usuarios
- **UsuarioService**: Lógica de usuarios
  - CRUD con validaciones
  - Prevención de autoeliminación
  - Cambio de roles
- **NotaService**: Lógica de notas
  - CRUD de notas
  - Control de permisos

### Controllers (Controladores)
- **AuthController**: Manejo de login/registro
- **UsuarioController**: Manejo de operaciones usuario
- **NotaController**: Manejo de operaciones nota

### Routes (Rutas)
- Definición de todas las rutas HTTP
- Decoradores para autenticación
- Decoradores para verificar roles (admin)

### Views (Plantillas)
- Templates HTML con Jinja2
- Base template reutilizable
- Plantillas organizadas por sección

## 🔒 Seguridad

- ✅ **Contraseñas encriptadas** con Werkzeug (bcrypt/scrypt)
- ✅ **Validación de sesiones** en todas las rutas
- ✅ **Protección de rutas** según rol de usuario
- ✅ **Prevención de autoeliminación** de usuarios
- ✅ **Validación de formularios** en cliente y servidor
- ✅ **Validación de emails** con regex
- ✅ **Validación de usernames** (3-20 caracteres)
- ✅ **Control de acceso** a notas de otros usuarios

## 🎨 Diseño UI/UX

### Características de Diseño:
- **Minimalista**: Interfaz limpia sin elementos innecesarios
- **Moderno**: Inspirado en X/Twitter, Linear, Notion
- **Responsivo**: Funciona en desktop, tablet y móvil
- **Tipografía**: Sistema Font Stack moderno
- **Colores**: Paleta profesional de 8 colores principales
- **Espaciado**: Sistema consistente de espacios
- **Sombras**: Jerarquía visual con diferentes niveles
- **Transiciones**: Animaciones suaves y profesionales

### Componentes:
- Cards con hover effects
- Botones con estados (hover, active, disabled)
- Tablas responsivas
- Formularios bien diseñados
- Alertas visuales (success, danger, warning, info)
- Modales de confirmación
- Badges para roles
- Grid layout automático

## 📋 Tabla de Usuarios

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INT | Identificador único |
| nombre | VARCHAR(100) | Nombre completo |
| email | VARCHAR(100) | Email único |
| usuario | VARCHAR(50) | Username único |
| contraseña | VARCHAR(255) | Password encriptada |
| rol | ENUM | 'admin' o 'usuario' |
| fecha_creacion | TIMESTAMP | Fecha de registro |
| fecha_actualizacion | TIMESTAMP | Última actualización |

## 📋 Tabla de Notas

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INT | Identificador único |
| titulo | VARCHAR(200) | Título de la nota |
| contenido | LONGTEXT | Contenido de la nota |
| usuario_id | INT | FK a usuarios.id |
| fecha_creacion | TIMESTAMP | Fecha de creación |
| fecha_actualizacion | TIMESTAMP | Última actualización |

## 🐛 Troubleshooting

### Error: "No se puede conectar a MySQL"
```
Soluciones:
1. Verificar que MySQL esté corriendo
2. Verificar credenciales en config/config.py
3. Verificar que la base de datos exista
4. Ejecutar: mysql -u root -p < database.sql
```

### Error: "No module named 'flask'"
```
Solución: Instalar dependencias
pip install -r requirements.txt
```

### Las notas no se cargan
```
Soluciones:
1. Verificar conexión a base de datos
2. Verificar que exista la tabla de notas
3. Revisar logs en la consola
```

### No puedo editar mi usuario
```
Nota: Los cambios de rol deben hacerlos otros admins
Para cambiar tu contraseña, usa "Mi Perfil"
```

## 📝 Variables de Configuración

En `config/config.py`:

```python
# Flask
SECRET_KEY = 'your-secret-key-change-in-production'
SESSION_PERMANENT = False
PERMANENT_SESSION_LIFETIME = timedelta(hours=24)

# MySQL
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DB = 'app_flask'
MYSQL_PORT = 3306

# Código admin
ADMIN_CODE = '72168522'

# Sesión
SESSION_COOKIE_SECURE = False  # True en producción
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
```

## 🚀 Despliegue en Producción

### Cambios recomendados:

1. **Cambiar SECRET_KEY**:
```python
import os
SECRET_KEY = os.urandom(24)
```

2. **Usar HTTPS**:
```python
SESSION_COOKIE_SECURE = True
```

3. **Usar WSGI (Gunicorn)**:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:crear_app()
```

4. **Variables de entorno**:
```bash
export FLASK_ENV=production
export MYSQL_HOST=tu-servidor-db
export MYSQL_USER=usuario
export MYSQL_PASSWORD=contraseña
```

5. **Base de datos remota**:
Actualizar `config/config.py` con datos del servidor

## 📚 Endpoints API

### Autenticación
- `GET/POST /auth/login` - Iniciar sesión
- `GET/POST /auth/registro` - Registrarse
- `GET /auth/logout` - Cerrar sesión

### Usuario (Admin)
- `GET /usuario/panel-admin` - Panel de admin
- `GET/POST /usuario/crear` - Crear usuario
- `GET/POST /usuario/editar/<id>` - Editar usuario
- `POST /usuario/eliminar/<id>` - Eliminar usuario
- `POST /usuario/cambiar-rol/<id>` - Cambiar rol
- `GET /usuario/mi-perfil` - Ver perfil
- `POST /usuario/actualizar-perfil` - Actualizar perfil

### Notas
- `GET /nota/mis-notas` - Ver mis notas
- `GET /nota/todas` - Ver todas las notas (admin)
- `GET/POST /nota/crear` - Crear nota
- `GET/POST /nota/editar/<id>` - Editar nota
- `GET /nota/ver/<id>` - Ver nota
- `POST /nota/eliminar/<id>` - Eliminar nota

### Principal
- `GET /` - Redirige a login o dashboard
- `GET /dashboard` - Dashboard principal
- `GET /acceso-denegado` - Error 403

## 📞 Soporte

Si encuentras problemas:
1. Revisa los logs en la consola
2. Verifica la conexión a MySQL
3. Comprueba las credenciales
4. Ejecuta nuevamente el script SQL

## 📜 Licencia

Proyecto educativo de ejemplo. Úsalo libremente.

---

**Creado con ❤️ para el curso ICC Semana 6**

**Última actualización**: Mayo 2026
