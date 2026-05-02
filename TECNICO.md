# REFERENCIA TÉCNICA

Documentación técnica completa de la aplicación Flask MVC.

## 📋 Índice de Contenidos

1. [Estructura MVC](#estructura-mvc)
2. [Flujo de Datos](#flujo-de-datos)
3. [Documentación de Clases](#documentación-de-clases)
4. [Documentación de Métodos](#documentación-de-métodos)
5. [Variables de Sesión](#variables-de-sesión)
6. [Códigos de Error](#códigos-de-error)
7. [Validaciones](#validaciones)

---

## Estructura MVC

### Arquitectura General

```
Navegador (HTTP)
    ↓
Routes (flask blueprints)
    ↓
Controllers (lógica de control)
    ↓
Services (lógica de negocio)
    ↓
Repository (acceso a datos)
    ↓
Database (MySQL)
    ↓
Models (representación)
    ↓
Vistas (HTML/Jinja2)
```

### Capas

#### 1. Routes (routes/routes.py)
- Define URLs y mapeo a controladores
- Gestiona autenticación y autorización
- Maneja decoradores `@login_requerido` y `@admin_requerido`
- Blueprints: auth_bp, usuario_bp, nota_bp, main_bp

#### 2. Controllers
- Reciben requests HTTP
- Validan entrada del usuario
- Llaman a services
- Retornan respuestas

**Archivos:**
- `controllers/auth_controller.py` - Autenticación
- `controllers/usuario_controller.py` - Usuarios
- `controllers/nota_controller.py` - Notas

#### 3. Services
- Contienen lógica de negocio
- Validan datos
- Llaman a repositories
- Retornan resultados

**Archivos:**
- `services/auth_service.py` - Lógica de autenticación
- `services/usuario_service.py` - Lógica de usuarios
- `services/nota_service.py` - Lógica de notas

#### 4. Repository
- Acceso directo a base de datos
- Queries SQL
- CRUD operations
- Sin lógica de negocio

**Archivos:**
- `repository/usuario_repository.py` - Queries de usuario
- `repository/nota_repository.py` - Queries de nota

#### 5. Models
- Representan entidades
- Métodos de conversión
- Propiedades

**Archivos:**
- `models/user.py` - Usuario
- `models/nota.py` - Nota

---

## Flujo de Datos

### Ejemplo: Crear Nueva Nota

```
1. Usuario llena formulario en /nota/crear
   ↓
2. POST a /nota/crear
   ↓
3. routes.py → crear_nota() route handler
   ↓
4. NotaController.crear_nota(usuario_id)
   ↓
5. NotaService.crear_nota(titulo, contenido, usuario_id)
   - Valida campos
   - Verifica usuario existe
   ↓
6. NotaRepository.crear_nota(...)
   - Inserta en base de datos
   - Retorna ID
   ↓
7. Retorna al template
   ↓
8. Usuario ve confirmación
```

### Ejemplo: Login

```
1. Usuario ingresa credenciales
   ↓
2. POST a /auth/login
   ↓
3. routes.py → login() route handler
   ↓
4. AuthController.login()
   ↓
5. AuthService.autenticar(usuario, contraseña)
   - Busca usuario en base de datos
   - Verifica contraseña con hash
   ↓
6. Si correcto:
   - Crea sesión session['usuario_id'] = ...
   - Redirige al dashboard
   ↓
7. Si incorrecto:
   - Muestra mensaje de error
   - Vuelve a formulario
```

---

## Documentación de Clases

### Clase Usuario (models/user.py)

```python
class Usuario:
    """Representa un usuario del sistema"""
    
    def __init__(self, id=None, nombre=None, email=None, 
                 usuario=None, contraseña=None, rol='usuario'):
        self.id              # int - Identificador único
        self.nombre          # str - Nombre completo
        self.email           # str - Email único
        self.usuario         # str - Username único
        self.contraseña      # str - Password (hash)
        self.rol             # str - 'admin' o 'usuario'
```

**Métodos:**
- `to_dict()` → Retorna diccionario
- `from_dict(data)` → Crea Usuario desde diccionario (static)

---

### Clase Nota (models/nota.py)

```python
class Nota:
    """Representa una nota del usuario"""
    
    def __init__(self, id=None, titulo=None, contenido=None, 
                 usuario_id=None, fecha_creacion=None):
        self.id              # int - Identificador único
        self.titulo          # str - Título
        self.contenido       # str - Contenido
        self.usuario_id      # int - FK a usuarios.id
        self.fecha_creacion  # datetime - Timestamp creación
```

**Métodos:**
- `to_dict()` → Retorna diccionario
- `from_dict(data)` → Crea Nota desde diccionario (static)

---

## Documentación de Métodos

### UsuarioRepository

```python
# Crear usuario
usuario_id = UsuarioRepository.crear_usuario(
    nombre, email, usuario, contraseña_hash, rol
)

# Obtener por ID
usuario = UsuarioRepository.obtener_usuario_por_id(usuario_id)

# Obtener por nombre de usuario
usuario_data = UsuarioRepository.obtener_usuario_por_usuario(usuario)

# Obtener por email
usuario_data = UsuarioRepository.obtener_usuario_por_email(email)

# Obtener todos
usuarios = UsuarioRepository.obtener_todos_los_usuarios()

# Actualizar
exito = UsuarioRepository.actualizar_usuario(
    usuario_id, nombre, email, usuario, contraseña_hash, rol
)

# Eliminar (y sus notas)
exito = UsuarioRepository.eliminar_usuario(usuario_id)

# Verificar si existe
existe = UsuarioRepository.usuario_existe(usuario)
existe = UsuarioRepository.email_existe(email)

# Contar
total = UsuarioRepository.contar_usuarios()
```

### NotaRepository

```python
# Crear nota
nota_id = NotaRepository.crear_nota(titulo, contenido, usuario_id)

# Obtener por ID
nota = NotaRepository.obtener_nota_por_id(nota_id)

# Obtener notas de usuario
notas = NotaRepository.obtener_notas_usuario(usuario_id)

# Obtener todas
notas = NotaRepository.obtener_todas_las_notas()

# Actualizar
exito = NotaRepository.actualizar_nota(nota_id, titulo, contenido)

# Eliminar
exito = NotaRepository.eliminar_nota(nota_id)

# Contar
total = NotaRepository.contar_notas_usuario(usuario_id)

# Con info de usuario
nota_con_usuario = NotaRepository.obtener_nota_con_usuario(nota_id)
```

### AuthService

```python
# Registrar usuario
resultado = AuthService.registrar_usuario(
    nombre, email, usuario, contraseña, codigo_admin
)
# Retorna: {'exito': bool, 'usuario_id': int, 'rol': str}

# Autenticar
resultado = AuthService.autenticar(usuario, contraseña)
# Retorna: {'exito': bool, 'usuario_id': int, 'usuario': str, ...}

# Validaciones
valido = AuthService.validar_email(email)
valido = AuthService.validar_usuario(usuario)
valido = AuthService.validar_contraseña(contraseña)
errores = AuthService.validar_registro(nombre, email, usuario, pwd, pwd_conf)

# Encriptación
hash = AuthService.encriptar_contraseña(contraseña)
correcto = AuthService.verificar_contraseña(contraseña, hash)
```

### UsuarioService

```python
# Obtener
usuario = UsuarioService.obtener_usuario(usuario_id)
usuarios = UsuarioService.obtener_todos_usuarios()

# Crear
resultado = UsuarioService.crear_usuario(nombre, email, usuario, contraseña, rol)

# Actualizar
resultado = UsuarioService.actualizar_usuario(usuario_id, nombre, email, ...)

# Eliminar (con protección)
resultado = UsuarioService.eliminar_usuario(usuario_id, usuario_actual_id)

# Cambiar rol (con protección)
resultado = UsuarioService.cambiar_rol(usuario_id, nuevo_rol, usuario_actual_id)
```

### NotaService

```python
# Obtener
nota = NotaService.obtener_nota(nota_id)
notas = NotaService.obtener_notas_usuario(usuario_id)
notas = NotaService.obtener_todas_notas()

# Crear
resultado = NotaService.crear_nota(titulo, contenido, usuario_id)

# Actualizar (con validación de permisos)
resultado = NotaService.actualizar_nota(nota_id, titulo, contenido, usuario_actual_id)

# Eliminar (con validación de permisos)
resultado = NotaService.eliminar_nota(nota_id, usuario_actual_id)
```

---

## Variables de Sesión

### Durante Login

Cuando un usuario inicia sesión, se establecen:

```python
session['usuario_id']    # int - ID del usuario
session['usuario']       # str - Username
session['nombre']        # str - Nombre completo
session['rol']          # str - 'admin' o 'usuario'
```

### Uso en Templates

```html
{{ session.get('nombre') }}      <!-- Nombre del usuario -->
{{ session.get('rol') }}          <!-- admin o usuario -->
{{ session.get('usuario_id') }}   <!-- ID del usuario -->
```

### Uso en Python

```python
from flask import session

usuario_id = session.get('usuario_id')
rol = session.get('rol')
es_admin = session.get('rol') == 'admin'
```

---

## Códigos de Error

### Respuestas de Servicios

Todos los servicios retornan diccionarios con estructura:

```python
{
    'exito': True/False,
    'mensaje': 'Descripción',
    'errores': ['error1', 'error2'],
    'usuario_id': int,
    'nota_id': int,
    # ... otros campos según contexto
}
```

### Códigos HTTP

- `200` - OK - Operación exitosa
- `302` - REDIRECT - Redireccionamiento
- `400` - BAD REQUEST - Datos inválidos
- `403` - FORBIDDEN - No tienes permisos
- `404` - NOT FOUND - No existe
- `500` - SERVER ERROR - Error del servidor

---

## Validaciones

### Email

```python
# Patrón
r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Ejemplos válidos
- usuario@ejemplo.com
- nombre.apellido@empresa.co
- user+tag@dominio.org
```

### Usuario

```python
# Patrón
r'^[a-zA-Z0-9_]{3,20}$'

# Requisitos
- Mínimo 3 caracteres
- Máximo 20 caracteres
- Solo letras, números y guiones bajos
- Único en base de datos

# Ejemplos válidos
- admin
- usuario_123
- juan_perez
```

### Contraseña

```python
# Requisitos
- Mínimo 6 caracteres
- Se encripta con Werkzeug (bcrypt)
- Nunca se almacena en texto plano
- Se valida con check_password_hash()
```

### Nombre

```python
# Requisitos
- Mínimo 2 caracteres
- No puede estar vacío
- Puede contener espacios
- Ejemplos: "Juan Pérez", "María García"
```

### Rol

```python
# Valores válidos
- 'admin' - Administrador con permisos completos
- 'usuario' - Usuario regular con permisos limitados
```

---

## Flujos de Control

### Flujo de Autenticación

```
┌─ Usuario no autenticado
│  ↓
├─ Accede a ruta protegida
│  ↓
├─ @login_requerido verifica sesión
│  ↓
├─ Si no hay sesión → Redirige a /auth/login
│  ↓
├─ Si hay sesión → Continúa
│
└─ Usuario autenticado con sesión válida
```

### Flujo de Autorización

```
┌─ Usuario autenticado (rol = usuario)
│  ↓
├─ Accede a ruta protegida (admin)
│  ↓
├─ @admin_requerido verifica rol
│  ↓
├─ Si rol ≠ 'admin' → Redirige a /acceso-denegado
│  ↓
└─ Si rol = 'admin' → Continúa
```

### Protección de Notas

```
┌─ Usuario quiere editar nota
│  ↓
├─ Verificar permisos:
│  ├─ Si admin → Permitir
│  └─ Si usuario_id != propietario → Denegar
│  ↓
└─ Si permitido → Proceder
```

---

## Configuración del Sistema

### Ambiente de Desarrollo

```python
DEBUG = True
TESTING = False
SESSION_PERMANENT = False
SESSION_COOKIE_SECURE = False
```

### Ambiente de Producción

```python
DEBUG = False
TESTING = False
SESSION_PERMANENT = True
SESSION_COOKIE_SECURE = True  # Requiere HTTPS
SESSION_COOKIE_HTTPONLY = True
```

---

## Comandos Útiles

### Gestión de Usuarios

```bash
# Generar hash de contraseña
python manage_users.py generar password123

# Cambiar contraseña de usuario existente
python manage_users.py cambiar admin newpassword

# Crear nuevo usuario
python manage_users.py crear "Nombre" email@test.com username password

# Crear usuario admin
python manage_users.py crear "Admin" admin2@test.com admin2 password123 admin
```

### Base de Datos

```bash
# Ver estructura
mysql -u root -p -e "DESCRIBE app_flask.usuarios;"

# Backup
mysqldump -u root -p app_flask > backup.sql

# Restaurar
mysql -u root -p app_flask < backup.sql

# Vaciar tabla (destructivo)
mysql -u root -p -e "TRUNCATE app_flask.usuarios;"
```

---

## Notas de Desarrollo

### Extender el Sistema

#### Agregar Nueva Entidad

1. Crear modelo en `models/entidad.py`
2. Crear repository en `repository/entidad_repository.py`
3. Crear service en `services/entidad_service.py`
4. Crear controller en `controllers/entidad_controller.py`
5. Agregar rutas en `routes/routes.py`
6. Crear templates en `views/templates/`

#### Agregar Nueva Validación

```python
# En services/entidad_service.py

@staticmethod
def validar_campo(valor):
    """Validar campo específico"""
    if not valor:
        return False
    if len(valor) < 3:
        return False
    # más validaciones...
    return True
```

#### Agregar Nuevo Rol

1. En base de datos, modificar enum en tabla usuarios
2. Agregar nuevas funciones de verificación
3. Crear nuevas rutas con decoradores apropiados

---

## Performance

### Índices en Base de Datos

```sql
-- Usuarios
INDEX idx_usuario (usuario)         -- Para búsquedas rápidas
INDEX idx_email (email)             -- Para búsquedas por email
INDEX idx_rol (rol)                 -- Para filtrar por rol

-- Notas
INDEX idx_usuario_id (usuario_id)   -- Para notas del usuario
INDEX idx_fecha_creacion (fecha_creacion)  -- Para ordenar
```

### Optimizaciones Recomendadas

1. Cacheo de sesiones
2. Paginación de notas grandes
3. Queries optimizadas
4. Compresión de respuestas
5. Minificación de CSS/JS

---

**Versión**: 1.0
**Última actualización**: Mayo 2026
