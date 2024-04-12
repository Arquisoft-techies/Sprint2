from django.urls import path
from . import views

urlpatterns = [
    path('proccesses/', views.offers_view, name='proccesses'),
    # Otras URLs para otros types de requestes
]