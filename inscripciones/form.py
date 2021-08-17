from django import forms
from  .models import Inscripcion
from django.contrib.auth.models import User
from django.db.models import fields


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username'
        ]
        labels = {
            'username': 'Nombre de usuario',
            

        }

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'