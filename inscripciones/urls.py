from django.urls import path, include
from . import views



urlpatterns = [
    path('inscripcionesform/<int:pk>/', views.inscripcionesform, name='inscripcionesform'),

]
