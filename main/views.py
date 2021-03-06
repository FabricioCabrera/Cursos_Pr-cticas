from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib import messages
from inscripciones.models import*
from .models import Curso
from .form import CursoForm
from django.db.models import Sum
#from .form import*
#from django.http import HttpResponseRedirect

# Create your views here.

def homepage(request):
     return render(request, "main/inicio.html", {"cursos": Curso.objects.all})

def registro(request):
     
     if request.method =="POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
               usuario = form.save()
               nombre_usuario = form.cleaned_data.get('username')
               messages.success(request, f"Nueva Cuenta Creada: {nombre_usuario}")
               login(request, usuario)
               messages.info(request, f"Has sido logeado como: {nombre_usuario}")
               return redirect("main:homepage")
          else:
               for msg in form.error_messages:
                    messages.error(request, f"{msg}: {form.error_messages[msg]}")

     form = UserCreationForm
     return render(request, "main/registro.html", {"form": form})

def logout_request(request):
     logout(request)
     messages.info(request, "Saliste exitosamente")
     return redirect("main:homepage")

def login_request(request):

     if request.method == "POST":
          form = AuthenticationForm(request, data=request.POST)
          if form.is_valid():
               usuario = form.cleaned_data.get('username')
               contraseña = form.cleaned_data.get('password')
               user = authenticate(username=usuario, password= contraseña)
               
               if user is not None:
                    login(request, user)
                    messages.info(request, f"Estás logiado como {usuario}")
                    return redirect("main:homepage")
               else:
                    messages.error(request, "Usuario o contraseña equivocada")
          else:    
               messages.error(request, "Usuario o contraseña equivocada")

     form = AuthenticationForm()
     return render(request, "main/login.html", {"form": form})

def curso_form(request):
    if request.method == 'GET':
        form = CursoForm
        contexto = {
        'form' : form
        }
    else:
        form = CursoForm(request.POST, request.FILES)
        contexto = {
        'form' : form
        }
        if form.is_valid():
               form.save()
               return redirect('main:homepage')

    return render(request,  "main/guardarCurso.html", contexto)


def inscritosCurso(request, id):
    curso = Curso.objects.get(id=id)
    inscritos_curso = Inscripcion.objects.filter(curso = curso)
    suma_costos = inscritos_curso.aggregate(Sum('costo_total'))
    contexto = {
        'curso': curso,
        'inscritos_curso': inscritos_curso, 
        'suma_costos': suma_costos  
    }
    return render(request, 'inscripciones/lista_inscritos.html', contexto)

def lista_form(request):
    return render(request, "main/lista_Cursos.html", {"cursos":Curso.objects.all})


def editarCurso(request,id):
    curso = Curso.objects.get(id = id)
    if request.method == 'GET':
        form = CursoForm(instance= curso)
        contexto = {
            'form': form
        }
    else:
        form = CursoForm(request.POST, request.FILES, instance= curso)
        contexto = {
            'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('main:lista_form')
    return render(request, "main/guardarCurso.html", contexto)

def eliminarCurso(request,id):
    curso = Curso.objects.get(id = id)
    curso.delete()
    return redirect('main:lista_form')
