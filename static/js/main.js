// Funciones auxiliares para modales
function abrirModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('show');
    }
}

function cerrarModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('show');
    }
}

// Cerrar modal al hacer click fuera
function configurarModales() {
    const modales = document.querySelectorAll('.modal');
    modales.forEach(modal => {
        modal.addEventListener('click', function(e) {
            if (e.target === this) {
                this.classList.remove('show');
            }
        });
    });
}

// Confirmar eliminación
function confirmarEliminacion(mensaje = '¿Estás seguro de que deseas eliminar este elemento?') {
    return confirm(mensaje);
}

// Mostrar alerta
function mostrarAlerta(mensaje, tipo = 'info') {
    const alertaDiv = document.createElement('div');
    alertaDiv.className = `alert alert-${tipo}`;
    alertaDiv.innerHTML = `
        <div style="flex: 1;">${mensaje}</div>
        <button class="alert-close" onclick="this.parentElement.remove()">×</button>
    `;
    
    const container = document.querySelector('main') || document.body;
    container.insertBefore(alertaDiv, container.firstChild);
    
    // Auto-cerrar después de 5 segundos
    setTimeout(() => {
        if (alertaDiv.parentElement) {
            alertaDiv.remove();
        }
    }, 5000);
}

// Validar formulario
function validarFormulario(formulario) {
    const inputs = formulario.querySelectorAll('input[required], textarea[required], select[required]');
    let valido = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.classList.add('is-invalid');
            valido = false;
        } else {
            input.classList.remove('is-invalid');
        }
    });
    
    return valido;
}

// Enviar formulario vía AJAX
function enviarFormularioAJAX(formulario, urlEnvio, redirectUrl = null) {
    if (!validarFormulario(formulario)) {
        mostrarAlerta('Por favor completa todos los campos requeridos', 'warning');
        return;
    }
    
    const datos = new FormData(formulario);
    
    fetch(urlEnvio, {
        method: 'POST',
        body: datos
    })
    .then(response => response.json())
    .then(data => {
        if (data.exito) {
            mostrarAlerta(data.mensaje, 'success');
            if (redirectUrl) {
                setTimeout(() => {
                    window.location.href = redirectUrl;
                }, 1500);
            }
        } else {
            const errores = data.errores || [data.mensaje];
            mostrarAlerta(errores.join('<br>'), 'danger');
        }
    })
    .catch(error => {
        mostrarAlerta('Error al procesar la solicitud', 'danger');
        console.error('Error:', error);
    });
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    configurarModales();
});
