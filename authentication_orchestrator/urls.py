from django.urls import path
from . import views

urlpatterns = [
    path('authentication/', views.offers_view, name='authentication'),
    # Otras URLs para otros tipos de requestes
]