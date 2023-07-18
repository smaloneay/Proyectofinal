from django.shortcuts import render

def home(request):
    contexto={"app": "Aplicacion Producto "}
    return render(request,"Producto/index.html", contexto)



from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import curso
from .forms import cursoForm




def home(request):
    cursos_agregados= curso.objects.all()
    contexto={"curso": cursos_agregados}
    return render(request, "Producto/index.html", contexto)
    #return render(request,"index.html", {"Cliente", Clientes_registros})


def crear_curso(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = cursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Producto:home")
    else:  # request.method == "GET"
        form = cursoForm()
    return render(request, "Producto/crear.html", {"form": form})