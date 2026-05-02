from datetime import datetime


class Nota:
    """Modelo para Nota"""
    
    def __init__(self, id=None, titulo=None, contenido=None, usuario_id=None, 
                 fecha_creacion=None):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.usuario_id = usuario_id
        self.fecha_creacion = fecha_creacion or datetime.now()
    
    def to_dict(self):
        """Convertir modelo a diccionario"""
        return {
            'id': self.id,
            'titulo': self.titulo,
            'contenido': self.contenido,
            'usuario_id': self.usuario_id,
            'fecha_creacion': self.fecha_creacion
        }
    
    @staticmethod
    def from_dict(data):
        """Crear modelo desde diccionario"""
        return Nota(
            id=data.get('id'),
            titulo=data.get('titulo'),
            contenido=data.get('contenido'),
            usuario_id=data.get('usuario_id'),
            fecha_creacion=data.get('fecha_creacion')
        )
