from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from sys import prefix
from typing import ContextManager
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main.models import Curso
from .models import Inscripcion
from .form import EstudianteForm, InscripcionForm, RegistroForm
# Create your views here.

def inscripcionesform(request,pk):
    
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
            inscripcion = inscripcion_form.save(commit=False)
            inscripcion.curso = curso
            inscripcion.estudiante = estudiante
            inscripcion.save()
            return redirect('inscripciones:lista_estudiantes')
        else:
            print('Error en los forms')
            print(inscripcion_form.errors)
            messages.error(request, registro_form.errors)
            messages.error(request, inscripcion_form.errors)
            
    return render(request,'inscripciones/inscripcion_form.html', contexto) 

    
def lista_estudiantes(request):

    return render(request, "inscripciones/lista_inscritos.html", {"inscritos_curso":Inscripcion.objects.all})

def eliminar_inscripcion(request,id):
    incripcion = Inscripcion.objects.get(id = id)
    incripcion.delete()
    return redirect('inscripciones:lista_estudiantes')

def editar_inscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id = id)
    user = inscripcion.estudiante
    if request.method == 'GET':
        estudiante_form = EstudianteForm(instance=user)
        inscripcion_form = InscripcionForm(instance=inscripcion) 
        contexto = {
        'estudiante_form':estudiante_form,
        'inscripcion_form':inscripcion_form

        }
    else:
        estudiante_form = EstudianteForm(request.POST, instance=user)
        inscripcion_form = InscripcionForm(request.POST, instance=inscripcion) 
        contexto = {
        'estudiante_form':estudiante_form,
        'inscripcion_form':inscripcion_form

        }
        if estudiante_form.is_valid() and inscripcion_form.is_valid():
            estudiante = estudiante_form.save(commit=False)
            estudiante.user = request.user
            estudiante.save()
            
            inscripcion = inscripcion_form.save(commit=False)
            inscripcion.estudiante = estudiante
            inscripcion.save()
            return redirect('inscripciones:lista_estudiantes')

        else:
            print('Error en los forms')
            print(inscripcion_form.errors)
            messages.error(request, estudiante_form.errors)
            messages.error(request, inscripcion_form.errors)
    return render(request,'inscripciones/editar_form.html', contexto)