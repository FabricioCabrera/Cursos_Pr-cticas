from django.contrib import admin
from django.utils.html import format_html
from .models import Curso


  # Register your models here.
class CursoAdmin (admin.ModelAdmin):

    list_display = (
        'id',
        'curso_titulo', 
        'curso_publicado',
        'curso_contenido',
        'curso_costo',
        'images',
        )

    def images(self, obj):
        return format_html('<img src={} width="130" height="100"/>', obj.image.url)
        

admin.site.register(Curso, CursoAdmin)

  