from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

urlpatterns = [
    #path('proccesses/', views.offers_view, name='proccesses'),
    # Otras URLs para otros types de requestes
    path('solicitudes/', views.solicitud_list, name='solicitudList'),
    path('solicitud/<id>', views.single_solicitud, name='singleSolicitud'),
    path('crearSolicitud/', csrf_exempt(views.solicitud_create), name='crearSolicitud'),
]