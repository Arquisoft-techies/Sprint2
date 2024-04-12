from django.urls import path
from . import views

urlpatterns = [
    path('proccesses/', views.ofertas_view, name='proccesses'),
    # Otras URLs para otros tipos de solicitudes
]