
def procesar_solicitud_de_usuarios(datos_solicitud):
    if validar_datos(datos_usuario):
        #Lógica para crear el usuario
        return {'success': True, 'mensaje': "Usuario creado correctamente"}
    else:
        return {'success': False, 'mensaje': "Datos de usuario no válidos"}

def validar_datos(datos_usuario):
    if 'nombre' in datos_usuario and 'correo' in datos_usuario:
        if '@' in datos_usuario['correo']:
            return True
    return False