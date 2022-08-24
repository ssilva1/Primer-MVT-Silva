from django.shortcuts import render
from .models import Familia
from datetime import date

def familia(request):
    return render(request, 'familia.html', contexto={})

#def crear_integrante(request):
#    integrante = Familia.objects.create(
#        nombre_y_apellido = 'Teodoro Silva',
#        dni = 38123456,
#        fecha_nacimiento = date(year=1993,month=5, day=14), 
#    )
#    contexto = {'integrante': integrante}
    
#    return render(request, 'familia.html', contexto)

def ver_integrantes(request):
    integrantes = Familia.objects.all()
    contexto = {'integrantes': integrantes}
    
    return render(request, 'familia.html', contexto)
