from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def busqueda_productos(request):
    return render(request, "busq_prod.html")

def buscar(request):
    if request.GET['producto']:
        #mensaje = "Articulo buscado: %r" %request.GET['producto']
        prod = request.GET['producto']

        if len(prod) > 20:
            
            mensaje = "Texto demasiado grande"
        
        else:
            
            articulos = Articulos.objects.filter(nombre__icontains=prod) #icontrains actua como un like nombre="" de sql
            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query": prod})

    else:
        mensaje = "No has introducido nada"

    return HttpResponse(mensaje)


def contacto(request):
    if request.method == "POST":
        asunto = request.POST['asunto']

        mensaje = request.POST['mensaje'] + "  " + request.POST['email']

        email_from = settings.EMAIL_HOST_USER

        email_to = ['juanmitaofunkatico@gmail.com']

        send_mail(asunto, mensaje, email_from, email_to)

        return  render(request, "gracias.html")

    return render(request, "contacto.html")

