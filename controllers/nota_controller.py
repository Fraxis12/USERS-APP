from flask import request
from services.nota_service import NotaService


class NotaController:
    """Controlador para manejo de notas"""
    
    @staticmethod
    def obtener_nota(nota_id):
        """Obtener nota por ID"""
        nota = NotaService.obtener_nota(nota_id)
        if nota:
            return {'exito': True, 'nota': nota}
        return {'exito': False, 'mensaje': 'Nota no encontrada'}
    
    @staticmethod
    def obtener_notas_usuario(usuario_id):
        """Obtener notas de un usuario"""
        notas = NotaService.obtener_notas_usuario(usuario_id)
        return {
            'exito': True,
            'notas': [nota.to_dict() for nota in notas],
            'total': len(notas)
        }
    
    @staticmethod
    def obtener_todas_notas():
        """Obtener todas las notas (solo admin)"""
        notas = NotaService.obtener_todas_notas()
        return {
            'exito': True,
            'notas': notas,
            'total': len(notas)
        }
    
    @staticmethod
    def crear_nota(usuario_id):
        """Crear nueva nota"""
        if request.method == 'POST':
            titulo = request.form.get('titulo', '').strip()
            contenido = request.form.get('contenido', '').strip()
            
            resultado = NotaService.crear_nota(titulo, contenido, usuario_id)
            
            return resultado
        
        return {'exito': False, 'mensaje': 'Método no permitido'}
    
    @staticmethod
    def actualizar_nota(nota_id, usuario_actual_id=None):
        """Actualizar nota"""
        if request.method == 'POST':
            titulo = request.form.get('titulo', '').strip()
            contenido = request.form.get('contenido', '').strip()
            
            resultado = NotaService.actualizar_nota(
                nota_id,
                titulo=titulo if titulo else None,
                contenido=contenido if contenido else None,
                usuario_actual_id=usuario_actual_id
            )
            
            return resultado
        
        return {'exito': False, 'mensaje': 'Método no permitido'}
    
    @staticmethod
    def eliminar_nota(nota_id, usuario_actual_id=None):
        """Eliminar nota"""
        resultado = NotaService.eliminar_nota(nota_id, usuario_actual_id)
        return resultado
