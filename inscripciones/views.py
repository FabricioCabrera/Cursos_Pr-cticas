from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main.models import Curso
from .models import Inscripcion
from .user import User
from .form import EstudianteForm, InscripcionForm, RegistroForm
# Create your views here.

def inscripcionesform(request,pk):
    print('Ingreso a Inscripción')
    registro_form = RegistroForm(prefix='form_registro')
    inscripcion_form = InscripcionForm(prefix='form_inscripcion') 

    contexto = {
        'registro_form':registro_form,
        'inscripcion_form':inscripcion_form

    }
    if request.method == 'POST':
        registro_form = RegistroForm(request.POST, prefix='form_registro')
        inscripcion_form = InscripcionForm(request.POST, prefix='form_inscripcion')
        
        if registro_form.is_valid() and inscripcion_form.is_valid():
            estudiante = registro_form.save(commit=False)
            estudiante.user = request.user
            estudiante.save()
            curso = Curso.objects.get(pk = pk)
           
            return redirect('inscribirse:lista_estudiantes')
        else:
            print('Error en los forms')
            print(inscripcion_form.errors)
            messages.error(request, registro_form.errors)
            messages.error(request, inscripcion_form.errors)
            
    return render(request,'inscripciones/inscripcion_form.html', contexto)

