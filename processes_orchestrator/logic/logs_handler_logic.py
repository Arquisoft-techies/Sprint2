# TODO: Arreglar import
from otra_app_logs.logic import process_request_logs

def send_request_to_logs_handler(request_data):
    # TODO: Lógica para enviar la request al manejador de logs: llamar a la función correspondiente en la otra aplicación
    response = process_request_logs(request_data)
    return response