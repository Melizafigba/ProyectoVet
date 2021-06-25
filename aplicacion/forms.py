from django import forms
from .models import Animal

class PostFormulario(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('autor', 'nombre', 'especie','receta_medica', 'fecha_emision','precio_consulta',)




