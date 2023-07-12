from django.shortcuts import render
from .models import Cliente
def home(request):
    Clientes_registros= Cliente.objects.all()
    return render(request,"index.html", {"clientes", Clientes_registros})