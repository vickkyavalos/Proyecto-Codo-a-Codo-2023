
from django.contrib import admin
from django.urls import path

from .views import Divulgacion, Astronomia,Biologia,Historia,Nosotros,Psicologia,Formulario,Contacto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Divulgacion.as_view(), name="Principal"),
    path('Astronomia/', Astronomia.as_view(), name= "Astronomia"),
    path('Biologia/', Biologia.as_view(), name= "Biologia"),
    path('Historia/', Historia.as_view(), name= "Historia"),
    path('Psicologia/', Psicologia.as_view(), name="Psicologia"),
    path('Formulario/', Formulario.as_view(), name= "Formulario"),
    path('Contacto/', Contacto.as_view(), name= "Contacto"),
    path('Nosotros/', Nosotros.as_view(), name= "Nosotros")
]
