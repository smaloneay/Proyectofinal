from django.shortcuts import render

def home(request):
    contexto={"app": "Aplicacion Producto "}
    return render(request,"index.html", {"Clientes", Clientes_registros})