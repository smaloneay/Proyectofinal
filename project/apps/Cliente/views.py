from django.shortcuts import render

from .models import Cliente

def home(request):
    Clientes_registros= Cliente.objects.all()
    contexto={"clientes": Clientes_registros}
    return render(request, "Cliente/index.html", contexto)
    #return render(request,"index.html", {"Cliente", Clientes_registros})
