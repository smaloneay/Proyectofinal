from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Cliente, Pais
from .forms import ClienteForm




def home(request):
    Clientes_registros= Cliente.objects.all()
    contexto={"Cliente": Clientes_registros}
    return render(request, "Cliente/index.html", contexto)
    #return render(request,"index.html", {"Cliente", Clientes_registros})

def crear_clientes(request):
    from datetime import date

    p1= Pais(nombre="Mexico")
    p2= Pais(nombre= "Peru")
    p3= Pais(nombre= "Uruguay")

    p1.save()
    p2.save()
    p3.save()

    c1= Cliente(nombre="Almendra", apellido="Darwin", nacimiento=date(2015,1,1),pais_origen_id=p1)
    c2= Cliente(nombre="Pepe", apellido="Jose", nacimiento=date(2000,5,8),pais_origen_id=p2)
    c3= Cliente(nombre="Juan", apellido="Sanchez", nacimiento=date(2002,2,3),pais_origen_id=p3)
    c4= Cliente(nombre="Sofia", apellido="Andrio", nacimiento=date(2004,4,5),pais_origen_id=None)

    c1.save()
    c2.save()
    c3.save()
    c4.save()
    return redirect("Cliente:home")

def crear_cliente(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Producto:home")
    else:  # request.method == "GET"
        form = ClienteForm()
    return render(request, "Cliente/crear.html", {"form": form})

def busqueda(request: HttpRequest)-> HttpResponse:
    cliente_nombre=Cliente.objects.filter(nombre__contains="fia")
    contexto= {
        "clientes_nombre": cliente_nombre
    }
    return render(request,"Cliente/search.html",contexto)