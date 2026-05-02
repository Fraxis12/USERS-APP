-- Script SQL para crear la base de datos y tablas

-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS app_flask CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Usar la base de datos
USE app_flask;

-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    rol ENUM('admin', 'usuario') DEFAULT 'usuario',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_usuario (usuario),
    INDEX idx_email (email),
    INDEX idx_rol (rol)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Crear tabla de notas
CREATE TABLE IF NOT EXISTS notas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(200) NOT NULL,
    contenido LONGTEXT NOT NULL,
    usuario_id INT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    INDEX idx_usuario_id (usuario_id),
    INDEX idx_fecha_creacion (fecha_creacion)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insertar usuario admin por defecto (contraseña: password123)
-- Hash generado con werkzeug.security.generate_password_hash('password123')
INSERT INTO usuarios (nombre, email, usuario, contraseña, rol) VALUES
('Administrador', 'admin@example.com', 'admin', 'scrypt:32768:8:1$I7MqXGxLqAqYLuG6$a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6', 'admin'),
('Usuario Prueba', 'usuario@example.com', 'usuario', 'scrypt:32768:8:1$I7MqXGxLqAqYLuG6$a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6', 'usuario');

-- Insertar notas de ejemplo
INSERT INTO notas (titulo, contenido, usuario_id) VALUES
('Mi Primera Nota', 'Esta es una nota de ejemplo creada en la aplicación.', 1),
('Plan del Proyecto', 'Tareas pendientes para completar el proyecto de notas.', 1),
('Notas de Estudio', 'Apuntes importantes para repasar más tarde.', 2);

-- Ver tablas creadas
SHOW TABLES;
DESCRIBE usuarios;
DESCRIBE notas;
