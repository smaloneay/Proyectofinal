from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import celular
from .forms import celularForm

def home(request):
    contexto={"app": "Aplicacion Producto "}
    return render(request,"Producto/index.html", contexto)


def home(request):
    celular_agregados= celular.objects.all()
    contexto={"celular": celular_agregados}
    return render(request, "Producto/index.html", contexto)
    #return render(request,"index.html", {"Cliente", Clientes_registros})


### Formulario Ingresar Productos###
def crear_celular(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = celularForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("Producto:home")
    else: 
        form = celularForm()
    return render(request, "Producto/crear.html", {"form": form})