from django.urls import path
from .views import home
app_name="Producto"

urlpatterns = [
    path("", home, name="home"),
]
