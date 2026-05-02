# VERIFICACIÓN POST-INSTALACIÓN

Una vez que hayas instalado la aplicación, usa esta lista para verificar que todo está funcionando correctamente.

## ✅ Lista de Verificación

### 1. Base de Datos

```bash
# Conectarse a MySQL
mysql -u root -p

# Verificar base de datos
SHOW DATABASES;
USE app_flask;
SHOW TABLES;

# Verificar usuarios
SELECT * FROM usuarios;

# Verificar notas
SELECT * FROM notas;
```

**Esperado:**
- ✓ Base de datos `app_flask` existe
- ✓ Tabla `usuarios` tiene campos: id, nombre, email, usuario, contraseña, rol
- ✓ Tabla `notas` tiene campos: id, titulo, contenido, usuario_id, fecha_creacion
- ✓ Usuario `admin` existe
- ✓ Usuario `usuario` existe

### 2. Entorno Python

```bash
# Activar venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate.bat # Windows

# Verificar Python
python --version

# Verificar paquetes
pip list | grep -i flask
pip list | grep -i mysql
pip list | grep -i werkzeug
```

**Esperado:**
- ✓ Python 3.8 o superior
- ✓ Flask 2.3.2+
- ✓ mysql-connector-python 8.0.33+
- ✓ Werkzeug 2.3.6+

### 3. Estructura de Carpetas

```bash
# Verificar que existan todas las carpetas
ls -la  # Linux/Mac
# o
dir     # Windows
```

**Esperado:**
```
TAREA3/
├── app.py ........................ ✓
├── config/ ....................... ✓
├── models/ ....................... ✓
├── repository/ ................... ✓
├── services/ ..................... ✓
├── controllers/ .................. ✓
├── routes/ ....................... ✓
├── views/templates/ .............. ✓
├── static/ ....................... ✓
├── database.sql .................. ✓
├── requirements.txt .............. ✓
├── README.md ..................... ✓
├── QUICKSTART.md ................. ✓
└── manage_users.py ............... ✓
```

### 4. Archivo de Configuración

```bash
# Verificar config/config.py
cat config/config.py  # Linux/Mac
# o
type config\config.py  # Windows
```

**Esperado:**
- ✓ MYSQL_HOST = 'localhost'
- ✓ MYSQL_USER = 'root'
- ✓ MYSQL_DB = 'app_flask'
- ✓ ADMIN_CODE = '72168522'

### 5. Iniciar Aplicación

```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar aplicación
python app.py
```

**Esperado:**
```
✓ Conexión a base de datos exitosa
✓ 🚀 Iniciando aplicación...
✓ 📍 http://localhost:5000
✓ Sin errores en la consola
```

### 6. Pruebas en Navegador

Abre http://localhost:5000

#### Página de Login
- [ ] Se carga correctamente
- [ ] Campo usuario está enfocado
- [ ] Botón "Iniciar Sesión" es visible
- [ ] Link "Regístrate aquí" funciona

#### Login con Admin
```
Usuario: admin
Contraseña: password123
```
- [ ] Login exitoso
- [ ] Redirige a Panel Admin
- [ ] Ver navbar con usuario "admin"

#### Panel de Administrador
- [ ] Se muestran usuarios registrados
- [ ] Botón "+ Nuevo Usuario" visible
- [ ] Tabla con columnas: ID, Nombre, Usuario, Email, Rol, Acciones
- [ ] Botón "Editar" funciona
- [ ] Botón "Eliminar" funciona

#### Crear Nueva Nota
- [ ] Formulario se carga
- [ ] Campos título y contenido visibles
- [ ] Botón "Crear Nota" funciona
- [ ] Nota se guarda en base de datos

#### Mi Perfil
- [ ] Se muestran datos del usuario
- [ ] Se puede editar nombre, email, usuario
- [ ] Se puede cambiar contraseña
- [ ] Cambios se guardan

#### Notas
- [ ] Se listar todas las notas del usuario
- [ ] Botones Ver, Editar, Eliminar funcionan
- [ ] Se puede ver contenido completo

#### Cierre de Sesión
- [ ] Botón "Salir" funciona
- [ ] Redirige a página de login
- [ ] Sesión se cierra correctamente

## ⚠️ Solución de Problemas Comunes

### Error: "No se puede conectar a MySQL"
```bash
# Verificar que MySQL esté corriendo
# Linux
sudo systemctl status mysql

# Mac
brew services list

# Windows
# Buscar "Servicios" → MySQL
```

### Error 404 al ingresar URL
```
Verificar que:
- La aplicación está ejecutándose (python app.py)
- La ruta existe en routes/routes.py
- Estás usando localhost:5000, no localhost:80
```

### Sesión no se mantiene
```
Verificar que:
- SESSION_PERMANENT = False en config
- PERMANENT_SESSION_LIFETIME está configurado
- Cookies están habilitadas en navegador
```

### Contraseña no funciona
```bash
# Cambiar contraseña del usuario admin
python manage_users.py cambiar admin password123
```

### Base de datos vacía después de instalar
```bash
# Ejecutar script SQL nuevamente
mysql -u root -p < database.sql
```

## 🔧 Ajustes Personalizados

### Cambiar Puerto
En `app.py`:
```python
app.run(port=8000)  # Cambiar de 5000 a 8000
```

### Cambiar Base de Datos
En `config/config.py`:
```python
MYSQL_HOST = 'tu-servidor'
MYSQL_USER = 'tu-usuario'
MYSQL_PASSWORD = 'tu-contraseña'
MYSQL_DB = 'tu-base-de-datos'
```

### Cambiar Código Admin
En `config/config.py`:
```python
ADMIN_CODE = '123456789'  # Cambiar de 72168522
```

## 📊 Estadísticas Esperadas

Después de instalar con los datos de ejemplo:
- **Usuarios**: 2 (admin, usuario)
- **Notas**: 3 (del usuario admin)
- **Tablas**: 2 (usuarios, notas)

## ✨ Características Verificadas

- [x] Autenticación funciona
- [x] Registro funciona
- [x] Roles (admin/usuario) funciona
- [x] CRUD de notas funciona
- [x] CRUD de usuarios (admin) funciona
- [x] Interfaz responsive
- [x] Estilos modernos aplicados
- [x] Validación de formularios
- [x] Mensajes de error y éxito
- [x] Protección de rutas por rol
- [x] Base de datos MySQL conectada

## 📞 Próximos Pasos

Si todo está verde (✓):
1. Explorar la aplicación
2. Crear nuevos usuarios
3. Crear notas
4. Probar con usuario regular
5. Probar funciones de admin
6. Revisar código fuente para aprender

Si algo falla:
1. Revisar sección de troubleshooting
2. Verificar logs en consola
3. Revisar README.md
4. Verificar database.sql fue ejecutado

## 🎉 ¡Felicidades!

Si toda la lista de verificación está completa, tu aplicación está lista para usar.

---

**Versión**: 1.0
**Fecha**: Mayo 2026
