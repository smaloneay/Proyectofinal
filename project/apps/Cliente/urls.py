from django.urls import path
from .views import home
app_name="Cliente"
urlpatterns = [
    path('', home, name="home"),
]
