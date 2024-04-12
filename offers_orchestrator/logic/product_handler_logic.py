# TODO: Arreglar import
from otra_app_products.logic import process_request_products

def send_request_to_products_handler(request_data):
    # TODO: Lógica para enviar la request al manejador de products: llamar a la función correspondiente en la otra aplicación
    response = process_request_products(request_data)
    return response