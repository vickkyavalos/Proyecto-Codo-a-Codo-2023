from django.views.generic import TemplateView

class Divulgacion(TemplateView):
    template_name = "index.html"

class Astronomia(TemplateView):
    template_name = "astronomia.html"

class Biologia(TemplateView):
    template_name = "bio4.html"

class Historia(TemplateView):
    template_name= "historia.html"

class Psicologia(TemplateView):
    template_name = "psicologia.html"
        
class Formulario(TemplateView):
    template_name = "formulario.html"

class Contacto(TemplateView):
    template_name = "contacto.html"

class Nosotros(TemplateView):
    template_name = "nosotro.html"

