from django.urls import path
from . import views

urlpatterns = [
    path('authentication/', views.ofertas_view, name='authentication'),
    # Otras URLs para otros tipos de solicitudes
]