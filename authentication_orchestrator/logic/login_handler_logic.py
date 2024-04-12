# TODO: Arreglar import
from otra_app_login.logic import process_request_login

def send_request_to_login_handler(request_data):
    # TODO: Lógica para enviar la request al manejador de login: llamar a la función correspondiente en la otra aplicación
    response = process_request_login(request_data)
    return response