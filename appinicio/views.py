from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from appinicio.models import Auto
from appinicio.forms import CrearAutoFormulario

fecha = datetime.now()

def inicio(request):
    # return HttpResponse ('Bienvenidos a mi inico')
    return render(request, 'appinicio/index.html')

def template1(request, nombre, apellido):
    return HttpResponse(f'<h1>Mi Template 1</h1> -- Fecha: {fecha} -- Buenas {nombre} {apellido}')

def template2 (request, nombre, apellido):
       
    template = loader.get_template('template2.html')
    
    datos = {
        'fecha': fecha,
        'nombre': nombre ,
        'apellido': apellido ,
    }

    return render (request, 'template2.html',datos)

def crear_auto(request):
    
    print('Valor de la request: ' , request)
    print('Valor de GET: ' , request.GET)
    print('Valor de POST: ' , request.POST)
    
    if request.method == 'POST':
        formulario = CrearAutoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            auto = Auto(marca=datos.get('marca'),modelo=datos.get('modelo'))
            auto.save()
            return redirect('autos')
        
    formulario = CrearAutoFormulario(request.POST)
    return render(request, 'appinicio/creacion.html', {'formulario': formulario})


def autos(request):
    
    autos = Auto.objects.all()
    
    return render(request, 'appinicio/autos.html', {'autos': autos})

