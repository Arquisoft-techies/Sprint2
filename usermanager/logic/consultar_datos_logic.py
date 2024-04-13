from .models import Cliente

def usuario_existe(basic_info):
    nombres = basic_info.get('nombres')
    apellidos = basic_info.get('apellidos')
    pais = basic_info.get('pais')
    ciudad = basic_info('ciudad')
    telefono = basic_info('telefono')
    correo = basic_info.get('correo')


    usuario_existente = Login.objects.filter(nombres=nombres, apellidos=apellidos, pais=pais, 
    ciudad=ciudad, telefono=telefono, correo=correo).exists()

    return usuario_existente

def obtener_informacion_cliente(basic_info):
    nombres = basic_info.get('numero_identificacion')
    try:
        cliente = Cliente.objects.get(numero_identificacion=numero_identificacion)
        datos_cliente = {
            'nombre': cliente.nombre,
            'apellidos': cliente.apellidos,
            'tipo_identificacion': cliente.tipo_identificacion,
            'numero_identificacion': cliente.numero_identificacion,
            'correo': cliente.correo,
            'telefono': cliente.telefono,
            'pais': cliente.pais,
            'empresa': cliente.empresa,
            'actividad_economica': cliente.actividad_economica,
            'ingresos': cliente.ingresos,
            'deudas': cliente.deudas,
            'ciudad': cliente.ciudad,
            'profesion': cliente.profesion,
        }

        return datos_cliente

    except Cliente.DoesNotExist:
        return None
