from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
from functools import wraps
from controllers.auth_controller import AuthController
from controllers.usuario_controller import UsuarioController
from controllers.nota_controller import NotaController

# Crear blueprints
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuario')
nota_bp = Blueprint('nota', __name__, url_prefix='/nota')
main_bp = Blueprint('main', __name__)

# Decoradores de autenticación
def login_requerido(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_requerido(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('auth.login'))
        if session.get('rol') != 'admin':
            return redirect(url_for('main.acceso_denegado'))
        return f(*args, **kwargs)
    return decorated_function

# =====================
# Rutas de Autenticación
# =====================

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        resultado = AuthController.registrar()
        if resultado['exito']:
            return redirect(url_for('auth.login'))
        else:
            return render_template('auth/registro.html', 
                                 errores=resultado.get('errores', []))
    return render_template('auth/registro.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'usuario_id' in session:
        if session.get('rol') == 'admin':
            return redirect(url_for('usuario.panel_admin'))
        else:
            return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        resultado = AuthController.login()
        if resultado['exito']:
            if session.get('rol') == 'admin':
                return redirect(url_for('usuario.panel_admin'))
            else:
                return redirect(url_for('main.dashboard'))
        else:
            return render_template('auth/login.html', 
                                 error=resultado.get('mensaje'))
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    AuthController.logout()
    return redirect(url_for('auth.login'))

# =====================
# Rutas Principales
# =====================

@main_bp.route('/')
def index():
    if 'usuario_id' in session:
        if session.get('rol') == 'admin':
            return redirect(url_for('usuario.panel_admin'))
        else:
            return redirect(url_for('main.dashboard'))
    return redirect(url_for('auth.login'))

@main_bp.route('/dashboard')
@login_requerido
def dashboard():
    return render_template('dashboard.html', 
                         usuario=session.get('nombre'),
                         rol=session.get('rol'))

@main_bp.route('/acceso-denegado')
def acceso_denegado():
    return render_template('acceso_denegado.html'), 403

# =====================
# Rutas de Usuarios (Admin)
# =====================

@usuario_bp.route('/panel-admin')
@admin_requerido
def panel_admin():
    usuarios = UsuarioController.obtener_todos_usuarios()
    return render_template('admin/panel_admin.html',
                         usuarios=usuarios.get('usuarios', []),
                         usuario_actual_id=session.get('usuario_id'),
                         nombre_usuario=session.get('nombre'))

@usuario_bp.route('/crear', methods=['GET', 'POST'])
@admin_requerido
def crear_usuario():
    if request.method == 'POST':
        resultado = UsuarioController.crear_usuario()
        if resultado['exito']:
            return redirect(url_for('usuario.panel_admin'))
        else:
            return render_template('admin/crear_usuario.html',
                                 errores=resultado.get('errores', []))
    return render_template('admin/crear_usuario.html')

@usuario_bp.route('/editar/<int:usuario_id>', methods=['GET', 'POST'])
@admin_requerido
def editar_usuario(usuario_id):
    if usuario_id == session.get('usuario_id'):
        return redirect(url_for('usuario.mi_perfil'))
    
    usuario = UsuarioController.obtener_usuario(usuario_id)
    
    if not usuario['exito']:
        return redirect(url_for('usuario.panel_admin'))
    
    if request.method == 'POST':
        resultado = UsuarioController.actualizar_usuario(usuario_id)
        if resultado['exito']:
            return redirect(url_for('usuario.panel_admin'))
        else:
            return render_template('admin/editar_usuario.html',
                                 usuario=usuario.get('usuario', {}),
                                 errores=resultado.get('errores', []))
    
    return render_template('admin/editar_usuario.html',
                         usuario=usuario.get('usuario', {}))

@usuario_bp.route('/eliminar/<int:usuario_id>', methods=['POST'])
@admin_requerido
def eliminar_usuario(usuario_id):
    resultado = UsuarioController.eliminar_usuario(usuario_id, session.get('usuario_id'))
    if resultado['exito']:
        return jsonify(resultado)
    else:
        return jsonify(resultado), 400

@usuario_bp.route('/cambiar-rol/<int:usuario_id>', methods=['POST'])
@admin_requerido
def cambiar_rol(usuario_id):
    resultado = UsuarioController.cambiar_rol(usuario_id, session.get('usuario_id'))
    return jsonify(resultado)

@usuario_bp.route('/mi-perfil')
@login_requerido
def mi_perfil():
    usuario = UsuarioController.obtener_usuario(session.get('usuario_id'))
    return render_template('usuario/mi_perfil.html',
                         usuario=usuario.get('usuario', {}))

@usuario_bp.route('/actualizar-perfil', methods=['POST'])
@login_requerido
def actualizar_perfil():
    resultado = UsuarioController.actualizar_usuario(session.get('usuario_id'))
    if resultado['exito']:
        return jsonify(resultado)
    else:
        return jsonify(resultado), 400

# =====================
# Rutas de Notas
# =====================

@nota_bp.route('/mis-notas')
@login_requerido
def mis_notas():
    notas = NotaController.obtener_notas_usuario(session.get('usuario_id'))
    # Formatear fechas para los templates
    for nota in notas.get('notas', []):
        if hasattr(nota.get('fecha_creacion'), 'strftime'):
            nota['fecha_creacion_formateada'] = nota['fecha_creacion'].strftime('%d/%m/%Y')
        else:
            nota['fecha_creacion_formateada'] = str(nota.get('fecha_creacion', 'N/A'))
    return render_template('notas/mis_notas.html',
                         notas=notas.get('notas', []),
                         usuario=session.get('nombre'))

@nota_bp.route('/todas')
@admin_requerido
def todas_notas():
    notas = NotaController.obtener_todas_notas()
    # Formatear fechas para los templates
    for nota in notas.get('notas', []):
        if hasattr(nota.get('fecha_creacion'), 'strftime'):
            nota['fecha_creacion_formateada'] = nota['fecha_creacion'].strftime('%d/%m/%Y %H:%M')
        else:
            nota['fecha_creacion_formateada'] = str(nota.get('fecha_creacion', 'N/A'))
    return render_template('admin/todas_notas.html',
                         notas=notas.get('notas', []),
                         usuario=session.get('nombre'))

@nota_bp.route('/crear', methods=['GET', 'POST'])
@login_requerido
def crear_nota():
    if request.method == 'POST':
        resultado = NotaController.crear_nota(session.get('usuario_id'))
        if resultado['exito']:
            return redirect(url_for('nota.mis_notas'))
        else:
            return render_template('notas/crear_nota.html',
                                 errores=resultado.get('errores', []))
    return render_template('notas/crear_nota.html')

@nota_bp.route('/editar/<int:nota_id>', methods=['GET', 'POST'])
@login_requerido
def editar_nota(nota_id):
    nota = NotaController.obtener_nota(nota_id)
    
    if not nota['exito']:
        return redirect(url_for('nota.mis_notas'))
    
    # Verificar permisos
    if session.get('rol') != 'admin' and nota['nota']['usuario_id'] != session.get('usuario_id'):
        return redirect(url_for('main.acceso_denegado'))
    
    if request.method == 'POST':
        resultado = NotaController.actualizar_nota(nota_id, session.get('usuario_id'))
        if resultado['exito']:
            return redirect(url_for('nota.mis_notas'))
        else:
            return render_template('notas/editar_nota.html',
                                 nota=nota.get('nota', {}),
                                 errores=resultado.get('errores', []))
    
    return render_template('notas/editar_nota.html',
                         nota=nota.get('nota', {}))

@nota_bp.route('/eliminar/<int:nota_id>', methods=['POST'])
@login_requerido
def eliminar_nota(nota_id):
    nota = NotaController.obtener_nota(nota_id)
    
    if not nota['exito']:
        return jsonify({'exito': False, 'mensaje': 'Nota no encontrada'}), 404
    
    # Verificar permisos
    if session.get('rol') != 'admin' and nota['nota']['usuario_id'] != session.get('usuario_id'):
        return jsonify({'exito': False, 'mensaje': 'No tienes permiso'}), 403
    
    resultado = NotaController.eliminar_nota(nota_id, session.get('usuario_id'))
    if resultado['exito']:
        return jsonify(resultado)
    else:
        return jsonify(resultado), 400

@nota_bp.route('/ver/<int:nota_id>')
@login_requerido
def ver_nota(nota_id):
    nota = NotaController.obtener_nota(nota_id)
    
    if not nota['exito']:
        return redirect(url_for('nota.mis_notas'))
    
    # Verificar permisos
    if session.get('rol') != 'admin' and nota['nota']['usuario_id'] != session.get('usuario_id'):
        return redirect(url_for('main.acceso_denegado'))
    
    # Formatear fecha
    nota_data = nota.get('nota', {})
    if hasattr(nota_data.get('fecha_creacion'), 'strftime'):
        nota_data['fecha_creacion_formateada'] = nota_data['fecha_creacion'].strftime('%d de %B de %Y a las %H:%M')
    else:
        nota_data['fecha_creacion_formateada'] = str(nota_data.get('fecha_creacion', 'N/A'))
    
    return render_template('notas/ver_nota.html', nota=nota_data)


def registrar_rutas(app):
    """Registrar todos los blueprints en la aplicación"""
    app.register_blueprint(auth_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(nota_bp)
    app.register_blueprint(main_bp)
