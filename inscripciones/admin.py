from django.contrib import admin

# Register your models here.
class InscripcionesAdmin (admin.ModelAdmin):

    list_display = (
        'id',
        'curso_titulo', 
        'curso_publicado',
        'curso_contenido',
        'curso_costo',
        )

admin.site.register(Curso, CursoAdmin)