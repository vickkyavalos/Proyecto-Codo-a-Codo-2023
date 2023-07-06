from django.views.generic import TemplateView

class Divulgacion(TemplateView):
    template_name = "index.html"

class Psicologia(TemplateView):
    template_name = "psicologia.html"

class Astronomia(TemplateView):
    template_name = "astronomia.html"
    
class Biologia(TemplateView):
    template_name = "bio4.html"
    
class Nosotros(TemplateView):
    template_name = "nosotro.html"