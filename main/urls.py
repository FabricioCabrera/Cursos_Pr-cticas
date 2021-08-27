from django.urls import path, include
from . import views


app_name= 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('registro/', views.registro, name="registro"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),
    path('guardarCurso/', views.curso_form, name='guardarCurso'),
    path('inscritos_curso/<int:id>/', views.inscritosCurso, name="inscritos_curso"),
  
    path('editarCurso/<int:id>/', views.editarCurso, name= 'editarCurso'),
    path('eliminarCurso/<int:id>/', views.eliminarCurso, name= 'eliminarCurso'),
    path('lista_form/', views.lista_form, name= 'lista_form'),
]
