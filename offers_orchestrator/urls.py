from django.urls import path
from . import views

urlpatterns = [
    path('offers/', views.ofertas_view, name='offers'),
    # Otras URLs para otros tipos de solicitudes
]