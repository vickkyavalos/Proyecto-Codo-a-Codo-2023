
from django.contrib import admin
from django.urls import path

from .views import Divulgacion, Psicologia,Astronomia


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Divulgacion/', Divulgacion.as_view(), name="Principal"),
    path('Psicologia/', Psicologia.as_view(), name="psicologia"),
    path('Astronomia/', Astronomia.as_view(), name= "Astronomia")
]
