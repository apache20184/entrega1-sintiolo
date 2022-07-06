from django.shortcuts import redirect, render 
from django.http import HttpResponse
from app.models import Familiar
from django.template import Context, Template
from .forms import FormFamiliar, BusquedaFamiliar
from datetime import datetime
# Create your views here.

def creacion_tablas (request):
    if request.method == 'POST':
        form = FormFamiliar(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_de_nacimiento')
            if not fecha:
                fecha = datetime.now() 
            
            familia = Familiar(
                nombre=data.get('nombre'),
                edad=data.get('edad'),
                fecha_de_nacimiento=fecha
               
            )
            familia.save()

            return redirect('listado')
        
        else:
            return render(request, 'formulario2.html', {'form': form})
            
    
    form_familiar = FormFamiliar()
    
    return render(request, 'formulario2.html', {'form': form_familiar})


def listadovista(request):
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        listado_familia = Familiar.objects.filter(nombre__icontains=nombre_de_busqueda) 
    else:
        listado_familia = Familiar.objects.all()
    
    form = BusquedaFamiliar()
    return render(request, 'listado.html', {'listado_familiar': listado_familia, 'form': form})
    
def nosotros(request):
     return render(request, 'nosotrostemplate.html',)
 
def inicio(request):
    return render(request, 'index.html')