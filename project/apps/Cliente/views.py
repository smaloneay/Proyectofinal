from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import is_valid_path
from .models import Cliente, Pais
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




def busqueda(request: HttpRequest) -> HttpResponse:
    # Búsqueda por nombre que contenga "dana"
    cliente_nombre = Cliente.objects.filter(nombre__contains="dana")

    # Nacimientos  mayores a 2000
    cliente_nacimiento = Cliente.objects.filter(
        nacimiento__gt=date(2000, 1, 1))

    # País de origen vacío
    cliente_pais = Cliente.objects.filter(pais_origen_id=None)

    contexto = {
        "clientes_nombre": cliente_nombre,
        "clientes_nacimiento": cliente_nacimiento,
        "clientes_pais": cliente_pais
    }
    return render(request, "Cliente/search.html", contexto)