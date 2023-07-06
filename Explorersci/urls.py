
from django.contrib import admin
from django.urls import path

from .views import Divulgacion, Psicologia,Astronomia,Biologia,Nosotros


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Divulgacion/', Divulgacion.as_view(), name="Principal"),
    path('Psicologia/', Psicologia.as_view(), name="psicologia"),
    path('Astronomia/', Astronomia.as_view(), name= "Astronomia"),
    path('Biologia/', Biologia.as_view(), name= "Biologia"),
    path('Nosotros/', Nosotros.as_view(), name= "Nosotros")
]
