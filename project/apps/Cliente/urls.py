from django.urls import path
from .views import home, crear_cliente,busqueda
app_name="Cliente"
urlpatterns = [
    path('', home, name="home"),
    path('crear/', crear_cliente, name="crear"),
    path('busqueda/',busqueda, name="busqueda")
]
