from django.views.generic import TemplateView

class Divulgacion(TemplateView):
    template_name = "index.html"

class Psicologia(TemplateView):
    template_name = "psicologia.html"

class Astronomia(TemplateView):
    template_name = "astronomia.html"