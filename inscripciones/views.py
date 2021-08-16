from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main.models import Curso
from .models import Incripciones
from .form import CursoForm

# Create your views here.
