from django import forms
from  .models import Incripciones


class InscripcionesForm(forms.ModelForm):
    class Meta:
        model = Incripciones
        fields = '__all__'