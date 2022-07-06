from django import forms

class FormFamiliar(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_de_nacimiento = forms.DateField(required=False)
    
class BusquedaFamiliar(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)