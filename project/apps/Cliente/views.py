from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Cliente
from .forms import ClienteForm




def home(request):
    Clientes_registros= Cliente.objects.all()
    contexto={"Cliente": Clientes_registros}
    return render(request, "Cliente/index.html", contexto)
    #return render(request,"index.html", {"Cliente", Clientes_registros})


def crear_cliente(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cliente:home")
    else:  # request.method == "GET"
        form = ClienteForm()
    return render(request, "Cliente/crear.html", {"form": form})


def busqueda(request: HttpRequest)-> HttpResponse:
    if request.method == 'POST':
        # Obtener el término de búsqueda del formulario
        termino_busqueda = request.POST.get('termino_busqueda')
        # Realizar la búsqueda en la base de datos
        Cliente = Cliente.objects.filter(nombre__icontains=termino_busqueda)
        # Pasar los resultados de la búsqueda al contexto
        context = {'Cliente': Cliente}
        return render(request, 'usuarios/buscar_usuarios.html', context)
    else:
        return render(request, 'Cliente/search.html')
    
    
    
    
    cliente_nombre=Cliente.objects.filter(nombre__contains="fia")
    contexto= {
        "clientes_nombre": cliente_nombre
    }
    return render(request,"Cliente/search.html",contexto)