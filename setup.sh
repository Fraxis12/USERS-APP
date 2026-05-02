#!/bin/bash

# Script de instalación y configuración rápida
# Para sistemas Linux/Mac

echo "🚀 Instalación de Aplicación de Notas - Flask MVC"
echo "=================================================="
echo ""

# Verificar Python
echo "📌 Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado. Por favor, instálalo primero."
    exit 1
fi
echo "✅ Python encontrado: $(python3 --version)"
echo ""

# Crear entorno virtual
echo "📌 Creando entorno virtual..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Entorno virtual creado"
else
    echo "✅ Entorno virtual ya existe"
fi
echo ""

# Activar entorno virtual
echo "📌 Activando entorno virtual..."
source venv/bin/activate
echo "✅ Entorno virtual activado"
echo ""

# Instalar dependencias
echo "📌 Instalando dependencias..."
pip install -q -r requirements.txt
echo "✅ Dependencias instaladas"
echo ""

# Verificar MySQL
echo "📌 Verificando MySQL..."
if ! command -v mysql &> /dev/null; then
    echo "⚠️  MySQL no está instalado o no está en el PATH"
    echo "   Por favor, instálalo manualmente: https://dev.mysql.com/downloads/"
    echo ""
else
    echo "✅ MySQL encontrado: $(mysql --version)"
    echo ""
    
    # Preguntar si crear base de datos
    read -p "¿Deseas crear la base de datos ahora? (s/n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        echo "📌 Creando base de datos..."
        mysql -u root -p < database.sql
        echo "✅ Base de datos creada"
    fi
fi

echo ""
echo "=================================================="
echo "✅ ¡Instalación completada!"
echo "=================================================="
echo ""
echo "📋 Próximos pasos:"
echo "1. Editar config/config.py si necesitas cambiar configuración MySQL"
echo "2. Ejecutar: source venv/bin/activate"
echo "3. Ejecutar: python app.py"
echo "4. Abrir: http://localhost:5000"
echo ""
echo "🔐 Credenciales de prueba:"
echo "   Usuario: admin"
echo "   Contraseña: password123"
echo ""
