# TODO: Arreglar import
from otra_app_riskanalysis.logic import process_request_riskanalysis

def send_request_to_riskanalysis_handler(request_data):
    # TODO: Lógica para enviar la request al manejador de analisisriesgos: llamar a la función correspondiente en la otra aplicación
    response = process_request_riskanalysis(request_data)
    return response