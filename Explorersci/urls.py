
from django.contrib import admin
from django.urls import path

from .views import Divulgacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Divulgacion.as_view(), name="Principal")
]
