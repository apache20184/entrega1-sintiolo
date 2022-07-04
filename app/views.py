from django.shortcuts import render 
from django.http import HttpResponse
from app.models import Familiar
from django.template import Context, Template
# Create your views here.
def creacion_tablas (request):
    mihtml=open(r"C:\Users\Alejo\Documents\trabajo2\proyecto2\app\templates\template.html")
    plantilla= Template(mihtml.read())
    
       
    familia = Familiar (nombre="pablo", fecha_de_nacimiento="1932-05-09",edad="40")
    
    familia.save()
    
    juan = Familiar (nombre="juan", fecha_de_nacimiento="1978-09-12",edad="35")
    juan.save()
    
    julieta = Familiar (nombre="julieta", fecha_de_nacimiento="1999-04-24",edad="78")
    julieta.save()
    micontexto= Context({"Familia":familia, "juan":juan, "julieta":julieta})
    documento=plantilla.render(micontexto)
    mihtml.close()
    return HttpResponse(documento)

    