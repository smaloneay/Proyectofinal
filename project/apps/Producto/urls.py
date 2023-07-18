from django.urls import path
from .views import home, crear_curso
app_name="Producto"

urlpatterns = [
    path("", home, name="home"),
    path('crear/', crear_curso, name="crear"),
    
]
