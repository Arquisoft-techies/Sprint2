# TODO: Arreglar import
from otra_app_services.logic import process_request_services

def send_request_to_services_handler(request_data):
    # TODO: Lógica para enviar la request al manejador de services: llamar a la función correspondiente en la otra aplicación
    response = process_request_services(request_data)
    return response