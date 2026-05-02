@echo off
REM Script de instalación para Windows

echo.
echo 🚀 Instalación de Aplicación de Notas - Flask MVC
echo ==================================================
echo.

REM Verificar Python
echo 📌 Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no está instalado o no está en el PATH
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version') do echo ✅ %%i
echo.

REM Crear entorno virtual
echo 📌 Creando entorno virtual...
if not exist venv (
    python -m venv venv
    echo ✅ Entorno virtual creado
) else (
    echo ✅ Entorno virtual ya existe
)
echo.

REM Activar entorno virtual
echo 📌 Activando entorno virtual...
call venv\Scripts\activate.bat
echo ✅ Entorno virtual activado
echo.

REM Instalar dependencias
echo 📌 Instalando dependencias...
pip install -q -r requirements.txt
echo ✅ Dependencias instaladas
echo.

echo ==================================================
echo ✅ ¡Instalación completada!
echo ==================================================
echo.
echo 📋 Próximos pasos:
echo 1. Editar config/config.py si necesitas cambiar configuración MySQL
echo 2. Ejecutar: venv\Scripts\activate.bat
echo 3. Crear base de datos:
echo    mysql -u root -p ^< database.sql
echo 4. Ejecutar: python app.py
echo 5. Abrir: http://localhost:5000
echo.
echo 🔐 Credenciales de prueba:
echo    Usuario: admin
echo    Contraseña: password123
echo.
pause
