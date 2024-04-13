from .modelos import Cliente

def actualizar_datos_cliente(numero_identificacion, nuevos_datos):
    try:
        cliente = Cliente.objects.get(numero_identificacion = numero_identificacion)
        for calve, valor in nuevos_datos.items():
            setattr(cliente, clave, valor)

        cliente.save()

        return True
    
    except Cliente.DoesNotExist:
        return False
