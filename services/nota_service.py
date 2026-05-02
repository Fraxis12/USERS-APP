from repository.nota_repository import NotaRepository
from repository.usuario_repository import UsuarioRepository


class NotaService:
    """Servicio de lógica de negocio para notas"""
    
    @staticmethod
    def obtener_nota(nota_id):
        """Obtener nota por ID"""
        return NotaRepository.obtener_nota_con_usuario(nota_id)
    
    @staticmethod
    def obtener_notas_usuario(usuario_id):
        """Obtener todas las notas de un usuario"""
        return NotaRepository.obtener_notas_usuario(usuario_id)
    
    @staticmethod
    def obtener_todas_notas():
        """Obtener todas las notas (solo admin)"""
        query_notas = NotaRepository.obtener_todas_las_notas()
        resultados = []
        
        for nota in query_notas:
            usuario = UsuarioRepository.obtener_usuario_por_id(nota.usuario_id)
            resultados.append({
                'id': nota.id,
                'titulo': nota.titulo,
                'contenido': nota.contenido,
                'usuario_id': nota.usuario_id,
                'usuario_nombre': usuario.nombre if usuario else 'Desconocido',
                'fecha_creacion': nota.fecha_creacion
            })
        
        return resultados
    
    @staticmethod
    def crear_nota(titulo, contenido, usuario_id):
        """Crear nueva nota"""
        errores = []
        
        if not titulo or len(titulo.strip()) < 1:
            errores.append("El título es obligatorio")
        
        if not contenido or len(contenido.strip()) < 1:
            errores.append("El contenido es obligatorio")
        
        usuario = UsuarioRepository.obtener_usuario_por_id(usuario_id)
        if not usuario:
            errores.append("Usuario no encontrado")
        
        if errores:
            return {'exito': False, 'errores': errores}
        
        nota_id = NotaRepository.crear_nota(titulo, contenido, usuario_id)
        
        if nota_id:
            return {
                'exito': True,
                'mensaje': 'Nota creada exitosamente',
                'nota_id': nota_id
            }
        else:
            return {
                'exito': False,
                'errores': ['Error al crear la nota']
            }
    
    @staticmethod
    def actualizar_nota(nota_id, titulo=None, contenido=None, usuario_actual_id=None):
        """Actualizar nota"""
        nota = NotaRepository.obtener_nota_por_id(nota_id)
        
        if not nota:
            return {'exito': False, 'errores': ['Nota no encontrada']}
        
        # Verificar que el usuario sea el propietario (a menos que sea admin)
        if usuario_actual_id and nota.usuario_id != usuario_actual_id:
            return {
                'exito': False,
                'errores': ['No tienes permiso para editar esta nota']
            }
        
        errores = []
        
        if titulo is not None and len(titulo.strip()) < 1:
            errores.append("El título es obligatorio")
        
        if contenido is not None and len(contenido.strip()) < 1:
            errores.append("El contenido es obligatorio")
        
        if errores:
            return {'exito': False, 'errores': errores}
        
        if NotaRepository.actualizar_nota(nota_id, titulo, contenido):
            return {
                'exito': True,
                'mensaje': 'Nota actualizada exitosamente'
            }
        else:
            return {
                'exito': False,
                'errores': ['Error al actualizar la nota']
            }
    
    @staticmethod
    def eliminar_nota(nota_id, usuario_actual_id=None):
        """Eliminar nota"""
        nota = NotaRepository.obtener_nota_por_id(nota_id)
        
        if not nota:
            return {'exito': False, 'errores': ['Nota no encontrada']}
        
        # Verificar que el usuario sea el propietario (a menos que sea admin)
        if usuario_actual_id and nota.usuario_id != usuario_actual_id:
            return {
                'exito': False,
                'errores': ['No tienes permiso para eliminar esta nota']
            }
        
        if NotaRepository.eliminar_nota(nota_id):
            return {
                'exito': True,
                'mensaje': 'Nota eliminada exitosamente'
            }
        else:
            return {
                'exito': False,
                'errores': ['Error al eliminar la nota']
            }
