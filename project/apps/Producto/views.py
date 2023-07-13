from django.shortcuts import render

def home(request):
    contexto={"app": "Aplicacion Producto "}
    return render(request,"Producto/index.html", contexto)