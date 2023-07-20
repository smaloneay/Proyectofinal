from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import home, crear_celular
app_name="Producto"

urlpatterns = [
    path("", home, name="home"),
    path('crear/', crear_celular, name="crear"),
    
    
]

urlpatterns += staticfiles_urlpatterns()