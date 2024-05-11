from django.http import HttpResponseRedirect, HttpResponse
from .forms import SolicitudForm
from django.shortcuts import render
from sprint.auth0backend import getRole
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.solicitudes_logic import crear_solicitud, get_solicitudes, get_solicitud
from django.contrib.auth.decorators import login_required

# def offers_view(request: HttpRequest):
#     if request.method == 'POST':
#         dato = request.POST.get('', '')
#         dato2 = Product.objects.raw('SELECT * FROM  WHERE  = %s', [dato])
#         response = {    
#             'respuesta': dato2
#         }
#     else:
#         response = {
#             'message': 'Solicitud recibida y procesada exitosamente'
#         }
#     return render(request, 'procesos.html', response)

@login_required
def solicitud_list(request):
    role = getRole(request)
    if role == "Gerencia Campus":
        solicitudes = get_solicitudes()
        context = {
            'solicitud_list': solicitudes
        }
        return render(request, 'Solicitud/solicitudes.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def single_solicitud(request, id=0):
    solicitud = get_solicitud(id)
    context = {
        'solicitud': solicitud
    }
    return render(request, 'Solicitud/solicitud.html', context)

@login_required
def solicitud_create(request):
    role = getRole(request)
    if role == "Gerencia Campus":
        if request.method == 'POST':
            form = SolicitudForm(request.POST)
            if form.is_valid():
                crear_solicitud(form)
                messages.add_message(request, messages.SUCCESS, 'La solicitud se creó existosamente')
                return HttpResponseRedirect(reverse('crearSolicitud'))
            else:
                print(form.errors)
        else:
            form = SolicitudForm()

        context = {
            'form': form,
        }
        return render(request, 'Solicitud/crearSolicitud.html', context)
    else:
        return HttpResponse("Unauthorized User")