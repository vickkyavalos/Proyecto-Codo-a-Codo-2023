
from django.contrib import admin
from django.urls import path

from .views import Divulgacion, Psicologia,Astronomia,Biologia,Nosotros,Formulario


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Divulgacion.as_view(), name="Principal"),
    path('Psicologia/', Psicologia.as_view(), name="Psicologia"),
    path('Astronomia/', Astronomia.as_view(), name= "Astronomia"),
    path('Biologia/', Biologia.as_view(), name= "Biologia"),
    path('Formulario/', Formulario.as_view(), name= "Formulario"),
    path('Nosotros/', Nosotros.as_view(), name= "Nosotros")
]
