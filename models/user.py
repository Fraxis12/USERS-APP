class Usuario:
    """Modelo para Usuario"""
    
    def __init__(self, id=None, nombre=None, email=None, usuario=None, 
                 contraseña=None, rol='usuario'):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.usuario = usuario
        self.contraseña = contraseña
        self.rol = rol
    
    def to_dict(self):
        """Convertir modelo a diccionario"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'usuario': self.usuario,
            'rol': self.rol
        }
    
    @staticmethod
    def from_dict(data):
        """Crear modelo desde diccionario"""
        return Usuario(
            id=data.get('id'),
            nombre=data.get('nombre'),
            email=data.get('email'),
            usuario=data.get('usuario'),
            contraseña=data.get('contraseña'),
            rol=data.get('rol', 'usuario')
        )
